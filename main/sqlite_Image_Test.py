import sqlite3
import os.path
from os import listdir, getcwd
from IPython.core.display import Image
import cv2

def get_picture_list(rel_path):
    abs_path = os.path.join(os.getcwd(),rel_path)
    print ('abs_path =', abs_path)
    dir_files = os.listdir(abs_path)
    #print dir_files
    return dir_files
picture_list = get_picture_list('ImageGUI')
print(picture_list)

def create_or_open_db(db_file):
    db_is_new = not os.path.exists(db_file)
    conn = sqlite3.connect(db_file)
    if db_is_new:
        print('Creating schema')
        sql = '''create table if not exists Suspects(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME STRING,
        GENDER STRING,
        PICTURE BLOB,
        TYPE TEXT,
        FILE_NAME TEXT);'''
        conn.execute(sql) # shortcut for conn.cursor().execute(sql)
    else:
        print('Schema exists\n')

    return conn

# def insert_picture(conn, picture_file):
#     with open(picture_file, 'rb') as input_file:
#         ablob = input_file.read()
#         base=os.path.basename(picture_file)
#         afile, ext = os.path.splitext(base)
#         sql = '''INSERT INTO Suspects
#         (PICTURE, TYPE, FILE_NAME)
#         VALUES(?, ?, ?);'''
#         conn.execute(sql,[sqlite3.Binary(ablob), ext, afile])
#         conn.commit()

# conn = create_or_open_db('picture_db.sqlite')
# picture_file = "./ImageGUI/6.jpg"
# insert_picture(conn, picture_file)
# conn.close()
#BULK INSERT
# conn = create_or_open_db('FaceNetdb.db')
# for fn in picture_list:
#     picture_file = "./ImageGUI/" + fn
#     insert_picture(conn, picture_file)

# for r in conn.execute("SELECT FILE_NAME FROM PICTURES"):
#     print
#     r[0]
#
# conn.close()

def extract_picture(cursor, picture_id):
    sql = "SELECT PICTURE, TYPE, FILE_NAME FROM Suspects WHERE id = :id"
    param = {'id': picture_id}
    cursor.execute(sql, param)
    ablob, ext, afile = cursor.fetchone()
    filename = afile + ext
    with open(filename, 'wb') as output_file:
        output_file.write(ablob)
    return filename

conn = create_or_open_db('FaceNetdb.db')
cur = conn.cursor()
filename = extract_picture(cur, 4)
print(filename)
cur.close()
conn.close()
Image(filename='./'+filename)

img = cv2.imread(filename)

# Output img with window name as 'image'
cv2.imshow('image', img)

# Maintain output window utill
# user presses a key
cv2.waitKey(0)
