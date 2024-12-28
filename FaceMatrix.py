import cv2
import face_recognition

# Load known face encoding and names
known_face_encodings = []
known_face_names = []

# load known faces and their names here
known_person1_image = face_recognition.load_image_file("C:\Users\srnis\Downloads\Documents\Face_Matrix\srn.jpg")
known_person2_image = face_recognition.load_image_file("C:\Users\srnis\Downloads\Documents\Face_Matrix\minhaj.jpg")
known_person3_image = face_recognition.load_image_file("C:\Users\srnis\Downloads\Documents\Face_Matrix\limon.jpg")
known_person4_image = face_recognition.load_image_file("C:\Users\srnis\Downloads\Documents\Face_Matrix\huda.jpg")
known_person5_image = face_recognition.load_image_file("C:\Users\srnis\Downloads\Documents\Face_Matrix\debobroto.jpg")

known_person1_encoding = face_recognition.face_encodings(known_person1_image) [0]
known_person2_encoding = face_recognition.face_encodings(known_person2_image) [0]
known_person3_encoding = face_recognition.face_encodings(known_person3_image) [0]
known_person4_encoding = face_recognition.face_encodings(known_person4_image) [0]
known_person5_encoding = face_recognition.face_encodings(known_person5_image) [0]
 
known_face_encodings.append(known_person1_encoding)
known_face_encodings.append(known_person2_encoding)
known_face_encodings.append(known_person3_encoding)
known_face_encodings.append(known_person4_encoding)
known_face_encodings.append(known_person5_encoding)

known_face_names.append("Sohanur Rahman Nishad")
known_face_names.append("MD Minhajul Islam")
known_face_names.append("Md Shamihul Islam Khan Limon")
known_face_names.append("Nurul Huda Laskor")
known_face_names.append("Debobroto Rudra Pal")

# Initialize webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame by frame
    ret, frame = video_capture.read()

    # find all face locations in the current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # loop through each face found in the frame
    for (top, right, bottom, left), face_encodings in zip(face_locations, face_encodings):

        # Check if the face matches any known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encodings)
        name = "Unknown Person"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Draw a box around the face and label with the name
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    # Display the resulting frame
    cv2.imshow("Video", frame)

    # break the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the webcame and close opencv windows
video_capture.release()
cv2.destroyAllWindows()

