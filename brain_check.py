import cv2

# Create Cascade Classifier 
face_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

# This reas the Image 
img = cv2.imread('test.jpg')  

# Converting Image To Gray
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Search for codinates in image 
faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.05, minNeighbors=5)
for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y ), (x + w, y + h), (255, 255, 255), 3)

# Reshaping To Display Properly 
resized = cv2.resize(img, (int(img.shape[1]/7), int(img.shape[0]/7)))
cv2.imshow("Gray", img) # resized
cv2.waitKey()
cv2.destroyAllWindows()



