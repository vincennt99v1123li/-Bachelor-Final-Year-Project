import cv2
import sys
import gc
from vin2_face_trainning_deep import Model
import pymysql
import datetime


def main(person_id,person,id):


    if len(sys.argv) != 1:
        print("Usage:%s camera_id\r\n" % (sys.argv[0]))
        sys.exit(0)
    # model = Model()
    # model.load_model(file_path='model/vin2.face.model.h5')

    #person = input("identify which person? (v/a)")

    file_path_link='model/'+person_id+'.face.model.h5'
    print('file_path'+str(file_path_link))

    model = Model()
    model.load_model(file_path=file_path_link)
    '''
    if person == "v" or person == "V":
        model = Model()
        model.load_model(file_path='model/101.face.model.h5')


    elif person == "a" or person == "A":
        model = Model()
        model.load_model(file_path='model/102.face.model.h5')
    '''
    print(model)

    color = (0, 255, 0)
    color2 = (0, 255, 255)
    color2 = (255, 0, 255)

    cap = cv2.VideoCapture(0)

    cascade_path = "cascades/data/haarcascade_frontalface_alt2.xml"

    flag=True

    while flag == True:
        ret, frame = cap.read()

        if ret is True:

            frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        else:
            continue

        cascade = cv2.CascadeClassifier(cascade_path)

        faceRects = cascade.detectMultiScale(frame_gray, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))



        if len(faceRects) > 0:
            for faceRect in faceRects:
                x, y, w, h = faceRect

                image = frame[y - 10: y + h + 10, x - 10: x + w + 10]
                faceID = model.face_predict(image)

                p1="v"
                if p1 == "v" or p1 == "V":
                    if faceID == 0:
                        cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), color, thickness=2)

                        cv2.putText(frame, str(person),
                                    (x + 30, y + 30),
                                    cv2.FONT_HERSHEY_SIMPLEX,
                                    1,
                                    (255, 0, 255),
                                    2)
                        #k  = 'q'

                        date_string = datetime.datetime.now()
                        db = pymysql.connect('localhost', 'root', '', 'fyp')
                        conn = pymysql.connect(user='root',
                                               password='',
                                               db='fyp',
                                               cursorclass=pymysql.cursors.DictCursor)
                        '''
                        pw = []
                        cur = conn.cursor()
                        cur.execute(
                            "select * from login_record")
                        for row in cur.fetchall():
                            pw.append(row)
                            print(pw)
                        '''

                        cur = conn.cursor()
                        sql = (
                            "insert into login_record (`Student_id`,`Login_date`,`time_table_id`) values (" +"'"+str(person_id)+"','"+str(date_string) +"','"+str(id)+ "') ")
                        print(sql)
                        cur.execute(sql)
                        conn.commit()

                        cv2.destroyAllWindows()
                        return("Success")
                        flag=False
                        #sys.exit()
                    elif faceID == 1:
                        label_name='Not '+str(person)
                        cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), color2, thickness=2)

                        cv2.putText(frame, str(label_name),
                                    (x + 30, y + 30),
                                    cv2.FONT_HERSHEY_SIMPLEX,
                                    1,
                                    (255, 0, 255),
                                    2)



        cv2.imshow("face reco"+str(person), frame)

        k = cv2.waitKey(10)

        if k & 0xFF == ord('q'):
            #return("Fail")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    sys.exit(main())
