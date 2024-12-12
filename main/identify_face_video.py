from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import tensorflow as tf
from scipy import misc
import cv2
import numpy as np
import facenet
import detect_face
import os
import time
from datetime import datetime
import pickle
import sqlite3

def main():
    input_http_url = "http://192.168.43.1:8080/video"
    input_video = "akshay_mov.mp4"
    modeldir = './model/20180402-114759.pb'
    classifier_filename = './class/classifier.pkl'
    npy = './npy'
    train_img = "./train_img"
    font = cv2.FONT_HERSHEY_SIMPLEX

    # -----------------------------------------------------------------------------------
    def draw_border(img, pt1, pt2, color, thickness, r, d):

        x1, y1 = pt1
        x2, y2 = pt2
        #  To make anglular turn remove + r and comment out ellipse
        # Top left
        cv2.line(img, (x1, y1), (x1 + d, y1), color, thickness)
        cv2.line(img, (x1, y1), (x1, y1 + d), color, thickness)
        # cv2.ellipse(img, (x1 , y1 ), (r, r), 180, 0, 90, color, thickness)
        # Top right
        cv2.line(img, (x2, y1), (x2 - d, y1), color, thickness)
        cv2.line(img, (x2, y1), (x2, y1 + d), color, thickness)
        # cv2.ellipse(img, (x2 , y1 + r), (r, r), 270, 0, 90, color, thickness)
        # Bottom left
        cv2.line(img, (x1 + r, y2), (x1 + r + d, y2), color, thickness)
        cv2.line(img, (x1, y2), (x1, y2 - d), color, thickness)
        # cv2.ellipse(img, (x1 + r, y2 ), (r, r), 90, 0, 90, color, thickness)
        # Bottom right
        cv2.line(img, (x2, y2), (x2 - d, y2), color, thickness)
        cv2.line(img, (x2, y2), (x2, y2 - d), color, thickness)
        # cv2.ellipse(img, (x2 , y2 ), (r, r), 0, 0, 90, color, thickness)

    # ----------------------------------------------------------------------------------
    def convertToBinary(filename):
        with open(filename, 'rb') as file:
            blobdata = file.read()
        return blobdata

    # def insertBLOB(photo):
    #     try :
    #         conn = sqlite3.connect('FaceNetdb.db')
    #         cmd = "INSERT INTO Suspects Image VALUE convertToBinary(photo) "
    #         suspectphoto = convertToBinary(photo)
    #         data_tuple = (suspectphoto)
    #         cursor = conn.cursor()
    #         cursor = conn.execute(cmd, data_tuple)
    #         cursor.close()
    #     except sqlite3.Error as error:
    #         print("Error")
    #     finally:
    #         if (conn):
    #             conn.close()
    #             print("closed connection")
    # insertBLOB("D:/AI Sagnam/Facenet-Real-time-face-recognition-using-deep-learning-Tensorflow-master/11.jpg")
    #

    def getProfile(Name):
        Name = (Name,)
        # print("chech ",Name)
        conn = sqlite3.connect('FaceNetdb.db')
        # cmd = "SELECT ID FROM Suspects Where  NAME ="
        cursor = conn.execute('SELECT ID  FROM Suspects WHERE NAME = ?', Name)
        # cursor = conn.execute(cmd)
        for row in cursor:
            print("ID = ", row[0])
            profile = row
        conn.close()
        return profile

    # def insertOrUpdate(Id, Name):
    #     conn = sqlite3.connect("FaceBase.db")
    #     cmd = "SELECT * FROM People Where  ID =" + str(id)
    #     cursor = conn.execute(cmd)
    #     isRecordExist = 0
    #     for row in cursor:
    #         isRecordExist=1
    #         if(isRecordExist == 1):
    #             cmd ="UPDATE People SET Name="str(Name)+ "where ID="+str(Id)
    #         else:
    #             cmd ="INSERT into People(ID,Name) Values("+str(Id)+"),"+str(Name)+")"
    #
    #         conn.execute(cmd)
    #         conn.commit()
    #         conn.close()

    with tf.Graph().as_default():
        gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.6)
        sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options, log_device_placement=False))
        with sess.as_default():
            pnet, rnet, onet = detect_face.create_mtcnn(sess, npy)

            minsize = 20  # minimum size of face
            threshold = [0.6, 0.7, 0.7]  # three steps's threshold
            factor = 0.709  # scale factor
            margin = 44
            frame_interval = 3
            batch_size = 1000
            image_size = 182
            input_image_size = 160

            HumanNames = os.listdir(train_img)
            HumanNames.sort()

            print('Loading Modal')
            facenet.load_model(modeldir)
            images_placeholder = tf.get_default_graph().get_tensor_by_name("input:0")
            embeddings = tf.get_default_graph().get_tensor_by_name("embeddings:0")
            phase_train_placeholder = tf.get_default_graph().get_tensor_by_name("phase_train:0")
            embedding_size = embeddings.get_shape()[1]

            classifier_filename_exp = os.path.expanduser(classifier_filename)
            with open(classifier_filename_exp, 'rb') as infile:
                (model, class_names) = pickle.load(infile)

            video_capture = cv2.VideoCapture(0)
            c = 0

            print('Start Recognition')
            prevTime = 0
            while True:
                ret, frame = video_capture.read()
                frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)  # resize frame (optional)

                curTime = time.time() + 1  # calc fps
                timeF = frame_interval

                cv2.putText(frame, str(datetime.now()), (350, 15), font, 0.56, (0, 0, 0), thickness=1, lineType=1)
                if (c % timeF == 0):
                    find_results = []

                    if frame.ndim == 2:
                        frame = facenet.to_rgb(frame)
                    frame = frame[:, :, 0:3]
                    bounding_boxes, _ = detect_face.detect_face(frame, minsize, pnet, rnet, onet, threshold, factor)
                    nrof_faces = bounding_boxes.shape[0]
                    print('Number of Detected_Faces : %d' % nrof_faces)

                    if nrof_faces > 0:
                        det = bounding_boxes[:, 0:4]
                        img_size = np.asarray(frame.shape)[0:2]

                        cropped = []
                        scaled = []
                        scaled_reshape = []
                        bb = np.zeros((nrof_faces, 4), dtype=np.int32)

                        for i in range(nrof_faces):
                            emb_array = np.zeros((1, embedding_size))

                            bb[i][0] = det[i][0]
                            bb[i][1] = det[i][1]
                            bb[i][2] = det[i][2]
                            bb[i][3] = det[i][3]

                            # inner exception
                            if bb[i][0] <= 0 or bb[i][1] <= 0 or bb[i][2] >= len(frame[0]) or bb[i][3] >= len(frame):
                                print('Face is very close!')
                                continue

                            cropped.append(frame[bb[i][1]:bb[i][3], bb[i][0]:bb[i][2], :])
                            cropped[i] = facenet.flip(cropped[i], False)
                            scaled.append(misc.imresize(cropped[i], (image_size, image_size), interp='bilinear'))
                            scaled[i] = cv2.resize(scaled[i], (input_image_size, input_image_size),
                                                   interpolation=cv2.INTER_CUBIC)
                            scaled[i] = facenet.prewhiten(scaled[i])
                            scaled_reshape.append(scaled[i].reshape(-1, input_image_size, input_image_size, 3))
                            feed_dict = {images_placeholder: scaled_reshape[i], phase_train_placeholder: False}
                            emb_array[0, :] = sess.run(embeddings, feed_dict=feed_dict)
                            predictions = model.predict_proba(emb_array)
                            # print(predictions)
                            best_class_indices = np.argmax(predictions, axis=1)
                            best_class_probabilities = predictions[
                                np.arange(len(best_class_indices)), best_class_indices]
                            # print("predictions")
                            print(best_class_indices,' with accuracy',best_class_probabilities)

                            print(best_class_probabilities)
                            if best_class_probabilities > 0.43:
                                draw_border(frame, (bb[i][0], bb[i][1]), (bb[i][2], bb[i][3]), (255, 255, 255), 2, 5,
                                            10)
                                # cv2.rectangle(frame, (bb[i][0], bb[i][1]), (bb[i][2], bb[i][3]), (0, 255, 0), 2)    #boxing face

                                # plot result idx under box
                                text_x = bb[i][0]
                                text_y = bb[i][3] + 20
                                # print('Result Indices: ', best_class_indices[0])
                                # print(HumanNames)
                                for H_i in HumanNames:
                                    if HumanNames[best_class_indices[0]] == H_i:
                                        result_names = HumanNames[best_class_indices[0]]
                                        cv2.putText(frame, result_names, (text_x, text_y),
                                                    cv2.FONT_HERSHEY_COMPLEX_SMALL,
                                                    1, (0, 0, 255), thickness=1, lineType=2)
                                        print(result_names)

                                        profile = getProfile(result_names)

                                        print(result_names, ' with accuracy ', best_class_probabilities)

                                        if (profile != None):
                                            print("with id ", str(profile[0]))
                                            # print("with Gender",str(profile[2]))

                    else:
                        print('Alignment Failure')
                # c+=1
                cv2.imshow('Video', frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            video_capture.release()
            cv2.destroyAllWindows()

if __name__ == "__main__":
    main()