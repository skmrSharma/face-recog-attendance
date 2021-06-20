import numpy as np
import face_recognition
import json

# f = open("E:\\iot project\\names_face_encodings.json", "w", encoding='utf-8')
# names_list.json contains roll_nos along with corresponding names
namesListFile = open("E:\\iot project\\names_list.json", "r", encoding='utf-8')
names = json.load(namesListFile)
namesListFile.close()
print(names)

# store the face_encodings of each detected face along with name in a dictionary
encodings_dict = {}
for i,val in names.items():
	print(i,val)
	f_image = face_recognition.load_image_file("E:\\iot project\\images\\n" + i + ".jpg")
	f_encoding = face_recognition.face_encodings(f_image)[0]
	encodings_dict[val] = f_encoding.tolist()


with open('E:\\iot project\\names_face_encodings.json', 'w') as json_file:
	json.dump(encodings_dict, json_file)

# Load a sample picture and learn how to recognize it.
# modi_image = face_recognition.load_image_file("E:\\iot project\\image face archive\\Five_Faces\\modi\\modi40.jpg")
# modi_face_encoding = face_recognition.face_encodings(modi_image)[0]
# print(modi_face_encoding)

# Load a second sample picture and learn how to recognize it.
# musk_image = face_recognition.load_image_file("E:\\iot project\\image face archive\\Five_Faces\\musk\\musk0.jpg")
# musk_face_encoding = face_recognition.face_encodings(musk_image)[0]