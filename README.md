Smart Surveillance System
=========================

Overview
--------
Smart Surveillance System is a desktop application for real-time face detection and recognition.  
It frees security personnel from routine monitoring by automatically detecting, identifying, and alerting on “wanted” individuals in live camera feeds.

Key Features
------------
• Real-time face detection (MTCNN, Dlib HOG, Haar-cascade)  
• Face embedding via FaceNet (128-dimensional vectors + triplet-loss)  
• Face classification with SVM (trained on embeddings)  
• Add new suspects: capture name, metadata, profile image  
• “Align” & “Train” workflows to preprocess and fit new faces into the model  
• User management with login (SQLite backend)  
• Simple PyQt5 GUI: Start/Pause stream, Add/Search/Train suspects, Manage accounts  
• Instant pop-up of recognized suspect’s full profile  

System Requirements
-------------------
Hardware  
 • Logitech (or equivalent) webcam, 30 fps, ≥340×240  
 • PC with ≥2 GHz CPU, ≥8 GB RAM, GPU recommended for TensorFlow  

Software  
 • Python 3.7+  
 • OpenCV  
 • TensorFlow  
 • MTCNN (npy models)  
 • Dlib  
 • PyQt5  
 • SQLite3  
 • NumPy, SciPy  
 • scikit-learn  

Installation
------------
1. Clone the repo:
2. Create and activate a virtual environment:
3. Install dependencies:
4. Download pretrained MTCNN (`det1.npy`, `det2.npy`, `det3.npy`) into `./models/mtcnn/`  
5. Download FaceNet model (`20180402-114759.pb`) into `./models/facenet/`  
6. Initialize the SQLite database:

Usage
-----
1. Launch the GUI:
2. **Login** with an existing account or create a new one via the “Add Account” tab.  
3. **Add Suspect**: enter name, gender, race, birth year, criminal record, profile image & training folder.  
4. **Align**: preprocess all raw images into aligned faces.  
5. **Train**: build/update the SVM classifier (`classifier.pkl`) on all aligned embeddings.  
6. **Start**: begin live video stream; recognized faces will trigger a pop-up with full profile.  
7. **Pause**: temporarily halt detection/recognition.  
8. **Search**: retrieve any suspect’s stored profile by ID, name, or race.



Algorithmic Details
-------------------
1. **Face Detection**  
   • MTCNN: 3-stage CNN (P-Net, R-Net, O-Net) for fast, accurate bounding-box + landmarks  
   • Dlib HOG + linear SVM  
   • OpenCV Haar cascades  
2. **Feature Extraction**  
   • FaceNet maps each face → 128-dimensional vector  
   • Triplet loss minimizes same-identity distances, maximizes different-identity distances  
3. **Classification**  
   • SVM (linear kernel, probability outputs) over embeddings  
   • Decision boundary defined by support vectors  

Testing & Validation
--------------------
• Unit & integration tests for database, detection, embedding, classification  
• Accuracy evaluations on held-out video sequences  
• Real-time performance stress tests at 30 fps  
  
