import face_recognition
import cv2
import numpy as np
import json

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

with open('E:\\iot project\\names_face_encodings.json',"r",encoding="utf-8") as f:
  names_encodings = json.load(f)

# Load arrays of known face encodings and their names from the above json file
known_face_encodings = list(names_encodings.values())
known_face_names = list(names_encodings.keys())
# print(len(known_face_encodings))
# print(known_face_names)

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

# prev_face_name = "Unknown"
prev_face_names = []

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            # print(matches)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame

    if face_names and face_names[0] not in prev_face_names:
        prev_face_names.append(face_names[0])

    # print(matches)
    # print(face_names)

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# print(face_names)
print("Recognised faces are:")
for val in prev_face_names:
    if val != "Unknown":
        # print(val, file=f)
        print(val)

# Store status of each person into dictionary
attendance_status = {}
prev_face_names = filter(lambda x: x != "Unknown", prev_face_names)
for val in known_face_names:
    if val in prev_face_names:
        attendance_status[val] = "Present"
    else:
        attendance_status[val] = "Absent"

# write the attendance_status dictionary into a json file
with open('E:\\iot project\\att_status.json', 'w', encoding='utf-8') as json_file:
  json.dump(attendance_status, json_file)

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
f.close()