import sys

from tkinter import ttk
import tkinter as tk
import tkinter.scrolledtext as tkst
from tkinter.constants import ACTIVE, DISABLED, NORMAL
from tkinter.constants import LEFT, BOTTOM
from tkinter import Button, Frame, Tk
from faulthandler import disable
import datetime
import time
from tkinter import END
# import cx_Oracle
# import login_loop_302
import clock
import json
import pymysql
import requests
import os

import vin3_face_recognition_test2
import vin3_cap_face
import vin3_face_trainning_deep

class Gui:
    def add_page_editarea(self, choice):
        if choice == "del" and self.add_list != "":

            self.add_list = self.add_list[:-1]
            self.editAreaTable2.delete("1.0", END)
            self.editAreaTable2.insert(tk.INSERT, self.add_list)
        elif choice == "del":
            pass
        elif choice == "Clear":
            """
            self.add_list = ""
            self.editAreaTable2.delete("1.0", END)
            """
            pass
        else:
            self.add_list += choice
            self.editAreaTable2.insert(tk.INSERT, choice)

    def add_reco_template(self,page):
        self.add_list = ''
        #self.editAreaTable2.delete("1.0", END)
        '''
        when button clicked
        '''

        '''
        if self.shop_id_choose == []:
            self.shop_id_choose.append(shop_id)
        else:
            self.shop_id_choose[0]=(shop_id)

        print(self.shop_id_choose[0])
        '''

        self.left_frame.pack_forget()

        section = "Add_pd"

        #self.btnbag.config(command=lambda: self.bag("2"))

        if section == "Add_pd":
            self.btnTR1.config(text='', background="gray20",
                               command='')

            self.btnTR2.config(text='', background="gray20",
                               command='')

            self.btnTR3.config(text='', background="gray20",
                               command='')

            self.btnTR4.config(text="", background="gray20",
                               command='')

            self.btnTR5.config(text="", background="gray20",
                               command='')

            self.btnTR6.config(text="", background="gray20",
                               command='')

            self.btnTR7.config(text='', background="gray20", command='')

            self.btnTR8.config(text='', background="gray20",
                               command='')


        self.btnHome.config(command=lambda: self.home_page("add_order"))
        self.btnBack.config(command=lambda: self.home_page("add_order"))

        self.left_frame = Frame(self.root, background="black",
                                borderwidth=5, relief="ridge",
                                width=600)
        self.left_frame.pack(side="left",
                             fill="both",
                             expand="yes",
                             )

        self.middle_frame = Frame(self.root, background="black",
                                  borderwidth=5, relief="ridge",
                                  )
        self.middle_frame.pack(side="left",
                               fill="both",

                               )

        self.frameL1 = tk.Frame(self.left_frame)
        self.frameL1.pack()
        self.frameL2 = tk.Frame(self.left_frame)
        self.frameL2.pack()
        self.frameL3 = tk.Frame(self.left_frame)
        self.frameL3.pack()
        self.frameL4 = tk.Frame(self.left_frame)
        self.frameL4.pack()
        self.frameL5 = tk.Frame(self.left_frame)
        self.frameL5.pack()
        self.frameL6 = tk.Frame(self.left_frame)
        self.frameL6.pack()
        self.frameL7 = tk.Frame(self.left_frame)
        self.frameL7.pack()
        self.frameL8 = tk.Frame(self.left_frame)
        self.frameL8.pack()
        self.frameL9 = tk.Frame(self.left_frame)
        self.frameL9.pack()
        self.frameL10 = tk.Frame(self.left_frame)
        self.frameL10.pack()
        self.frameL11 = tk.Frame(self.left_frame)
        self.frameL11.pack()


        if page == 'reco':
            self.lable_pd = tk.Label(self.frameL1, bg='black', text='Face Reconition Attendence Taking',
                                 font=("Helvetica", 20, "bold "), fg="white", borderwidth=5)
            self.lable_pd.pack()
        elif page == 'cap':
            self.lable_pd = tk.Label(self.frameL1, bg='black', text='Face Capture',
                                     font=("Helvetica", 20, "bold "), fg="white", borderwidth=5)
            self.lable_pd.pack()
        elif page == 'train':
            self.lable_pd = tk.Label(self.frameL1, bg='black', text='Face Trainning',
                                     font=("Helvetica", 20, "bold "), fg="white", borderwidth=5)
            self.lable_pd.pack()

        self.btn_pd = [[0 for x in range(45)] for y in range(1)]
        for i in range(0, 5):
            self.btn_pd[0][i] = tk.Button(self.frameL3, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                          bg="grey20", width=20, height=4, command='')
            self.btn_pd[0][i].pack(side=tk.LEFT)

        for i in range(5, 10):
            self.btn_pd[0][i] = tk.Button(self.frameL4, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                          bg="grey20", width=20,
                                          height=4, command='')
            self.btn_pd[0][i].pack(side=tk.LEFT)
        for i in range(10, 15):
            self.btn_pd[0][i] = tk.Button(self.frameL5, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                          bg="grey20", width=20,
                                          height=4, command='')
            self.btn_pd[0][i].pack(side=tk.LEFT)
        for i in range(15, 20):
            self.btn_pd[0][i] = tk.Button(self.frameL6, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                          bg="grey20", width=20,
                                          height=4, command='')
            self.btn_pd[0][i].pack(side=tk.LEFT)
        for i in range(20, 25):
            self.btn_pd[0][i] = tk.Button(self.frameL7, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                          bg="grey20", width=20,
                                          height=4, command='')
            self.btn_pd[0][i].pack(side=tk.LEFT)
        for i in range(25, 30):
            self.btn_pd[0][i] = tk.Button(self.frameL8, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                          bg="grey20", width=20,
                                          height=4, command='')
            self.btn_pd[0][i].pack(side=tk.LEFT)
        for i in range(30, 35):
            self.btn_pd[0][i] = tk.Button(self.frameL9, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                          bg="grey20", width=20,
                                          height=4, command='')
            self.btn_pd[0][i].pack(side=tk.LEFT)
        for i in range(35, 40):
            self.btn_pd[0][i] = tk.Button(self.frameL10, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                          bg="grey20", width=20,
                                          height=4, command='')
            self.btn_pd[0][i].pack(side=tk.LEFT)
        for i in range(40, 45):
            self.btn_pd[0][i] = tk.Button(self.frameL11, text=" ", font=("Helvetica", 10, "bold "), fg="white",
                                          bg="grey20", width=20,
                                          height=4, command='')
            self.btn_pd[0][i].pack(side=tk.LEFT)

            #self.btn_pd[0][0].config(text="Supreme\n$148", command=lambda: self.add_order_demo("supreme"))
            #self.btn_pd[0][1].config(text="Super Supreme\n$168", command=lambda: self.add_order_demo("super_supreme"))

        self.frameM1 = tk.Frame(self.middle_frame)
        self.frameM1.pack()

        if section == "Add_pd" or section == "Add_pd_p_t" or section == "Add_pd_check":
            tk.Label(self.frameM1, bg='black', text='',
                     font=("Helvetica", 20, "bold "), fg="white", borderwidth=5).pack()



        self.frameM1 = tk.Frame(self.middle_frame)
        self.frameM1.pack()
        self.frameM2 = tk.Frame(self.middle_frame)
        self.frameM2.pack()
        self.frameM3 = tk.Frame(self.middle_frame)
        self.frameM3.pack()
        self.frameM4 = tk.Frame(self.middle_frame)
        self.frameM4.pack()
        self.frameM5 = tk.Frame(self.middle_frame)
        self.frameM5.pack()
        self.frameM6 = tk.Frame(self.middle_frame)
        self.frameM6.pack()
        self.frameM7 = tk.Frame(self.middle_frame)
        self.frameM7.pack()
        self.frameM8 = tk.Frame(self.middle_frame)
        self.frameM8.pack()
        self.frameM9 = tk.Frame(self.middle_frame)
        self.frameM9.pack()

        self.editAreaTable = tkst.ScrolledText(self.frameM1, height=8, width=40, background="black", fg="white",
                                               font=("courier new", 15, "bold"))
        self.editAreaTable.pack(fill="both", expand="yes", side="left")

        self.editAreaTable.insert(tk.INSERT, "")

        self.editAreaTable2 = tkst.ScrolledText(self.frameM2, height=2, width=40, background="black", fg="white",
                                                font=("courier new", 15, "bold"))
        self.editAreaTable2.pack(fill="both", expand="yes", side="left")

        self.editAreaTable.insert(tk.INSERT, 'Input_student_id: ')

        tk.Button(self.frameM3, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM3, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM3, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM3, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=8,
                  height=2,command='').pack(
            side=tk.LEFT)

        tk.Button(self.frameM5, text="7", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.add_page_editarea("7")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="8", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.add_page_editarea("8")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="9", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.add_page_editarea("9")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="<[X]", font=("Helvetica", 20, "bold "), fg="white", bg="dark red", width=4,
                  height=2, command=lambda: self.add_page_editarea("del")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)

        tk.Button(self.frameM6, text="4", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.add_page_editarea("4")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="5", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.add_page_editarea("5")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="6", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.add_page_editarea("6")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)

        tk.Button(self.frameM7, text="1", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.add_page_editarea("1")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="2", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.add_page_editarea("2")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="3", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.add_page_editarea("3")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)

        tk.Button(self.frameM8, text="0", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.add_page_editarea("0")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command='').pack(
            side=tk.LEFT)
        if page == "reco" :
            tk.Button(self.frameM8, text="Enter", font=("Helvetica", 20, "bold "), fg="white", bg="dark green", width=8,
                      height=2, command=lambda:self.face_reco()).pack(
                side=tk.LEFT)
        elif page == "cap":
            tk.Button(self.frameM8, text="Enter", font=("Helvetica", 20, "bold "), fg="white", bg="dark green", width=8,
                      height=2, command=lambda: self.face_cap()).pack(
                side=tk.LEFT)
        elif page == "train":
            tk.Button(self.frameM8, text="Enter", font=("Helvetica", 20, "bold "), fg="white", bg="dark green", width=8,
                      height=2, command=lambda: self.face_train()).pack(
                side=tk.LEFT)

        if page == "Add_pd" or section == "Add_pd_p_t" or section == "Add_pd_check":
            #self.add_order_pizza(section)
            pass



    def face_reco(self):
        print('list'+str(self.add_list))

        first_name = []
        cur_fyp = self.conn_fyp.cursor()
        cur_fyp.execute(
            "select first_name from student where student_id = '" + str(self.add_list)+"'")
        for row in cur_fyp.fetchall():
            first_name.append(row)
        print(str(first_name[0])[16:-2])

        confirm_flag = vin3_face_recognition_test2.main(str(self.add_list),str(first_name[0])[16:-2],self.id)
        #print(confirm_flag)
        if confirm_flag == 'Success':
            #print('1')
            self.date_label.config(text=str(self.user_name[0])[1:-1]  + "  Timetable ID: " +str(self.id)+"  " +str(self.add_list)+str(first_name[0])[16:-2] + ":OK      " + str(
                self.date.strftime('%Y/%m/%d') + '      '))
            pass
        self.add_list=''
        self.editAreaTable2.delete("1.0", END)
        #self.home_page("add_order")
        pass

    def main_page(self, section, order_id, table_id):
        '''
        self.cur.close()
        self.db = pymysql.connect('localhost', 'root', '', 'ubereat')
        self.conn = pymysql.connect(user='root',
                                    password='',
                                    db='ubereat',
                                    cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.db.cursor()
        '''
        self.cur_fyp.close()
        self.db_fyp = pymysql.connect('localhost', 'root', '', 'fyp')
        self.conn_fyp = pymysql.connect(user='root',
                                        password='',
                                        db='fyp',
                                        cursorclass=pymysql.cursors.DictCursor)
        self.cur_fyp = self.db_fyp.cursor()

        # print(self.id)
        self.left_frame = Frame(self.root, background="black",
                                borderwidth=5, relief="ridge",
                                width=1000)
        self.left_frame.pack(side="left",
                             fill="both",
                             expand="yes",
                             )

        self.frameL1 = tk.Frame(self.left_frame)

        self.frameL1.pack()

        self.frameL2 = tk.Frame(self.left_frame)

        self.frameL2.pack()

        self.frameL3 = tk.Frame(self.left_frame)

        self.frameL3.pack()

        self.frameL4 = tk.Frame(self.left_frame)

        self.frameL4.pack()

        self.frameL5 = tk.Frame(self.left_frame)

        self.frameL5.pack()

        self.frameL6 = tk.Frame(self.left_frame)

        self.frameL6.pack()

        self.frameL7 = tk.Frame(self.left_frame)

        self.frameL7.pack()

        self.frameL8 = tk.Frame(self.left_frame)

        self.frameL8.pack()

        self.frameL9 = tk.Frame(self.left_frame)

        self.frameL9.pack()

        self.frameL10 = tk.Frame(self.left_frame)

        self.frameL10.pack()

        self.frameTablelabel = tk.Frame(self.left_frame)
        self.frameTablelabel.pack()

        if section == 1:
            tk.Label(self.frameL1, bg='black', text='Feature list',
                     font=("Helvetica", 20, "bold "), fg="white", borderwidth=5).pack()

        elif section == 2:
            tk.Label(self.frameL1, bg='black', text='Switch table',
                     font=("Helvetica", 20, "bold "), fg="white", borderwidth=5).pack()

        self.btn_tb = [[0 for x in range(100)] for y in range(1)]
        for i in range(0, 5):
            self.btn_tb[0][i] = tk.Button(self.frameL3, text='', font=("Helvetica", 10, "bold "), background="grey20",
                                          fg='white', width=30, height=6,
                                          command='')
            self.btn_tb[0][i].pack(side=tk.LEFT)

        for i in range(6, 11):
            self.btn_tb[0][i] = tk.Button(self.frameL4, text='', font=("Helvetica", 10, "bold "), background="grey20",
                                          fg='white', width=30, height=6,
                                          command='')
            self.btn_tb[0][i].pack(side=tk.LEFT)
        for i in range(11, 16):
            self.btn_tb[0][i] = tk.Button(self.frameL5, text='', font=("Helvetica", 10, "bold "), background="grey20",
                                          fg='white', width=30, height=6,
                                          command='')
            self.btn_tb[0][i].pack(side=tk.LEFT)
        for i in range(16, 21):
            self.btn_tb[0][i] = tk.Button(self.frameL6, text='', font=("Helvetica", 10, "bold "), background="grey20",
                                          fg='white', width=30, height=6,
                                          command='')
            self.btn_tb[0][i].pack(side=tk.LEFT)
        for i in range(21, 26):
            self.btn_tb[0][i] = tk.Button(self.frameL7, text='', font=("Helvetica", 10, "bold "), background="grey20",
                                          fg='white', width=30, height=6,
                                          command='')
            self.btn_tb[0][i].pack(side=tk.LEFT)
        for i in range(26, 31):
            self.btn_tb[0][i] = tk.Button(self.frameL8, text='', font=("Helvetica", 10, "bold "), background="grey20",
                                          fg='white', width=30, height=6,
                                          command='')
            self.btn_tb[0][i].pack(side=tk.LEFT)

        self.btn_tb[0][0].config(text="Face Capture", command=lambda: self.add_reco_template('cap'))
        self.btn_tb[0][1].config(text="Face Trainning", command=lambda: self.add_reco_template('train'))

        self.btnTR1.config(text='My Order', font=("Helvetica", 20, "bold "), bg='forest green',
                           command=lambda: self.my_order())

        self.btnTR2.config(text='My Account', font=("Helvetica", 20, "bold "), bg='forest green',
                           command=lambda: self.my_account())

        self.btnTR3.config(text='My Address', font=("Helvetica", 20, "bold "), bg='forest green',
                           command=lambda: self.my_address())

        self.btnTR4.config(text='My Payment', font=("Helvetica", 20, "bold "), bg='forest green',
                           command=lambda: self.my_payment())

        self.btnTR5.config(text='', background="grey20", font=("Helvetica", 20, "bold "), command='')

        self.btnTR6.config(text='', background="grey20", command= self.add_reco_template('reco'))

        self.btnTR7.config(text='', background="grey20", command='')

        self.btnTR8.config(text='', bg='grey20', command='')

        self.btnBack.config(command='')
        self.btnHome.config(command='')

        self.btnbag.config(command=lambda: self.bag("1"))
        self.btnrefresh.config(command=lambda: self.test_reply())

        #if section == 1:
            #pass
            #self.main_page_table()

        #elif section == 2:
            #self.switch_table(order_id, table_id)



    def __init__(self, root, id):
        self.root = root
        self.root.geometry('1920x1080')
        self.root.title("Reco+")

        '''
        self.db = pymysql.connect('localhost', 'root', '', 'ubereat')
        self.conn = pymysql.connect(user='root',
                                    password='',
                                    db='ubereat',
                                    cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.db.cursor()
        '''
        self.db_fyp = pymysql.connect('localhost', 'root', '', 'fyp')
        self.conn_fyp = pymysql.connect(user='root',
                                    password='',
                                    db='fyp',
                                    cursorclass=pymysql.cursors.DictCursor)
        self.cur_fyp = self.db_fyp.cursor()

        self.frameRt = tk.Frame(self.root, background="black")
        self.frameRt.pack(fill="both")

        self.id = str(id)
        print(self.id)
        self.user_name = []
        cur_fyp = self.conn_fyp.cursor()
        cur_fyp.execute("select course.course_name from course inner join course_timetable on course_timetable.course_id = course.course_id where course_timetable.time_table_id ='" + str(self.id) + "'")
        for row in cur_fyp.fetchall():
            self.user_name.append(row)



        #print(str(self.user_name[0]))
        self.date = datetime.datetime.now()
        self.date_label = tk.Label(self.frameRt, text=str(self.user_name[0])[1:-1] + "      Timetable ID: " +str(self.id)+" "+ str(
            self.date.strftime('%Y/%m/%d') + '      '), font=("courier new", 20, "bold"), bg='black', fg="white")
        self.date_label.pack(side=tk.LEFT)

        self.clock1 = clock.Clock(self.frameRt)
        self.clock1.pack(side=tk.LEFT)
        self.clock1.configure(font=("courier new", 20, "bold"), bg='black', fg="white")

        self.btnbag = tk.Button(self.frameRt, text='Log Out', font=("Helvetica", 10, "bold "), width=20,
                                height=1, bg="black", fg="white", command=lambda: self.bag("1"))
        self.btnbag.pack(side=tk.LEFT)

        self.btnrefresh = tk.Button(self.frameRt, text='REFRESH', font=("Helvetica", 10, "bold "), width=20,
                                    height=1, bg="black", fg="white", command=lambda: self.bag("1"))
        self.btnrefresh.pack(side=tk.LEFT)

        self.bottom_nvaigation = Frame(self.root, background="black", borderwidth=5,
                                       relief="ridge", height=35)
        self.bottom_nvaigation.pack(side="bottom", fill="both",
                                    )

        self.right_frame = Frame(self.root, background="black",
                                 borderwidth=5, relief="ridge")
        self.right_frame.pack(side="right", fill="both",
                              )

        self.frame_bottom_nvaigation = tk.Frame(self.bottom_nvaigation)
        self.frame_bottom_nvaigation.pack()

        self.btnBack = tk.Button(self.frame_bottom_nvaigation, text='', font=("Helvetica", 10, "bold "), width=88,
                                 height=1, bg="black", fg="white")
        self.btnBack.pack(side=tk.LEFT)

        self.btnHome = tk.Button(self.frame_bottom_nvaigation, text='', font=("Helvetica", 10, "bold "), width=88,
                                 height=1, bg="black", fg="white", command=lambda: self.home_page())
        self.btnHome.pack(side=tk.LEFT)

        self.frameR1 = tk.Frame(self.right_frame)

        self.frameR1.pack()

        self.frameR2 = tk.Frame(self.right_frame)

        self.frameR2.pack()

        self.frameR3 = tk.Frame(self.right_frame)

        self.frameR3.pack()

        self.frameR4 = tk.Frame(self.right_frame)

        self.frameR4.pack()

        self.frameR5 = tk.Frame(self.right_frame)

        self.frameR5.pack()

        self.frameR6 = tk.Frame(self.right_frame)

        self.frameR6.pack()

        self.frameR7 = tk.Frame(self.right_frame)

        self.frameR7.pack()

        self.frameR8 = tk.Frame(self.right_frame)

        self.frameR8.pack()

        self.btnTR1 = tk.Button(self.frameR1, text='', font=("Helvetica", 20, "bold "), background="grey20", fg='white',
                                width=10, height=2)
        self.btnTR1.pack(side=tk.LEFT)
        self.btnTR2 = tk.Button(self.frameR2, text='', font=("Helvetica", 20, "bold "), background="grey20", fg='white',
                                width=10, height=2)
        self.btnTR2.pack(side=tk.LEFT)
        self.btnTR3 = tk.Button(self.frameR3, text='', font=("Helvetica", 20, "bold "), background="grey20", fg='white',
                                width=10, height=2)
        self.btnTR3.pack(side=tk.LEFT)
        self.btnTR4 = tk.Button(self.frameR4, text='', font=("Helvetica", 20, "bold "), background="grey20", fg='white',
                                width=10, height=2)
        self.btnTR4.pack(side=tk.LEFT)
        self.btnTR5 = tk.Button(self.frameR5, text='', font=("Helvetica", 20, "bold "), background="grey20", fg='white',
                                width=10, height=2)
        self.btnTR5.pack(side=tk.LEFT)
        self.btnTR6 = tk.Button(self.frameR6, text='', font=("Helvetica", 20, "bold "), background="grey20", fg='white',
                                width=10, height=2)
        self.btnTR6.pack(side=tk.LEFT)
        self.btnTR7 = tk.Button(self.frameR7, text='', font=("Helvetica", 20, "bold "), background="grey20", fg='white',
                                width=10, height=2)
        self.btnTR7.pack(side=tk.LEFT)
        self.btnTR8 = tk.Button(self.frameR8, text='', font=("Helvetica", 20, "bold "), background="grey20", fg='white',
                                width=10, height=2)
        self.btnTR8.pack(side=tk.LEFT)

        self.table_id_nm = ""
        self.add_list = ""
        self.del_list = ''
        self.address_list = ""
        self.delivery_list = []

        self.add_no_list = []
        self.add_id_list = []
        self.add_pd_list = []
        self.add_qty_list = []
        self.add_price_list = []
        self.add_link_list = []

        self.add_link_price_list = []
        self.set_option_count = 0
        self.creator_option_count = 0
        self.add_pd_location = ''
        self.table_people_no = ''
        self.member_id = ''
        self.update_order_id = []

        self.shop_id_choose=[]

        self.user_payment = []


        # print(self.user_address)


        self.main_page(1, [], '')


def main(id, window):
    root = tk.Tk()
    Gui(root, id)
    window.destroy()
    root.mainloop()


if __name__ == '__main__':
    sys.exit(main())

