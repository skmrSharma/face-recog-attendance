import numpy as np
import face_recognition
import json

# f = open("E:\\iot project\\names_face_encodings.json", "w", encoding='utf-8')
# names_list.json contains roll_nos along with corresponding names
namesListFile = open("names_list.json", "r", encoding='utf-8')
names = json.load(namesListFile)
namesListFile.close()
print(names)

# store the face_encodings of each detected face along with name in a dictionary
encodings_dict = {}
for i,val in names.items():
	print(i,val)
	f_image = face_recognition.load_image_file("./images/n" + i + ".jpg")
	f_encoding = face_recognition.face_encodings(f_image)[0]
	encodings_dict[val] = f_encoding.tolist()


with open('names_face_encodings.json', 'w') as json_file:
	json.dump(encodings_dict, json_file)