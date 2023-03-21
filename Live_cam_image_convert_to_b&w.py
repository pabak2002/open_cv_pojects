import cv2
# faceCascade=cv2.CascadeClassifier("D:\opencv_practice\harcascade_files\haarcascade_frontalface_default.xml")
cap=cv2.VideoCapture(0)

img_counter=0

while True:
    ret,frame=cap.read()

    if not ret:
        break
    cv2.imshow("images",frame)

    k=cv2.waitKey(1)

    if(k%256==113):
        print("'q' pressed.......closing app")
        break

    elif k%256==32:
        img_name="opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name,frame)
        print("screenshot taken")
        img_counter+=1



for i in range(img_counter):
    img=cv2.imread(r'opencv_frame_{}.png'.format(i))
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # thresh,img_black=cv2.threshold(gray,170,255,cv2.THRESH_BINARY)
    cv2.imshow('Original image',img)
    cv2.imshow('Gray image',gray)
    # cv2.imshow('B/W image',img_black)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


