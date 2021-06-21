# face-recog-attendance
A python app for marking attendance using face recognition

## Usage

1. Train the model using face_recog_train.py
2. Test the model using face_recog_test.py

## How it Works

1. The face_recog_train.py generates the face encodings for the images in ./images directory.
2. The names are read from the names_list.json file, during the above step, and name-encoding pairs are stored into the JSON file.
3. The face_recog_test.py captures the feed from your webcam, and detects faces.
4. Encodings are generated for the detected faces and they are compared with the already available encodings.
5. If matches are found, they are marked as present. Those names that were not matched are marked absent.
