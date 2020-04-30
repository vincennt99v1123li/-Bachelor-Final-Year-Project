import cv2
import sys

from PIL import Image


def CatchPICFromVideo(window_name, camera_idx, catch_pic_num, path_name):
    cv2.namedWindow(window_name)
    cap = cv2.VideoCapture(0)
    classfier = cv2.CascadeClassifier("cascades/data/haarcascade_frontalface_alt2.xml")
    color = (255, 255, 0)

    num = 0
    while cap.isOpened():
        #print(path_name)
        ok, frame = cap.read()  # 讀取一幀資料
        if not ok:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


        faceRects = classfier.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
        if len(faceRects) > 0:
            for faceRect in faceRects:
                x, y, w, h = faceRect


                img_name = path_name+"/"+str(num)+'.jpg'
                #image = frame[y - 10: y + h + 10, x - 10: x + w + 10]

                roi_color = frame[y:y + h, x:x + w]

                cv2.imwrite(img_name, roi_color)

                num += 1
                if num > (catch_pic_num):
                    break


                #cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), color, 2)

                color = (255, 255, 0)  # in BGR
                stroke = 3
                end_cord_x = x + w
                end_cord_y = y + h
                cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)

                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, 'num:%d' % (num), (x + 30, y + 30), font, 1, (255, 0, 255), 4)

                #
        if num > (catch_pic_num): break


        cv2.imshow(window_name, frame)
        c = cv2.waitKey(10)
        if c & 0xFF == ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()
    return("Success")

if __name__ == '__main__':
    sys.exit(CatchPICFromVideo())
