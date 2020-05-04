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
import vin3_Login_loop
import vin3_Login_student_loop
import clock
import json
import pymysql
import requests
import os

import vin3_face_recognition_test2
import vin3_cap_face
import vin3_face_trainning_deep

class Gui:
    def last_page(self, page):

        if page == "table_sub":
            self.left_frame.pack_forget()
            self.main_page(self.section, [], '')
            self.table_id_nm = ""

        elif page == "address_page":
            self.left_frame.pack_forget()
            self.address_list = []
            self.main_page(self.section, [], '')

        elif page == "check_order":
            self.left_frame.pack_forget()
            self.middle_frame.pack_forget()
            self.main_page(self.section, [], '')
        else:
            self.address_list = ''
            # self.add_pd_list = []
            # self.add_qty_list = []
            # self.add_link_list=[]
            self.add_link_price_list = []
            self.table_id_nm = ""
            self.delivery_list = []

    def last_page_tb(self, page, table_no):
        if page == "set_tb":
            self.left_frame.pack_forget()

            # self.add_pd_list = []
            # self.add_qty_list = []
            # self.add_link_list = []
            self.add_link_price_list = []
            self.table_sub(self.table_id_nm, table_no)



        else:
            self.left_frame.pack_forget()
            self.middle_frame.pack_forget()
            # self.add_pd_list = []
            # self.add_qty_list = []
            # self.add_link_list = []
            self.add_link_price_list = []
            self.address_list = ''
            self.table_sub(self.table_id_nm, table_no)
            self.delivery_list = []

    def last_page_switch(self, table_id, number):
        self.left_frame.pack_forget()

        # self.add_pd_list = []
        # self.add_qty_list = []
        # self.add_link_list = []
        self.add_link_price_list = []
        print(table_id)
        print(number)
        self.table_sub(table_id, int(number))

    def home_page(self, page):

        if page == "add_order":
            self.left_frame.pack_forget()
            self.middle_frame.pack_forget()
            # self.add_pd_list = []
            # self.add_qty_list = []
            # self.add_link_list = []
            self.add_link_price_list = []
            self.table_id_nm = ""
            self.main_page(self.section, [], '')



        elif page == "check_order":
            self.left_frame.pack_forget()
            self.middle_frame.pack_forget()
            self.main_page(self.section, [], '')


        elif page == "del_order":
            self.left_frame.pack_forget()
            self.middle_frame.pack_forget()
            # self.add_pd_list = []
            # self.add_qty_list = []
            # self.add_link_list = []
            self.add_link_price_list = []
            self.table_id_nm = ""
            self.main_page(self.section, [], '')
            self.delivery_list = []
            self.address_list = ''

        else:
            self.left_frame.pack_forget()
            # self.add_pd_list = []
            # self.add_qty_list = []
            # self.add_link_list = []
            self.add_link_price_list = []
            self.table_id_nm = ""
            self.main_page(self.section, [], '')
            self.delivery_list = []
            self.address_list = ''


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



    def del_page_editarea(self, choice):
        if choice == "del":
            self.del_list = self.del_list[:-1]
            self.editAreaTable3.delete("1.0", END)
            self.editAreaTable3.insert(tk.INSERT, self.del_list)

        elif choice == "Clear":
            pass
        else:
            self.del_list += choice
            self.editAreaTable3.insert(tk.INSERT, choice)
            self.editAreaTable3.see("end")


    def staff_search_id(self):

        option_list = self.del_list
        self.del_list = ''
        self.editAreaTable3.delete("1.0", END)

        first_name = []
        last_name = []
        sex = []
        date_of_birth = []
        student_id = []
        position = []

        cur = self.conn_fyp.cursor()
        cur.execute("select first_name from staff where staff_id = '"+str(option_list)+"'")

        for row in cur.fetchall():
            first_name.append(row)
        # print(str(first_name[0])[16:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select last_name from staff where staff_id = '"+str(option_list)+"'")

        for row in cur.fetchall():
            last_name.append(row)
        # print(str(last_name[0])[15:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select sex from staff where staff_id = '"+str(option_list)+"'")

        for row in cur.fetchall():
            sex.append(row)
        # print(str(sex[0])[9:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select date_of_birth from staff where staff_id = '"+str(option_list)+"'")

        for row in cur.fetchall():
            date_of_birth.append(row)
        # print(str(date_of_birth[0])[19:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select staff_id from staff where staff_id = '"+str(option_list)+"'")

        for row in cur.fetchall():
            student_id.append(row)
        # print(str(student_id[0])[15:-1])

        cur = self.conn_fyp.cursor()
        cur.execute("select position from staff where staff_id = '"+str(option_list)+"'")

        for row in cur.fetchall():
            position.append(row)
        # print(str(face_cap[0])[14:-2])

        cur = self.conn_fyp.cursor()



        self.editAreaTable.delete("1.0", END)
        x = 0
        while x < len(student_id):
            self.editAreaTable.insert(tk.INSERT, 'Staff id: ' + str(student_id[x])[11:-1] + '\n')
            self.editAreaTable.insert(tk.INSERT,
                                      'Name: ' + str(first_name[x])[16:-2] + ' ' + str(last_name[x])[15:-2] + '\n')
            self.editAreaTable.insert(tk.INSERT, 'Sex: ' + str(sex[x])[9:-2] + '\n')
            self.editAreaTable.insert(tk.INSERT, 'Date of birth: ' + str(date_of_birth[x])[19:-2] + '\n')
            self.editAreaTable.insert(tk.INSERT, 'Position: ' + str(position[x])[13:-2] + '\n')

            self.editAreaTable.insert(tk.INSERT, '\n')
            self.editAreaTable.insert(tk.INSERT, '\n')
            self.editAreaTable.insert(tk.INSERT, '\n')

            x += 1

        pass

    def staff_order_last_name(self):
        self.editAreaTable.delete("1.0", END)
        first_name = []
        last_name = []
        sex = []
        date_of_birth = []
        student_id = []
        position = []


        cur = self.conn_fyp.cursor()
        cur.execute("select first_name from staff order by last_name")

        for row in cur.fetchall():
            first_name.append(row)
        # print(str(first_name[0])[16:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select last_name from staff order by last_name")

        for row in cur.fetchall():
            last_name.append(row)
        # print(str(last_name[0])[15:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select sex from staff order by last_name")

        for row in cur.fetchall():
            sex.append(row)
        # print(str(sex[0])[9:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select date_of_birth from staff order by last_name")

        for row in cur.fetchall():
            date_of_birth.append(row)
        # print(str(date_of_birth[0])[19:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select staff_id from staff order by last_name")

        for row in cur.fetchall():
            student_id.append(row)
        # print(str(student_id[0])[15:-1])

        cur = self.conn_fyp.cursor()
        cur.execute("select position from staff order by last_name")

        for row in cur.fetchall():
            position.append(row)
        # print(str(face_cap[0])[14:-2])






        x = 0
        while x < len(student_id):
            self.editAreaTable.insert(tk.INSERT, 'Student id: ' + str(student_id[x])[13:-1] + '\n')
            self.editAreaTable.insert(tk.INSERT,
                                      'Name: ' + str(first_name[x])[16:-2] + ' ' + str(last_name[x])[15:-2] + '\n')
            self.editAreaTable.insert(tk.INSERT, 'Sex: ' + str(sex[x])[9:-2] + '\n')
            self.editAreaTable.insert(tk.INSERT, 'Date of birth: ' + str(date_of_birth[x])[19:-2] + '\n')
            self.editAreaTable.insert(tk.INSERT, 'Position: ' + str(position[x])[11:-2] + '\n')


            self.editAreaTable.insert(tk.INSERT, '\n')
            self.editAreaTable.insert(tk.INSERT, '\n')
            self.editAreaTable.insert(tk.INSERT, '\n')

            x += 1
        pass

    def staff_list_all(self):
        self.editAreaTable.delete("1.0", END)
        first_name = []
        last_name = []
        sex = []
        date_of_birth = []
        student_id = []
        position = []


        cur = self.conn_fyp.cursor()
        cur.execute("select first_name from staff")

        for row in cur.fetchall():
            first_name.append(row)
        # print(str(first_name[0])[16:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select last_name from staff")

        for row in cur.fetchall():
            last_name.append(row)
        # print(str(last_name[0])[15:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select sex from staff")

        for row in cur.fetchall():
            sex.append(row)
        # print(str(sex[0])[9:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select date_of_birth from staff")

        for row in cur.fetchall():
            date_of_birth.append(row)
        # print(str(date_of_birth[0])[19:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select staff_id from staff")

        for row in cur.fetchall():
            student_id.append(row)
        print(str(student_id[0])[13:-1])

        cur = self.conn_fyp.cursor()
        cur.execute("select position from staff")

        for row in cur.fetchall():
            position.append(row)
        print(str(position[0])[11:-2])






        x = 0
        while x < len(student_id):
            self.editAreaTable.insert(tk.INSERT, 'Student id: ' + str(student_id[x])[13:-1] + '\n')
            self.editAreaTable.insert(tk.INSERT,
                                      'Name: ' + str(first_name[x])[16:-2] + ' ' + str(last_name[x])[15:-2] + '\n')
            self.editAreaTable.insert(tk.INSERT, 'Sex: ' + str(sex[x])[9:-2] + '\n')
            self.editAreaTable.insert(tk.INSERT, 'Date of birth: ' + str(date_of_birth[x])[19:-2] + '\n')
            self.editAreaTable.insert(tk.INSERT, 'Position: ' + str(position[x])[14:-2] + '\n')
            #self.editAreaTable.insert(tk.INSERT, 'Face trainning: ' + str(face_train[x])[16:-2] + '\n')

            self.editAreaTable.insert(tk.INSERT, '\n')
            self.editAreaTable.insert(tk.INSERT, '\n')
            self.editAreaTable.insert(tk.INSERT, '\n')

            x += 1
        pass

    def staff_list(self):
        self.del_list=''

        self.left_frame.pack_forget()
        self.left_frame = Frame(self.root, background="black",
                                borderwidth=5, relief="ridge",
                                width=600)
        self.left_frame.pack(side="left",
                             fill="both",
                             expand="yes",
                             )



        self.middle_frame = Frame(self.root, width=20, background="black",
                                  borderwidth=5, relief="ridge",
                                  )
        self.middle_frame.pack(side="left",
                               fill="both",

                               )

        tk.Label(self.left_frame, bg='black', text='Staff list',
                 font=("Helvetica", 20, "bold "), fg="white", borderwidth=5).pack()

        self.editAreaTable = tkst.ScrolledText(self.left_frame, height=8, width=69, background="black", fg="white",
                                               font=("Helvetica", 15, "bold"))
        self.editAreaTable.pack(fill="both", expand="yes", side="left")
        '''
        self.editAreaTable.insert(tk.INSERT,
                                  "Order id: O001\n\nOrder time: 2/2/2020 11:11:11\n\nSuper Supreme x1 $168\nDelivery fee: $20\nTotal $188\n\nDelivery Location: Flat B, 23/F, Block 66, XYZ Garden, 8 Testing Road, HK\nPayment: Cash\nDelivery time: 30 min\n\n\n")
        self.editAreaTable.insert(tk.INSERT,
                                  "Order id: O124\n\nOrder time: 1/2/2020 11:11:11\n\nSupreme x2 $296\nDelivery fee: $20\nTotal $316\n\nDelivery Location: Flat B, 23/F, Block 66, XYZ Garden, 8 Testing Road, HK\nPayment: Cash\nDelivery time:1/2/2020 11:33:11")
        '''

        self.btnTR1.config(text='Order by\nLast Name', font=("Helvetica", 20, "bold "), bg="grey20",
                           command=lambda:self.staff_order_last_name())
        self.btnTR2.config(text='List All', font=("Helvetica", 20, "bold "), bg="grey20",command=lambda:self.staff_list_all())
        self.btnTR3.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR4.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR5.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR6.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR7.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR8.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")

        self.btnBack.config(command=lambda: self.home_page("add_order"))
        self.btnHome.config(command=lambda: self.home_page("add_order"))

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

        self.editAreaTable2 = tkst.ScrolledText(self.frameM1, height=10, width=40, background="black", fg="white",
                                                font=("Helvetica", 15, "bold"))
        self.editAreaTable2.pack(fill="both", expand="yes", side="left")

        self.editAreaTable3 = tkst.ScrolledText(self.frameM2, height=2, width=40, background="black", fg="white",
                                                font=("Helvetica", 15, "bold"))
        self.editAreaTable3.pack(fill="both", expand="yes", side="left")

        tk.Button(self.frameM5, text="7", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("7")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="8", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("8")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="9", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("9")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="<[X]", font=("Helvetica", 20, "bold "), fg="white", bg="dark red", width=4,
                  height=2, command=lambda: self.del_page_editarea("del")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)

        tk.Button(self.frameM6, text="4", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("4")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="5", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("5")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="6", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("6")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)

        tk.Button(self.frameM7, text="1", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("1")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="2", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("2")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="3", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("3")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="0", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("0")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="Search", font=("Helvetica", 20, "bold "), fg="white", bg="dark green",
                  width=8, height=2, command=lambda:self.staff_search_id()).pack(
            side=tk.LEFT)


        self.editAreaTable2.insert(tk.INSERT, 'Input Staff id to Search: ')



        self.staff_list_all()


        pass



    def staff_modify_update(self):
        cur = self.conn_fyp.cursor()
        cur.execute("update staff set `first_name` = '"+str(self.create_input1.get())+ "' where staff_id = '" + str( self.option_list) + "'")
        cur.execute("commit")

        cur = self.conn_fyp.cursor()
        cur.execute("update staff set `last_name` = '" + str(self.create_input2.get()) + "' where staff_id = '" + str( self.option_list) + "'")
        cur.execute("commit")

        cur = self.conn_fyp.cursor()
        cur.execute("update staff set `sex` = '" + str(self.create_input3.get()) + "' where staff_id = '" + str( self.option_list) + "'")
        cur.execute("commit")

        cur = self.conn_fyp.cursor()
        cur.execute("update staff set `date_of_birth` = '" + str(self.create_input4.get()) + "' where staff_id = '" + str( self.option_list) + "'")
        cur.execute("commit")

        cur = self.conn_fyp.cursor()
        cur.execute("update staff set `position` = '" + str(self.create_input5.get()) + "' where staff_id = '" + str( self.option_list) + "'")
        cur.execute("commit")

        cur.close()
        self.db_fyp = pymysql.connect('localhost', 'root', '', 'fyp')
        self.conn_fyp = pymysql.connect(user='root',
                                    password='',
                                    db='fyp',
                                    cursorclass=pymysql.cursors.DictCursor)
        cur = self.db_fyp.cursor()



        self.date_label.config(text=str(self.user_name[0])[15:-2] + "      " + str(self.create_input2.get()) + ":Has Been updated      " + str(
            self.date.strftime('%Y/%m/%d') + '      '))
        self.create_input1.delete(0, 'end')
        self.create_input2.delete(0, 'end')
        self.create_input3.delete(0, 'end')
        self.create_input4.delete(0, 'end')
        self.create_input5.delete(0, 'end')
        pass

    def staff_modify_search(self):
        self.option_list = self.del_list
        self.del_list = ''
        self.editAreaTable3.delete("1.0", END)

        first_name = []
        last_name = []
        sex = []
        date_of_birth = []
        student_id = []
        position = []

        cur = self.conn_fyp.cursor()
        cur.execute("select first_name from staff where staff_id = '" + str( self.option_list) + "'")

        for row in cur.fetchall():
            first_name.append(row)
        # print(str(first_name[0])[16:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select last_name from staff where staff_id = '" + str( self.option_list) + "'")

        for row in cur.fetchall():
            last_name.append(row)
        # print(str(last_name[0])[15:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select sex from staff where staff_id = '" + str( self.option_list) + "'")

        for row in cur.fetchall():
            sex.append(row)
        # print(str(sex[0])[9:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select date_of_birth from staff where staff_id = '" + str( self.option_list) + "'")

        for row in cur.fetchall():
            date_of_birth.append(row)
        # print(str(date_of_birth[0])[19:-2])



        cur = self.conn_fyp.cursor()
        cur.execute("select position from staff where staff_id = '" + str( self.option_list) + "'")

        for row in cur.fetchall():
            position.append(row)
        # print(str(position[0])[14:-2])

        self.create_input1.delete(0, 'end')
        self.create_input2.delete(0, 'end')
        self.create_input3.delete(0, 'end')
        self.create_input4.delete(0, 'end')
        self.create_input5.delete(0, 'end')


        self.create_input1.insert(END, str(first_name[0])[16:-2])
        self.create_input2.insert(END, str(last_name[0])[15:-2])
        self.create_input3.insert(END, str(sex[0])[9:-2])
        self.create_input4.insert(END, str(date_of_birth[0])[19:-2])
        self.create_input5.insert(END, str(position[0])[14:-2])



        pass

    def staff_modify(self):
        self.del_list=''
        self.left_frame.pack_forget()
        self.left_frame = Frame(self.root, background="black",
                                borderwidth=5, relief="ridge",
                                width=600)
        self.left_frame.pack(side="left",
                             fill="both",
                             expand="yes",
                             )

        self.middle_frame = Frame(self.root, width=20, background="black",
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

        self.create_title1 = tk.Label(self.frameL1, text="Staff Modify", font=("Helvetica", 30),
                                      fg="white",
                                      background="black")
        self.create_title1.pack(side=tk.LEFT)

        self.create_title2 = tk.Label(self.frameL3, text="Please update the followings", font=("Helvetica", 10),
                                      fg="white",
                                      background="black")
        self.create_title2.pack(side=tk.LEFT)

        self.create_label1 = tk.Label(self.frameL4, text="First Name: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label1.pack(side=tk.LEFT)

        self.create_input1 = tk.Entry(self.frameL4, text="", background="white", width=80)
        self.create_input1.pack(side=tk.LEFT)

        self.create_label2 = tk.Label(self.frameL5, text="Last Name: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label2.pack(side=tk.LEFT)

        self.create_input2 = tk.Entry(self.frameL5, text="", background="white", width=80)
        self.create_input2.pack(side=tk.LEFT)

        self.create_label3 = tk.Label(self.frameL6, text="Sex (M/F): ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label3.pack(side=tk.LEFT)

        self.create_input3 = tk.Entry(self.frameL6, text="", background="white", width=80)
        self.create_input3.pack(side=tk.LEFT)

        self.create_label4 = tk.Label(self.frameL7, text="Date of Birth: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label4.pack(side=tk.LEFT)

        self.create_input4 = tk.Entry(self.frameL7, text="", background="white", width=80)
        self.create_input4.pack(side=tk.LEFT)

        self.create_label5 = tk.Label(self.frameL8, text="Position: ", font=("Helvetica", 20),
                                      fg="white",
                                      background="black")
        self.create_label5.pack(side=tk.LEFT)

        self.create_input5 = tk.Entry(self.frameL8, text="", background="white", width=80)
        self.create_input5.pack(side=tk.LEFT)


        self.create_submit = tk.Button(self.frameL9, text='Submit', font=("Helvetica", 20, "bold "), fg="white",
                                       bg="dark green",
                                       width=12, height=2, command=lambda: self.staff_modify_update())
        self.create_submit.pack(side=tk.LEFT)

        self.btnTR1.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR2.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR3.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR4.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR5.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR6.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR7.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR8.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")

        self.btnBack.config(command=lambda: self.home_page("add_order"))
        self.btnHome.config(command=lambda: self.home_page("add_order"))

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

        self.editAreaTable2 = tkst.ScrolledText(self.frameM1, height=10, width=40, background="black", fg="white",
                                                font=("Helvetica", 15, "bold"))
        self.editAreaTable2.pack(fill="both", expand="yes", side="left")

        self.editAreaTable3 = tkst.ScrolledText(self.frameM2, height=2, width=40, background="black", fg="white",
                                                font=("Helvetica", 15, "bold"))
        self.editAreaTable3.pack(fill="both", expand="yes", side="left")

        tk.Button(self.frameM5, text="7", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("7")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="8", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("8")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="9", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("9")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="<[X]", font=("Helvetica", 20, "bold "), fg="white", bg="dark red", width=4,
                  height=2, command=lambda: self.del_page_editarea("del")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)

        tk.Button(self.frameM6, text="4", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("4")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="5", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("5")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="6", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("6")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)

        tk.Button(self.frameM7, text="1", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("1")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="2", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("2")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="3", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("3")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="0", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("0")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="Search", font=("Helvetica", 20, "bold "), fg="white", bg="dark green",
                  width=8, height=2, command=lambda: self.staff_modify_search()).pack(
            side=tk.LEFT)

        self.editAreaTable2.insert(tk.INSERT, 'Input Staff id to Search: ')

        #self.staff_list_all()

        pass
        pass



    def student_modify_update(self):
        cur = self.conn_fyp.cursor()
        cur.execute("update student set `first_name` = '"+str(self.create_input1.get())+ "' where student_id = '" + str( self.option_list) + "'")
        cur.execute("commit")

        cur = self.conn_fyp.cursor()
        cur.execute("update student set `last_name` = '" + str(self.create_input2.get()) + "' where student_id = '" + str( self.option_list) + "'")
        cur.execute("commit")

        cur = self.conn_fyp.cursor()
        cur.execute("update student set `sex` = '" + str(self.create_input3.get()) + "' where student_id = '" + str( self.option_list) + "'")
        cur.execute("commit")

        cur = self.conn_fyp.cursor()
        cur.execute("update student set `date_of_birth` = '" + str(self.create_input4.get()) + "' where student_id = '" + str( self.option_list) + "'")
        cur.execute("commit")



        cur.close()
        self.db_fyp = pymysql.connect('localhost', 'root', '', 'fyp')
        self.conn_fyp = pymysql.connect(user='root',
                                    password='',
                                    db='fyp',
                                    cursorclass=pymysql.cursors.DictCursor)
        cur = self.db_fyp.cursor()



        self.date_label.config(text=str(self.user_name[0])[15:-2] + "      " + str(self.create_input2.get()) + ":Has Been updated      " + str(
            self.date.strftime('%Y/%m/%d') + '      '))
        self.create_input1.delete(0, 'end')
        self.create_input2.delete(0, 'end')
        self.create_input3.delete(0, 'end')
        self.create_input4.delete(0, 'end')

        pass

    def student_modify_search(self):
        self.option_list = self.del_list
        self.del_list = ''
        self.editAreaTable3.delete("1.0", END)

        first_name = []
        last_name = []
        sex = []
        date_of_birth = []
        student_id = []
        position = []

        cur = self.conn_fyp.cursor()
        cur.execute("select first_name from student where student_id = '" + str( self.option_list) + "'")

        for row in cur.fetchall():
            first_name.append(row)
        # print(str(first_name[0])[16:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select last_name from student where student_id = '" + str( self.option_list) + "'")

        for row in cur.fetchall():
            last_name.append(row)
        # print(str(last_name[0])[15:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select sex from student where student_id = '" + str( self.option_list) + "'")

        for row in cur.fetchall():
            sex.append(row)
        # print(str(sex[0])[9:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select date_of_birth from student where student_id = '" + str( self.option_list) + "'")

        for row in cur.fetchall():
            date_of_birth.append(row)
        # print(str(date_of_birth[0])[19:-2])





        self.create_input1.delete(0, 'end')
        self.create_input2.delete(0, 'end')
        self.create_input3.delete(0, 'end')
        self.create_input4.delete(0, 'end')



        self.create_input1.insert(END, str(first_name[0])[16:-2])
        self.create_input2.insert(END, str(last_name[0])[15:-2])
        self.create_input3.insert(END, str(sex[0])[9:-2])
        self.create_input4.insert(END, str(date_of_birth[0])[19:-2])




        pass

    def student_modify(self):
        self.del_list=''
        self.left_frame.pack_forget()
        self.left_frame = Frame(self.root, background="black",
                                borderwidth=5, relief="ridge",
                                width=600)
        self.left_frame.pack(side="left",
                             fill="both",
                             expand="yes",
                             )

        self.middle_frame = Frame(self.root, width=20, background="black",
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

        self.create_title1 = tk.Label(self.frameL1, text="Student Modify", font=("Helvetica", 30),
                                      fg="white",
                                      background="black")
        self.create_title1.pack(side=tk.LEFT)

        self.create_title2 = tk.Label(self.frameL3, text="Please update the followings", font=("Helvetica", 10),
                                      fg="white",
                                      background="black")
        self.create_title2.pack(side=tk.LEFT)

        self.create_label1 = tk.Label(self.frameL4, text="First Name: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label1.pack(side=tk.LEFT)

        self.create_input1 = tk.Entry(self.frameL4, text="", background="white", width=80)
        self.create_input1.pack(side=tk.LEFT)

        self.create_label2 = tk.Label(self.frameL5, text="Last Name: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label2.pack(side=tk.LEFT)

        self.create_input2 = tk.Entry(self.frameL5, text="", background="white", width=80)
        self.create_input2.pack(side=tk.LEFT)

        self.create_label3 = tk.Label(self.frameL6, text="Sex (M/F): ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label3.pack(side=tk.LEFT)

        self.create_input3 = tk.Entry(self.frameL6, text="", background="white", width=80)
        self.create_input3.pack(side=tk.LEFT)

        self.create_label4 = tk.Label(self.frameL7, text="Date of Birth: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label4.pack(side=tk.LEFT)

        self.create_input4 = tk.Entry(self.frameL7, text="", background="white", width=80)
        self.create_input4.pack(side=tk.LEFT)




        self.create_submit = tk.Button(self.frameL8, text='Submit', font=("Helvetica", 20, "bold "), fg="white",
                                       bg="dark green",
                                       width=12, height=2, command=lambda: self.student_modify_update())
        self.create_submit.pack(side=tk.LEFT)

        self.btnTR1.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR2.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR3.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR4.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR5.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR6.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR7.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR8.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")

        self.btnBack.config(command=lambda: self.home_page("add_order"))
        self.btnHome.config(command=lambda: self.home_page("add_order"))

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

        self.editAreaTable2 = tkst.ScrolledText(self.frameM1, height=10, width=40, background="black", fg="white",
                                                font=("Helvetica", 15, "bold"))
        self.editAreaTable2.pack(fill="both", expand="yes", side="left")

        self.editAreaTable3 = tkst.ScrolledText(self.frameM2, height=2, width=40, background="black", fg="white",
                                                font=("Helvetica", 15, "bold"))
        self.editAreaTable3.pack(fill="both", expand="yes", side="left")

        tk.Button(self.frameM5, text="7", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("7")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="8", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("8")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="9", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("9")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="<[X]", font=("Helvetica", 20, "bold "), fg="white", bg="dark red", width=4,
                  height=2, command=lambda: self.del_page_editarea("del")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)

        tk.Button(self.frameM6, text="4", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("4")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="5", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("5")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="6", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("6")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)

        tk.Button(self.frameM7, text="1", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("1")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="2", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("2")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="3", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("3")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="0", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("0")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="Search", font=("Helvetica", 20, "bold "), fg="white", bg="dark green",
                  width=8, height=2, command=lambda: self.student_modify_search()).pack(
            side=tk.LEFT)

        self.editAreaTable2.insert(tk.INSERT, 'Input Student id to Search: ')

        #self.staff_list_all()

        pass
        pass


    def student_search_id(self):

        option_list = self.del_list
        self.del_list = ''
        self.editAreaTable3.delete("1.0", END)

        first_name = []
        last_name = []
        sex = []
        date_of_birth = []
        student_id = []
        face_cap = []
        face_train = []

        cur = self.conn_fyp.cursor()
        cur.execute("select first_name from student where student_id = '"+str(option_list)+"'")

        for row in cur.fetchall():
            first_name.append(row)
        # print(str(first_name[0])[16:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select last_name from student where student_id = '"+str(option_list)+"'")

        for row in cur.fetchall():
            last_name.append(row)
        # print(str(last_name[0])[15:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select sex from student where student_id = '"+str(option_list)+"'")

        for row in cur.fetchall():
            sex.append(row)
        # print(str(sex[0])[9:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select date_of_birth from student where student_id = '"+str(option_list)+"'")

        for row in cur.fetchall():
            date_of_birth.append(row)
        # print(str(date_of_birth[0])[19:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select student_id from student where student_id = '"+str(option_list)+"'")

        for row in cur.fetchall():
            student_id.append(row)
        # print(str(student_id[0])[15:-1])

        cur = self.conn_fyp.cursor()
        cur.execute("select face_cap from student where student_id = '"+str(option_list)+"'")

        for row in cur.fetchall():
            face_cap.append(row)
        # print(str(face_cap[0])[14:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select face_train from student where student_id = '"+str(option_list)+"'")

        for row in cur.fetchall():
            face_train.append(row)
        # print(str(face_train[0])[16:-2])



        self.editAreaTable.delete("1.0", END)
        x = 0
        while x < len(student_id):
            self.editAreaTable.insert(tk.INSERT, 'Student id: ' + str(student_id[x])[15:-1] + '\n')
            self.editAreaTable.insert(tk.INSERT,
                                      'Name: ' + str(first_name[x])[16:-2] + ' ' + str(last_name[x])[15:-2] + '\n')
            self.editAreaTable.insert(tk.INSERT, 'Sex: ' + str(sex[x])[9:-2] + '\n')
            self.editAreaTable.insert(tk.INSERT, 'Date of birth: ' + str(date_of_birth[x])[19:-2] + '\n')
            self.editAreaTable.insert(tk.INSERT, 'Face capture: ' + str(face_cap[x])[14:-2] + '\n')
            self.editAreaTable.insert(tk.INSERT, 'Face trainning: ' + str(face_train[x])[16:-2] + '\n')

            self.editAreaTable.insert(tk.INSERT, '\n')
            self.editAreaTable.insert(tk.INSERT, '\n')
            self.editAreaTable.insert(tk.INSERT, '\n')

            x += 1

        pass

    def student_order_last_name(self):
        self.editAreaTable.delete("1.0", END)
        first_name = []
        last_name = []
        sex = []
        date_of_birth = []
        student_id = []
        face_cap = []
        face_train = []

        cur = self.conn_fyp.cursor()
        cur.execute("select first_name from student order by last_name")

        for row in cur.fetchall():
            first_name.append(row)
        # print(str(first_name[0])[16:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select last_name from student order by last_name")

        for row in cur.fetchall():
            last_name.append(row)
        # print(str(last_name[0])[15:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select sex from student order by last_name")

        for row in cur.fetchall():
            sex.append(row)
        # print(str(sex[0])[9:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select date_of_birth from student order by last_name")

        for row in cur.fetchall():
            date_of_birth.append(row)
        # print(str(date_of_birth[0])[19:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select student_id from student order by last_name")

        for row in cur.fetchall():
            student_id.append(row)
        # print(str(student_id[0])[15:-1])

        cur = self.conn_fyp.cursor()
        cur.execute("select face_cap from student order by last_name")

        for row in cur.fetchall():
            face_cap.append(row)
        # print(str(face_cap[0])[14:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select face_train from student order by last_name")

        for row in cur.fetchall():
            face_train.append(row)
        # print(str(face_train[0])[16:-2])




        x = 0
        while x < len(student_id):
            self.editAreaTable.insert(tk.INSERT, 'Student id: ' + str(student_id[x])[15:-1] + '\n')
            self.editAreaTable.insert(tk.INSERT,
                                      'Name: ' + str(first_name[x])[16:-2] + ' ' + str(last_name[x])[15:-2] + '\n')
            self.editAreaTable.insert(tk.INSERT, 'Sex: ' + str(sex[x])[9:-2] + '\n')
            self.editAreaTable.insert(tk.INSERT, 'Date of birth: ' + str(date_of_birth[x])[19:-2] + '\n')
            self.editAreaTable.insert(tk.INSERT, 'Face capture: ' + str(face_cap[x])[14:-2] + '\n')
            self.editAreaTable.insert(tk.INSERT, 'Face trainning: ' + str(face_train[x])[16:-2] + '\n')

            self.editAreaTable.insert(tk.INSERT, '\n')
            self.editAreaTable.insert(tk.INSERT, '\n')
            self.editAreaTable.insert(tk.INSERT, '\n')

            x += 1
        pass

    def student_list_all(self):
        self.editAreaTable.delete("1.0", END)
        first_name = []
        last_name = []
        sex = []
        date_of_birth = []
        student_id = []
        face_cap = []
        face_train = []

        cur = self.conn_fyp.cursor()
        cur.execute("select first_name from student")

        for row in cur.fetchall():
            first_name.append(row)
        # print(str(first_name[0])[16:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select last_name from student")

        for row in cur.fetchall():
            last_name.append(row)
        # print(str(last_name[0])[15:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select sex from student")

        for row in cur.fetchall():
            sex.append(row)
        # print(str(sex[0])[9:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select date_of_birth from student")

        for row in cur.fetchall():
            date_of_birth.append(row)
        # print(str(date_of_birth[0])[19:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select student_id from student")

        for row in cur.fetchall():
            student_id.append(row)
        # print(str(student_id[0])[15:-1])

        cur = self.conn_fyp.cursor()
        cur.execute("select face_cap from student")

        for row in cur.fetchall():
            face_cap.append(row)
        # print(str(face_cap[0])[14:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select face_train from student")

        for row in cur.fetchall():
            face_train.append(row)
        # print(str(face_train[0])[16:-2])




        x = 0
        while x < len(student_id):
            self.editAreaTable.insert(tk.INSERT, 'Student id: ' + str(student_id[x])[15:-1] + '\n')
            self.editAreaTable.insert(tk.INSERT,
                                      'Name: ' + str(first_name[x])[16:-2] + ' ' + str(last_name[x])[15:-2] + '\n')
            self.editAreaTable.insert(tk.INSERT, 'Sex: ' + str(sex[x])[9:-2] + '\n')
            self.editAreaTable.insert(tk.INSERT, 'Date of birth: ' + str(date_of_birth[x])[19:-2] + '\n')
            self.editAreaTable.insert(tk.INSERT, 'Face capture: ' + str(face_cap[x])[14:-2] + '\n')
            self.editAreaTable.insert(tk.INSERT, 'Face trainning: ' + str(face_train[x])[16:-2] + '\n')

            self.editAreaTable.insert(tk.INSERT, '\n')
            self.editAreaTable.insert(tk.INSERT, '\n')
            self.editAreaTable.insert(tk.INSERT, '\n')

            x += 1
        pass

    def student_list(self):
        self.del_list=''
        self.left_frame.pack_forget()
        self.left_frame = Frame(self.root, background="black",
                                borderwidth=5, relief="ridge",
                                width=600)
        self.left_frame.pack(side="left",
                             fill="both",
                             expand="yes",
                             )



        self.middle_frame = Frame(self.root, width=20, background="black",
                                  borderwidth=5, relief="ridge",
                                  )
        self.middle_frame.pack(side="left",
                               fill="both",

                               )
        tk.Label(self.left_frame, bg='black', text='Student List',
                 font=("Helvetica", 20, "bold "), fg="white", borderwidth=5).pack()

        self.editAreaTable = tkst.ScrolledText(self.left_frame, height=8, width=69, background="black", fg="white",
                                               font=("Helvetica", 15, "bold"))
        self.editAreaTable.pack(fill="both", expand="yes", side="left")
        '''
        self.editAreaTable.insert(tk.INSERT,
                                  "Order id: O001\n\nOrder time: 2/2/2020 11:11:11\n\nSuper Supreme x1 $168\nDelivery fee: $20\nTotal $188\n\nDelivery Location: Flat B, 23/F, Block 66, XYZ Garden, 8 Testing Road, HK\nPayment: Cash\nDelivery time: 30 min\n\n\n")
        self.editAreaTable.insert(tk.INSERT,
                                  "Order id: O124\n\nOrder time: 1/2/2020 11:11:11\n\nSupreme x2 $296\nDelivery fee: $20\nTotal $316\n\nDelivery Location: Flat B, 23/F, Block 66, XYZ Garden, 8 Testing Road, HK\nPayment: Cash\nDelivery time:1/2/2020 11:33:11")
        '''

        self.btnTR1.config(text='Order by\nLast Name', font=("Helvetica", 20, "bold "), bg="grey20",
                           command=lambda:self.student_order_last_name())
        self.btnTR2.config(text='List All', font=("Helvetica", 20, "bold "), bg="grey20",command=lambda:self.student_list_all())
        self.btnTR3.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR4.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR5.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR6.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR7.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR8.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")

        self.btnBack.config(command=lambda: self.last_page("add_order"))
        self.btnHome.config(command=lambda: self.home_page("add_order"))

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

        self.editAreaTable2 = tkst.ScrolledText(self.frameM1, height=10, width=40, background="black", fg="white",
                                                font=("Helvetica", 15, "bold"))
        self.editAreaTable2.pack(fill="both", expand="yes", side="left")

        self.editAreaTable3 = tkst.ScrolledText(self.frameM2, height=2, width=40, background="black", fg="white",
                                                font=("Helvetica", 15, "bold"))
        self.editAreaTable3.pack(fill="both", expand="yes", side="left")

        tk.Button(self.frameM5, text="7", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("7")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="8", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("8")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="9", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("9")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="<[X]", font=("Helvetica", 20, "bold "), fg="white", bg="dark red", width=4,
                  height=2, command=lambda: self.del_page_editarea("del")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)

        tk.Button(self.frameM6, text="4", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("4")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="5", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("5")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="6", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("6")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)

        tk.Button(self.frameM7, text="1", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("1")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="2", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("2")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="3", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("3")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="0", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("0")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="Search", font=("Helvetica", 20, "bold "), fg="white", bg="dark green",
                  width=8, height=2, command=lambda:self.student_search_id()).pack(
            side=tk.LEFT)


        self.editAreaTable2.insert(tk.INSERT, 'Input Student id to Search: ')



        self.student_list_all()


        pass



    def course_modify_update(self):
        cur = self.conn_fyp.cursor()
        cur.execute("update course set `course_name` = '"+str(self.create_input1.get())+ "' where course_id = '" + str( self.option_list) + "'")
        cur.execute("commit")

        cur = self.conn_fyp.cursor()
        cur.execute("update course set `staff_id` = '" + str(self.create_input2.get()) + "' where course_id = '" + str( self.option_list) + "'")
        cur.execute("commit")




        cur.close()
        self.db_fyp = pymysql.connect('localhost', 'root', '', 'fyp')
        self.conn_fyp = pymysql.connect(user='root',
                                    password='',
                                    db='fyp',
                                    cursorclass=pymysql.cursors.DictCursor)
        cur = self.db_fyp.cursor()



        self.date_label.config(text=str(self.user_name[0])[15:-2] + "      " + str(self.option_list) + ":Has Been updated      " + str(
            self.date.strftime('%Y/%m/%d') + '      '))
        self.create_input1.delete(0, 'end')
        self.create_input2.delete(0, 'end')


        pass

    def course_modify_search(self):
        self.option_list = self.del_list
        self.del_list = ''
        self.editAreaTable3.delete("1.0", END)

        course_name = []
        staff_id = []


        cur = self.conn_fyp.cursor()
        cur.execute("select course_name from course where course_id = '" + str( self.option_list) + "'")

        for row in cur.fetchall():
            course_name.append(row)
        #print(str(course_name[0])[16:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select staff_id from course where course_id = '" + str( self.option_list) + "'")

        for row in cur.fetchall():
            staff_id.append(row)
        #print(str(staff_id[0])[15:-2])







        self.create_input1.delete(0, 'end')
        self.create_input2.delete(0, 'end')



        self.create_input1.insert(END, str(course_name[0])[17:-2])
        self.create_input2.insert(END, str(staff_id[0])[13:-1])





        pass

    def course_modify(self):
        self.del_list=''
        self.left_frame.pack_forget()
        self.left_frame = Frame(self.root, background="black",
                                borderwidth=5, relief="ridge",
                                width=600)
        self.left_frame.pack(side="left",
                             fill="both",
                             expand="yes",
                             )

        self.middle_frame = Frame(self.root, width=20, background="black",
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

        self.create_title1 = tk.Label(self.frameL1, text="Course Modify", font=("Helvetica", 30),
                                      fg="white",
                                      background="black")
        self.create_title1.pack(side=tk.LEFT)

        self.create_title2 = tk.Label(self.frameL3, text="Please update the followings", font=("Helvetica", 10),
                                      fg="white",
                                      background="black")
        self.create_title2.pack(side=tk.LEFT)

        self.create_label1 = tk.Label(self.frameL4, text="Course Name: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label1.pack(side=tk.LEFT)

        self.create_input1 = tk.Entry(self.frameL4, text="", background="white", width=80)
        self.create_input1.pack(side=tk.LEFT)

        self.create_label2 = tk.Label(self.frameL5, text="Staff ID: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label2.pack(side=tk.LEFT)

        self.create_input2 = tk.Entry(self.frameL5, text="", background="white", width=80)
        self.create_input2.pack(side=tk.LEFT)





        self.create_submit = tk.Button(self.frameL6, text='Submit', font=("Helvetica", 20, "bold "), fg="white",
                                       bg="dark green",
                                       width=12, height=2, command=lambda: self.course_modify_update())
        self.create_submit.pack(side=tk.LEFT)

        self.btnTR1.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR2.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR3.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR4.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR5.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR6.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR7.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR8.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")

        self.btnBack.config(command=lambda: self.home_page("add_order"))
        self.btnHome.config(command=lambda: self.home_page("add_order"))

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

        self.editAreaTable2 = tkst.ScrolledText(self.frameM1, height=10, width=40, background="black", fg="white",
                                                font=("Helvetica", 15, "bold"))
        self.editAreaTable2.pack(fill="both", expand="yes", side="left")

        self.editAreaTable3 = tkst.ScrolledText(self.frameM2, height=2, width=40, background="black", fg="white",
                                                font=("Helvetica", 15, "bold"))
        self.editAreaTable3.pack(fill="both", expand="yes", side="left")

        tk.Button(self.frameM5, text="7", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("7")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="8", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("8")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="9", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("9")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="<[X]", font=("Helvetica", 20, "bold "), fg="white", bg="dark red", width=4,
                  height=2, command=lambda: self.del_page_editarea("del")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)

        tk.Button(self.frameM6, text="4", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("4")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="5", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("5")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="6", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("6")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)

        tk.Button(self.frameM7, text="1", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("1")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="2", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("2")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="3", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("3")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="0", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("0")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="Search", font=("Helvetica", 20, "bold "), fg="white", bg="dark green",
                  width=8, height=2, command=lambda: self.course_modify_search()).pack(
            side=tk.LEFT)

        self.editAreaTable2.insert(tk.INSERT, 'Input Course id to Search: ')

        #self.staff_list_all()

        pass
        pass



    def course_list_my(self):
        self.editAreaTable.delete("1.0", END)
        first_name = []
        last_name = []
        course_id = []
        course_name = []
        staff_id=[]


        if self.section ==2:
            cur = self.conn_fyp.cursor()
            cur.execute("select course_id from course  where staff_id = '"+str(self.id)+"' order by course_name")

            for row in cur.fetchall():
                course_id.append(row)
            #print(str(course_id[0])[14:-1])

            cur = self.conn_fyp.cursor()
            cur.execute("select course_name from course  where staff_id = '"+str(self.id)+"' order by course_name")

            for row in cur.fetchall():
                course_name.append(row)
            #print(str(course_name[0])[17:-2])

        else:
            cur = self.conn_fyp.cursor()
            cur.execute("select student_course.course_id from student_course inner join course on  student_course.course_id =  course.course_id  where student_course.student_id = '" + str(self.id) + "' order by course.course_name")

            for row in cur.fetchall():
                course_id.append(row)
            # print(str(course_id[0])[14:-1])

            i=0
            while i<len(course_id):
                cur = self.conn_fyp.cursor()
                cur.execute("select course_name from course  where course_id = '" + str(course_id[i])[14:-1] + "'")

                for row in cur.fetchall():
                    course_name.append(row)
                    # print(str(course_name[0])[17:-2])


                cur = self.conn_fyp.cursor()
                cur.execute("select staff_id  from course where course_id = '" + str(course_id[i])[14:-1]+"'")

                for row in cur.fetchall():
                    staff_id.append(row)
                #print(str(staff_id[0])[13:-1])
                i += 1
            y=0
            while y<len(staff_id):
                cur = self.conn_fyp.cursor()
                cur.execute("select first_name  from staff where staff_id = '"+str(staff_id[y])[13:-1]+"'")

                for row in cur.fetchall():
                    first_name.append(row)
                    #print(str(first_name[0])[16:-2])

                cur = self.conn_fyp.cursor()
                cur.execute("select last_name  from staff where staff_id = '" + str(staff_id[y])[13:-1] + "'")

                for row in cur.fetchall():
                    last_name.append(row)
                # print(str(last_name[0])[15:-2])

                y+=1



        x = 0
        while x < len(course_id):
            self.editAreaTable.insert(tk.INSERT, 'Course ID: ' +str(course_id[x])[14:-1]+ '\n')
            self.editAreaTable.insert(tk.INSERT,
                                      'Course Name: ' + str(course_name[x])[17:-2] + '\n')
            if self.section ==3:
                self.editAreaTable.insert(tk.INSERT, 'Staff ID: ' + str(staff_id[x])[13:-1] + '\n')
                self.editAreaTable.insert(tk.INSERT, 'Teacher Name: ' + str(first_name[x])[16:-2]+" "+str(last_name[x])[15:-2] + '\n')
            #self.editAreaTable.insert(tk.INSERT, 'Position: ' + str(position[x])[14:-2] + '\n')
            #self.editAreaTable.insert(tk.INSERT, 'Face trainning: ' + str(face_train[x])[16:-2] + '\n')

            self.editAreaTable.insert(tk.INSERT, '\n')
            self.editAreaTable.insert(tk.INSERT, '\n')
            self.editAreaTable.insert(tk.INSERT, '\n')

            x += 1

        pass

    def course_list_all(self):
        self.editAreaTable.delete("1.0", END)
        first_name = []
        last_name = []
        course_id = []
        course_name = []
        staff_id=[]



        cur = self.conn_fyp.cursor()
        cur.execute("select course_id from course order by course_name")

        for row in cur.fetchall():
            course_id.append(row)
        #print(str(course_id[0])[14:-1])

        cur = self.conn_fyp.cursor()
        cur.execute("select course_name from course order by course_name")

        for row in cur.fetchall():
            course_name.append(row)
        #print(str(course_name[0])[17:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select staff_id  from course order by course_name")

        for row in cur.fetchall():
            staff_id.append(row)
        #print(str(staff_id[0])[13:-1])

        y=0
        while y<len(staff_id):
            cur = self.conn_fyp.cursor()
            cur.execute("select first_name  from staff where staff_id = '"+str(staff_id[y])[13:-1]+"'")

            for row in cur.fetchall():
                first_name.append(row)
                #print(str(first_name[0])[16:-2])

            cur = self.conn_fyp.cursor()
            cur.execute("select last_name  from staff where staff_id = '" + str(staff_id[y])[13:-1] + "'")

            for row in cur.fetchall():
                last_name.append(row)
               # print(str(last_name[0])[15:-2])

            y+=1



        x = 0
        while x < len(course_id):
            self.editAreaTable.insert(tk.INSERT, 'Course ID: ' +str(course_id[x])[14:-1]+ '\n')
            self.editAreaTable.insert(tk.INSERT,
                                      'Course Name: ' + str(course_name[x])[17:-2] + '\n')
            self.editAreaTable.insert(tk.INSERT, 'Staff ID: ' + str(staff_id[x])[13:-1] + '\n')
            self.editAreaTable.insert(tk.INSERT, 'Teacher Name: ' + str(first_name[x])[16:-2]+" "+str(last_name[x])[15:-2] + '\n')
            #self.editAreaTable.insert(tk.INSERT, 'Position: ' + str(position[x])[14:-2] + '\n')
            #self.editAreaTable.insert(tk.INSERT, 'Face trainning: ' + str(face_train[x])[16:-2] + '\n')

            self.editAreaTable.insert(tk.INSERT, '\n')
            self.editAreaTable.insert(tk.INSERT, '\n')
            self.editAreaTable.insert(tk.INSERT, '\n')

            x += 1

        pass

    def course_list(self):
        self.del_list=''

        self.left_frame.pack_forget()
        self.left_frame = Frame(self.root, background="black",
                                borderwidth=5, relief="ridge",
                                width=600)
        self.left_frame.pack(side="left",
                             fill="both",
                             expand="yes",
                             )





        tk.Label(self.left_frame, bg='black', text='Course list',
                 font=("Helvetica", 20, "bold "), fg="white", borderwidth=5).pack()

        self.editAreaTable = tkst.ScrolledText(self.left_frame, height=8, width=69, background="black", fg="white",
                                               font=("Helvetica", 15, "bold"))
        self.editAreaTable.pack(fill="both", expand="yes", side="left")
        '''
        self.editAreaTable.insert(tk.INSERT,
                                  "Order id: O001\n\nOrder time: 2/2/2020 11:11:11\n\nSuper Supreme x1 $168\nDelivery fee: $20\nTotal $188\n\nDelivery Location: Flat B, 23/F, Block 66, XYZ Garden, 8 Testing Road, HK\nPayment: Cash\nDelivery time: 30 min\n\n\n")
        self.editAreaTable.insert(tk.INSERT,
                                  "Order id: O124\n\nOrder time: 1/2/2020 11:11:11\n\nSupreme x2 $296\nDelivery fee: $20\nTotal $316\n\nDelivery Location: Flat B, 23/F, Block 66, XYZ Garden, 8 Testing Road, HK\nPayment: Cash\nDelivery time:1/2/2020 11:33:11")
        '''

        if self.section ==2:
            self.btnTR1.config(text='My Course', font=("Helvetica", 20, "bold "), bg="grey20",
                               command=lambda:self.course_list_my())
            self.btnTR2.config(text='List All', font=("Helvetica", 20, "bold "), bg="grey20",command=lambda:self.course_list_all())
        else:
            self.btnTR1.config(text='', font=("Helvetica", 20, "bold "), bg="grey20",command='')
            self.btnTR2.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR3.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR4.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR5.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR6.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR7.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR8.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")

        self.btnBack.config(command=lambda: self.home_page("_order"))
        self.btnHome.config(command=lambda: self.home_page("_order"))

        if self.section == 2 or self.section == 3:
            self.course_list_my()
        else:
            self.course_list_all()


        pass



    def add_student_course_update(self):

        result_list = []
        cur = self.conn_fyp.cursor()
        cur.execute(
            "select student_id from student_course where student_id = '" + str(self.stdid_value) + "' and course_id =  '"+str(self.cid_value)+"'")
        for row in cur.fetchall():
            result_list.append(row)
            print(str(result_list[0]))

        if (result_list) != []:
            self.date_label.config(
                text=str(self.user_name[0])[15:-2] + "      " + "Already exeisted" + "      " + str(
                    self.date.strftime('%Y/%m/%d') + '      '))

        else:

            sql=("insert into student_course (course_id, student_id) values('"+str(self.cid_value)+"','"+str(self.stdid_value)+"')")
            self.cur_fyp.execute(sql)
            self.cur_fyp.execute('commit')
            self.cur_fyp.close()
            self.db_fyp = pymysql.connect('localhost', 'root', '', 'fyp')
            self.conn_fyp = pymysql.connect(user='root',
                                            password='',
                                            db='fyp',
                                            cursorclass=pymysql.cursors.DictCursor)
            self.cur_fyp = self.db_fyp.cursor()

            self.date_label.config(text=str(self.user_name[0])[15:-2] + "      " + str(self.stdid_value) + ":Has Been added to" +str(self.cid_value)+"      " + str(self.date.strftime('%Y/%m/%d') + '      '))

        self.create_label1.config(text='First Name:')
        self.create_label2.config(text='Last Name:' )
        self.create_label3.config(text='Course:')
        self.create_label_stdid.config(text='')
        self.create_label_cid.config(text='')

    def add_student_course_search_course(self):
        self.option_list = self.del_list
        self.del_list = ''
        self.editAreaTable3.delete("1.0", END)

        course_name = []
        last_name = []
        sex = []
        date_of_birth = []
        student_id = []
        position = []

        cur = self.conn_fyp.cursor()
        cur.execute("select course_name from course where course_id = '" + str( self.option_list) + "'")

        for row in cur.fetchall():
            course_name.append(row)
        # print(str(course_name[0])[17:-2])




        self.create_label3.config(text='Course:'+str(course_name[0])[17:-2])
        self.create_label_cid.config(text=str(self.option_list))
        self.cid_value = str(self.option_list)
        self.editAreaTable2.delete("1.0", END)
        self.editAreaTable2.insert(tk.INSERT, 'Input Student id to Search: ')
        self.search_btn_course.config(command=lambda: self.add_student_course_search())

        pass

    def add_student_course_search(self):
        self.option_list = self.del_list
        self.del_list = ''
        self.editAreaTable3.delete("1.0", END)

        first_name = []
        last_name = []
        sex = []
        date_of_birth = []
        student_id = []
        position = []

        cur = self.conn_fyp.cursor()
        cur.execute("select first_name from student where student_id = '" + str( self.option_list) + "'")

        for row in cur.fetchall():
            first_name.append(row)
        # print(str(first_name[0])[16:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select last_name from student where student_id = '" + str( self.option_list) + "'")

        for row in cur.fetchall():
            last_name.append(row)
        # print(str(last_name[0])[15:-2])


        self.create_label1.config(text='First Name:'+str(first_name[0])[16:-2])
        self.create_label2.config(text='Last Name:' + str(last_name[0])[15:-2])
        self.create_label_stdid.config(text=str( self.option_list))
        self.stdid_value=str( self.option_list)
        self.editAreaTable2.delete("1.0", END)
        self.editAreaTable2.insert(tk.INSERT, 'Input Course id to Search: ')

        self.search_btn_course.config(command=lambda: self.add_student_course_search_course())

        pass

    def add_student_course(self):
        self.del_list=''
        self.left_frame.pack_forget()
        self.left_frame = Frame(self.root, background="black",
                                borderwidth=5, relief="ridge",
                                width=600)
        self.left_frame.pack(side="left",
                             fill="both",
                             expand="yes",
                             )

        self.middle_frame = Frame(self.root, width=20, background="black",
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

        self.create_title1 = tk.Label(self.frameL1, text="Add Student to Course", font=("Helvetica", 30),
                                      fg="white",
                                      background="black")
        self.create_title1.pack(side=tk.LEFT)

        self.create_title2 = tk.Label(self.frameL3, text="Please confirm the followings", font=("Helvetica", 10),
                                      fg="white",
                                      background="black")
        self.create_title2.pack(side=tk.LEFT)

        self.create_label1 = tk.Label(self.frameL4, text="First Name: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label1.pack(side=tk.LEFT)



        self.create_label2 = tk.Label(self.frameL5, text="Last Name: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label2.pack(side=tk.LEFT)



        self.create_label3 = tk.Label(self.frameL6, text="Course: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label3.pack(side=tk.LEFT)

        self.create_label4 = tk.Label(self.frameL7, text="Student ID: ", font=("Helvetica", 15), fg="white",
                                      background="black")
        self.create_label4.pack(side=tk.LEFT)

        self.create_label_stdid = tk.Label(self.frameL7, text="", font=("Helvetica", 15), fg="white",
                                      background="black")
        self.create_label_stdid.pack(side=tk.LEFT)

        self.create_label5 = tk.Label(self.frameL7, text="Course ID: ", font=("Helvetica", 15), fg="white",
                                      background="black")
        self.create_label5.pack(side=tk.LEFT)

        self.create_label_cid = tk.Label(self.frameL7, text="", font=("Helvetica", 15), fg="white",
                                           background="black")
        self.create_label_cid.pack(side=tk.LEFT)




        self.create_submit = tk.Button(self.frameL8, text='Submit', font=("Helvetica", 20, "bold "), fg="white",
                                       bg="dark green",
                                       width=12, height=2, command=lambda: self.add_student_course_update())
        self.create_submit.pack(side=tk.LEFT)

        self.btnTR1.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR2.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR3.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR4.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR5.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR6.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR7.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR8.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")

        self.btnBack.config(command=lambda: self.home_page("add_order"))
        self.btnHome.config(command=lambda: self.home_page("add_order"))

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

        self.editAreaTable2 = tkst.ScrolledText(self.frameM1, height=10, width=40, background="black", fg="white",
                                                font=("Helvetica", 15, "bold"))
        self.editAreaTable2.pack(fill="both", expand="yes", side="left")

        self.editAreaTable3 = tkst.ScrolledText(self.frameM2, height=2, width=40, background="black", fg="white",
                                                font=("Helvetica", 15, "bold"))
        self.editAreaTable3.pack(fill="both", expand="yes", side="left")

        tk.Button(self.frameM5, text="7", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("7")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="8", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("8")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="9", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("9")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="<[X]", font=("Helvetica", 20, "bold "), fg="white", bg="dark red", width=4,
                  height=2, command=lambda: self.del_page_editarea("del")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)

        tk.Button(self.frameM6, text="4", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("4")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="5", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("5")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="6", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("6")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)

        tk.Button(self.frameM7, text="1", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("1")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="2", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("2")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="3", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("3")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="0", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("0")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command='').pack(
            side=tk.LEFT)
        self.search_btn_course=tk.Button(self.frameM8, text="Search", font=("Helvetica", 20, "bold "), fg="white", bg="dark green",
                  width=8, height=2, command=lambda: self.add_student_course_search())
        self.search_btn_course.pack(side=tk.LEFT)

        self.editAreaTable2.insert(tk.INSERT, 'Input Student id to Search: ')

        self.staff_list_all()

        pass
        pass



    def del_student_course_update(self):

        result_list = []
        cur = self.conn_fyp.cursor()
        cur.execute(
            "select student_id from student_course where student_id = '" + str(self.stdid_value) + "' and course_id =  '"+str(self.cid_value)+"'")
        for row in cur.fetchall():
            result_list.append(row)
            print(str(result_list[0]))

        if (result_list) == []:
            self.date_label.config(
                text=str(self.user_name[0])[15:-2] + "      " + "Already not exeisted" + "      " + str(
                    self.date.strftime('%Y/%m/%d') + '      '))

        else:

            sql = ("delete from student_course where course_id ='" + str(self.cid_value) + "' and student_id ='" + str(
                self.stdid_value) + "'")

            self.cur_fyp.execute(sql)
            self.cur_fyp.execute('commit')
            self.cur_fyp.close()
            self.db_fyp = pymysql.connect('localhost', 'root', '', 'fyp')
            self.conn_fyp = pymysql.connect(user='root',
                                            password='',
                                            db='fyp',
                                            cursorclass=pymysql.cursors.DictCursor)
            self.cur_fyp = self.db_fyp.cursor()

            self.date_label.config(text=str(self.user_name[0])[15:-2] + "      " + str(self.stdid_value) + ":Has Been delete from" +str(self.cid_value)+"      " + str(self.date.strftime('%Y/%m/%d') + '      '))

        self.create_label1.config(text='First Name:')
        self.create_label2.config(text='Last Name:' )
        self.create_label3.config(text='Course:')
        self.create_label_stdid.config(text='')
        self.create_label_cid.config(text='')

    def del_student_course_search_course(self):
        self.option_list = self.del_list
        self.del_list = ''
        self.editAreaTable3.delete("1.0", END)

        course_name = []
        last_name = []
        sex = []
        date_of_birth = []
        student_id = []
        position = []

        cur = self.conn_fyp.cursor()
        cur.execute("select course_name from course where course_id = '" + str( self.option_list) + "'")

        for row in cur.fetchall():
            course_name.append(row)
        # print(str(course_name[0])[17:-2])




        self.create_label3.config(text='Course:'+str(course_name[0])[17:-2])
        self.create_label_cid.config(text=str(self.option_list))
        self.cid_value = str(self.option_list)
        self.editAreaTable2.delete("1.0", END)
        self.editAreaTable2.insert(tk.INSERT, 'Input Student id to Search: ')
        self.search_btn_course.config(command=lambda: self.del_student_course_search())

        pass

    def del_student_course_search(self):
        self.option_list = self.del_list
        self.del_list = ''
        self.editAreaTable3.delete("1.0", END)

        first_name = []
        last_name = []
        sex = []
        date_of_birth = []
        student_id = []
        position = []

        cur = self.conn_fyp.cursor()
        cur.execute("select first_name from student where student_id = '" + str( self.option_list) + "'")

        for row in cur.fetchall():
            first_name.append(row)
        # print(str(first_name[0])[16:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select last_name from student where student_id = '" + str( self.option_list) + "'")

        for row in cur.fetchall():
            last_name.append(row)
        # print(str(last_name[0])[15:-2])


        self.create_label1.config(text='First Name:'+str(first_name[0])[16:-2])
        self.create_label2.config(text='Last Name:' + str(last_name[0])[15:-2])
        self.create_label_stdid.config(text=str( self.option_list))
        self.stdid_value=str( self.option_list)
        self.editAreaTable2.delete("1.0", END)
        self.editAreaTable2.insert(tk.INSERT, 'Input Course id to Search: ')

        self.search_btn_course.config(command=lambda: self.del_student_course_search_course())

        pass

    def del_student_course(self):
        self.del_list=''
        self.left_frame.pack_forget()
        self.left_frame = Frame(self.root, background="black",
                                borderwidth=5, relief="ridge",
                                width=600)
        self.left_frame.pack(side="left",
                             fill="both",
                             expand="yes",
                             )

        self.middle_frame = Frame(self.root, width=20, background="black",
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

        self.create_title1 = tk.Label(self.frameL1, text="Delete Student from Course", font=("Helvetica", 30),
                                      fg="white",
                                      background="black")
        self.create_title1.pack(side=tk.LEFT)

        self.create_title2 = tk.Label(self.frameL3, text="Please confirm the followings", font=("Helvetica", 10),
                                      fg="white",
                                      background="black")
        self.create_title2.pack(side=tk.LEFT)

        self.create_label1 = tk.Label(self.frameL4, text="First Name: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label1.pack(side=tk.LEFT)



        self.create_label2 = tk.Label(self.frameL5, text="Last Name: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label2.pack(side=tk.LEFT)



        self.create_label3 = tk.Label(self.frameL6, text="Course: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label3.pack(side=tk.LEFT)

        self.create_label4 = tk.Label(self.frameL7, text="Student ID: ", font=("Helvetica", 15), fg="white",
                                      background="black")
        self.create_label4.pack(side=tk.LEFT)

        self.create_label_stdid = tk.Label(self.frameL7, text="", font=("Helvetica", 15), fg="white",
                                      background="black")
        self.create_label_stdid.pack(side=tk.LEFT)

        self.create_label5 = tk.Label(self.frameL7, text="Course ID: ", font=("Helvetica", 15), fg="white",
                                      background="black")
        self.create_label5.pack(side=tk.LEFT)

        self.create_label_cid = tk.Label(self.frameL7, text="", font=("Helvetica", 15), fg="white",
                                           background="black")
        self.create_label_cid.pack(side=tk.LEFT)




        self.create_submit = tk.Button(self.frameL8, text='Submit', font=("Helvetica", 20, "bold "), fg="white",
                                       bg="dark green",
                                       width=12, height=2, command=lambda: self.del_student_course_update())
        self.create_submit.pack(side=tk.LEFT)

        self.btnTR1.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR2.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR3.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR4.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR5.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR6.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR7.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR8.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")

        self.btnBack.config(command=lambda: self.home_page("add_order"))
        self.btnHome.config(command=lambda: self.home_page("add_order"))

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

        self.editAreaTable2 = tkst.ScrolledText(self.frameM1, height=10, width=40, background="black", fg="white",
                                                font=("Helvetica", 15, "bold"))
        self.editAreaTable2.pack(fill="both", expand="yes", side="left")

        self.editAreaTable3 = tkst.ScrolledText(self.frameM2, height=2, width=40, background="black", fg="white",
                                                font=("Helvetica", 15, "bold"))
        self.editAreaTable3.pack(fill="both", expand="yes", side="left")

        tk.Button(self.frameM5, text="7", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("7")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="8", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("8")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="9", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("9")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="<[X]", font=("Helvetica", 20, "bold "), fg="white", bg="dark red", width=4,
                  height=2, command=lambda: self.del_page_editarea("del")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)

        tk.Button(self.frameM6, text="4", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("4")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="5", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("5")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="6", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("6")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)

        tk.Button(self.frameM7, text="1", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("1")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="2", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("2")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="3", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("3")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="0", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("0")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command='').pack(
            side=tk.LEFT)
        self.search_btn_course=tk.Button(self.frameM8, text="Search", font=("Helvetica", 20, "bold "), fg="white", bg="dark green",
                  width=8, height=2, command=lambda: self.del_student_course_search())
        self.search_btn_course.pack(side=tk.LEFT)

        self.editAreaTable2.insert(tk.INSERT, 'Input Student id to Search: ')

        self.staff_list_all()

        pass
        pass




    def add_timetable_update(self):
        sql = ("insert into `course_timetable` (`course_id`,`day`,`time`,`room`) values ( '" + str( self.option_list)+"','"+self.create_input3.get()+"-"+self.create_input4.get()+"-"+self.create_input5.get()+"','"+self.create_input6.get()+"','"+self.create_input7.get()+"')")

        self.cur_fyp.execute(sql)
        self.cur_fyp.execute('commit')

        self.cur_fyp.close()
        self.db_fyp = pymysql.connect('localhost', 'root', '', 'fyp')
        self.conn_fyp = pymysql.connect(user='root',
                                    password='',
                                    db='fyp',
                                    cursorclass=pymysql.cursors.DictCursor)
        self.cur_fyp = self.db_fyp.cursor()



        self.date_label.config(text=str(self.user_name[0])[15:-2] + "      " + str( self.option_list)+ " :inserted      " + str(
            self.date.strftime('%Y/%m/%d') + '      '))
        #self.create_input1.delete(0, 'end')
        #self.create_input2.delete(0, 'end')
        self.create_input3.delete(0, 'end')
        self.create_input4.delete(0, 'end')
        self.create_input5.delete(0, 'end')
        self.create_input6.delete(0, 'end')
        self.create_input7.delete(0, 'end')


        pass

    def add_timetable_search(self):
        self.option_list = self.del_list
        self.del_list = ''
        self.editAreaTable3.delete("1.0", END)

        course_name = []
        last_name = []
        sex = []
        date_of_birth = []
        student_id = []
        position = []

        cur = self.conn_fyp.cursor()
        cur.execute("select Course_name from course where course_id = '" + str( self.option_list) + "'")

        for row in cur.fetchall():
            course_name.append(row)
        # print(str(first_name[0])[16:-2])


        self.create_label1.config(text='Course Name:' + str(course_name[0])[17:-2])

        pass

    def add_timetable(self):
        self.del_list=''
        self.left_frame.pack_forget()
        self.left_frame = Frame(self.root, background="black",
                                borderwidth=5, relief="ridge",
                                width=600)
        self.left_frame.pack(side="left",
                             fill="both",
                             expand="yes",
                             )

        self.middle_frame = Frame(self.root, width=20, background="black",
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

        self.create_title1 = tk.Label(self.frameL1, text="Add Timetable", font=("Helvetica", 30),
                                      fg="white",
                                      background="black")
        self.create_title1.pack(side=tk.LEFT)

        self.create_title2 = tk.Label(self.frameL3, text="Please input the followings", font=("Helvetica", 10),
                                      fg="white",
                                      background="black")
        self.create_title2.pack(side=tk.LEFT)

        self.create_label1 = tk.Label(self.frameL4, text="Course ID: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label1.pack(side=tk.LEFT)





        self.create_label3 = tk.Label(self.frameL5, text="Day(Date): ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label3.pack(side=tk.LEFT)

        self.create_input3 = tk.Entry(self.frameL5, text="", background="white", width=80)
        self.create_input3.pack(side=tk.LEFT)

        self.create_label4 = tk.Label(self.frameL6, text="Day(Month): ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label4.pack(side=tk.LEFT)

        self.create_input4 = tk.Entry(self.frameL6, text="", background="white", width=80)
        self.create_input4.pack(side=tk.LEFT)

        self.create_label5 = tk.Label(self.frameL7, text="Day(Year): ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label5.pack(side=tk.LEFT)

        self.create_input5 = tk.Entry(self.frameL7, text="", background="white", width=80)
        self.create_input5.pack(side=tk.LEFT)

        self.create_label6 = tk.Label(self.frameL8, text="Time (24Hr): ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label6.pack(side=tk.LEFT)

        self.create_input6 = tk.Entry(self.frameL8, text="", background="white", width=80)
        self.create_input6.pack(side=tk.LEFT)

        self.create_label7 = tk.Label(self.frameL9, text="Room: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label7.pack(side=tk.LEFT)

        self.create_input7 = tk.Entry(self.frameL9, text="", background="white", width=80)
        self.create_input7.pack(side=tk.LEFT)




        self.create_submit = tk.Button(self.frameL10, text='Submit', font=("Helvetica", 20, "bold "), fg="white",
                                       bg="dark green",
                                       width=12, height=2, command=lambda: self.add_timetable_update())
        self.create_submit.pack(side=tk.LEFT)

        self.btnTR1.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR2.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR3.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR4.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR5.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR6.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR7.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR8.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")

        self.btnBack.config(command=lambda: self.home_page("add_order"))
        self.btnHome.config(command=lambda: self.home_page("add_order"))

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

        self.editAreaTable2 = tkst.ScrolledText(self.frameM1, height=10, width=40, background="black", fg="white",
                                                font=("Helvetica", 15, "bold"))
        self.editAreaTable2.pack(fill="both", expand="yes", side="left")

        self.editAreaTable3 = tkst.ScrolledText(self.frameM2, height=2, width=40, background="black", fg="white",
                                                font=("Helvetica", 15, "bold"))
        self.editAreaTable3.pack(fill="both", expand="yes", side="left")

        tk.Button(self.frameM5, text="7", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("7")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="8", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("8")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="9", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("9")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="<[X]", font=("Helvetica", 20, "bold "), fg="white", bg="dark red", width=4,
                  height=2, command=lambda: self.del_page_editarea("del")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)

        tk.Button(self.frameM6, text="4", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("4")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="5", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("5")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="6", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("6")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)

        tk.Button(self.frameM7, text="1", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("1")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="2", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("2")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="3", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("3")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="0", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("0")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="Search", font=("Helvetica", 20, "bold "), fg="white", bg="dark green",
                  width=8, height=2, command=lambda: self.add_timetable_search()).pack(
            side=tk.LEFT)

        self.editAreaTable2.insert(tk.INSERT, 'Input Course id to Search: ')

        self.staff_list_all()

        pass
        pass



    def modify_timetable_update(self):
        cur = self.conn_fyp.cursor()
        cur.execute(
            "update course_timetable set `course_id` = '" + str(self.create_input2.get()) + "' where time_table_id = '" + str(
                self.option_list) + "'")
        cur.execute("commit")

        cur = self.conn_fyp.cursor()
        cur.execute(
            "update course_timetable set `day` = '" + str(self.create_input3.get()) + "' where time_table_id = '" + str(
                self.option_list) + "'")
        cur.execute("commit")

        cur = self.conn_fyp.cursor()
        cur.execute("update course_timetable set `time` = '" + str(self.create_input6.get()) + "' where time_table_id = '" + str(
            self.option_list) + "'")
        cur.execute("commit")

        cur = self.conn_fyp.cursor()
        cur.execute(
            "update course_timetable set `room` = '" + str(self.create_input7.get()) + "' where time_table_id = '" + str(
                self.option_list) + "'")
        cur.execute("commit")

        cur.close()
        self.db_fyp = pymysql.connect('localhost', 'root', '', 'fyp')
        self.conn_fyp = pymysql.connect(user='root',
                                        password='',
                                        db='fyp',
                                        cursorclass=pymysql.cursors.DictCursor)
        cur = self.db_fyp.cursor()



        self.date_label.config(text=str(self.user_name[0])[15:-2] + "      " + str( self.option_list)+ " :updated      " + str(
            self.date.strftime('%Y/%m/%d') + '      '))
        #self.create_input1.delete(0, 'end')
        #self.create_input2.delete(0, 'end')
        self.create_input2.delete(0, 'end')
        self.create_input3.delete(0, 'end')
        self.create_input6.delete(0, 'end')
        self.create_input7.delete(0, 'end')


        pass

    def modify_timetable_search(self):
        self.option_list = self.del_list
        self.del_list = ''
        self.editAreaTable3.delete("1.0", END)

        course_id=[]
        day=[]
        time=[]
        room=[]

        cur = self.conn_fyp.cursor()
        cur.execute("select course_id from course_timetable where time_table_id = '" + str( self.option_list) + "'")

        for row in cur.fetchall():
            course_id.append(row)
        # print(str(first_name[0])[16:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select day from course_timetable where time_table_id = '" + str(self.option_list) + "'")

        for row in cur.fetchall():
            day.append(row)

        cur = self.conn_fyp.cursor()
        cur.execute("select time from course_timetable where time_table_id = '" + str(self.option_list) + "'")

        for row in cur.fetchall():
            time.append(row)

        cur = self.conn_fyp.cursor()
        cur.execute("select room from course_timetable where time_table_id = '" + str(self.option_list) + "'")

        for row in cur.fetchall():
            room.append(row)


        self.create_label1.config(text='Timetable ID:' + str( self.option_list))


        self.create_input2.delete(0, 'end')
        self.create_input3.delete(0, 'end')
        self.create_input6.delete(0, 'end')
        self.create_input7.delete(0, 'end')


        self.create_input2.insert(END, str(course_id[0])[14:-1])
        self.create_input3.insert(END, str(day[0])[9:-2])
        self.create_input6.insert(END, str(time[0])[10:-2])
        self.create_input7.insert(END, str(room[0])[10:-2])



        pass

    def modify_timetable(self):
        self.del_list=''
        self.left_frame.pack_forget()
        self.left_frame = Frame(self.root, background="black",
                                borderwidth=5, relief="ridge",
                                width=600)
        self.left_frame.pack(side="left",
                             fill="both",
                             expand="yes",
                             )

        self.middle_frame = Frame(self.root, width=20, background="black",
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

        self.create_title1 = tk.Label(self.frameL1, text="Modify Timetable", font=("Helvetica", 30),
                                      fg="white",
                                      background="black")
        self.create_title1.pack(side=tk.LEFT)

        self.create_title2 = tk.Label(self.frameL3, text="Please update the followings", font=("Helvetica", 10),
                                      fg="white",
                                      background="black")
        self.create_title2.pack(side=tk.LEFT)

        self.create_label1 = tk.Label(self.frameL4, text="Timetable ID: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label1.pack(side=tk.LEFT)


        self.create_label2 = tk.Label(self.frameL5, text="Course ID: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label2.pack(side=tk.LEFT)

        self.create_input2 = tk.Entry(self.frameL5, text="", background="white", width=80)
        self.create_input2.pack(side=tk.LEFT)



        self.create_label3 = tk.Label(self.frameL6, text="Day: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label3.pack(side=tk.LEFT)

        self.create_input3 = tk.Entry(self.frameL6, text="", background="white", width=80)
        self.create_input3.pack(side=tk.LEFT)



        self.create_label6 = tk.Label(self.frameL7, text="Time (24Hr): ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label6.pack(side=tk.LEFT)

        self.create_input6 = tk.Entry(self.frameL7, text="", background="white", width=80)
        self.create_input6.pack(side=tk.LEFT)

        self.create_label7 = tk.Label(self.frameL8, text="Room: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label7.pack(side=tk.LEFT)

        self.create_input7 = tk.Entry(self.frameL8, text="", background="white", width=80)
        self.create_input7.pack(side=tk.LEFT)




        self.create_submit = tk.Button(self.frameL9, text='Submit', font=("Helvetica", 20, "bold "), fg="white",
                                       bg="dark green",
                                       width=12, height=2, command=lambda: self.modify_timetable_update())
        self.create_submit.pack(side=tk.LEFT)

        self.btnTR1.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR2.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR3.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR4.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR5.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR6.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR7.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR8.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")

        self.btnBack.config(command=lambda: self.home_page("add_order"))
        self.btnHome.config(command=lambda: self.home_page("add_order"))

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

        self.editAreaTable2 = tkst.ScrolledText(self.frameM1, height=10, width=40, background="black", fg="white",
                                                font=("Helvetica", 15, "bold"))
        self.editAreaTable2.pack(fill="both", expand="yes", side="left")

        self.editAreaTable3 = tkst.ScrolledText(self.frameM2, height=2, width=40, background="black", fg="white",
                                                font=("Helvetica", 15, "bold"))
        self.editAreaTable3.pack(fill="both", expand="yes", side="left")

        tk.Button(self.frameM5, text="7", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("7")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="8", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("8")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="9", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("9")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="<[X]", font=("Helvetica", 20, "bold "), fg="white", bg="dark red", width=4,
                  height=2, command=lambda: self.del_page_editarea("del")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)

        tk.Button(self.frameM6, text="4", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("4")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="5", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("5")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="6", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("6")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)

        tk.Button(self.frameM7, text="1", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("1")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="2", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("2")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="3", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("3")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="0", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("0")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="Search", font=("Helvetica", 20, "bold "), fg="white", bg="dark green",
                  width=8, height=2, command=lambda: self.modify_timetable_search()).pack(
            side=tk.LEFT)

        self.editAreaTable2.insert(tk.INSERT, 'Input Timetable id to Search: ')

        self.staff_list_all()

        pass
        pass




    def view_timetable_search(self):

        option_list = self.del_list
        self.del_list = ''
        self.editAreaTable3.delete("1.0", END)

        course_name=[]
        staff_id = []
        time_table_id = []

        teacher_first_name=[]
        teacher_last_name = []
        student_first_name = []
        student_last_name=[]

        day=[]
        time=[]
        room=[]

        cur = self.conn_fyp.cursor()
        cur.execute("select course_name from course where course_id = '"+str(option_list)+"'")

        for row in cur.fetchall():
            course_name.append(row)
        #print(str(course_name[0])[17:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select staff_id from course where course_id = '"+str(option_list)+"'")

        for row in cur.fetchall():
            staff_id.append(row)
        #print(str(staff_id[0])[13:-1])

        cur = self.conn_fyp.cursor()
        cur.execute("select time_table_id  from course_timetable where course_id = '"+str(option_list)+"' order by day")

        for row in cur.fetchall():
            time_table_id.append(row)
        #print(str(time_table_id[0])[18:-1])

        cur = self.conn_fyp.cursor()
        cur.execute("select day  from course_timetable where course_id = '" + str(option_list) + "' order by day")

        for row in cur.fetchall():
            day.append(row)
        #print(str(day[0])[9:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select time  from course_timetable where course_id = '" + str(option_list) + "' order by day")

        for row in cur.fetchall():
            time.append(row)
        #print(str(time[0])[10:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select room  from course_timetable where course_id = '" + str(option_list) + "' order by day")

        for row in cur.fetchall():
            room.append(row)
        #print(str(room[0])[9:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select first_name from staff where staff_id = '" + str(staff_id[0])[13:-1] + "'")

        for row in cur.fetchall():
            teacher_first_name.append(row)
        #print(str(teacher_first_name[0])[16:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select last_name from staff where staff_id = '" + str(staff_id[0])[13:-1] + "'")

        for row in cur.fetchall():
            teacher_last_name.append(row)
        #print(str(teacher_last_name[0])[15:-2])




        self.editAreaTable.delete("1.0", END)
        self.editAreaTable.insert(tk.INSERT, 'Course id: ' + str(option_list) + '\n')
        self.editAreaTable.insert(tk.INSERT, 'Course name: ' + str(course_name[0])[17:-2] + '\n')
        self.editAreaTable.insert(tk.INSERT, 'Teacher name: ' + str(teacher_first_name[0])[16:-2]+' '+ str(teacher_last_name[0])[15:-2]+ '\n')
        self.editAreaTable.insert(tk.INSERT, 'Teacher staff id: ' + str(staff_id[0])[13:-1] + '\n\n\n')
        self.editAreaTable.insert(tk.INSERT, 'TImetable (id/day/time/room)\n')


        x = 0
        while x < len(time_table_id):
            self.editAreaTable.insert(tk.INSERT, str(time_table_id[x])[18:-1]+' '+str(day[x])[9:-2]+' '+str(time[x])[10:-2]+' '+str(room[x])[10:-2] + '\n')



            x += 1

        pass

    def view_timetable_all(self):
        self.editAreaTable.delete("1.0", END)
        option_list = self.del_list
        self.del_list = ''
        self.editAreaTable3.delete("1.0", END)

        course_name=[]
        staff_id = []
        student_id = []
        course_id=[]

        teacher_first_name=[]
        teacher_last_name = []
        student_first_name = []
        student_last_name=[]



        day = []
        time = []
        room = []


        if self.section == 2:
            cur = self.conn_fyp.cursor()
            cur.execute("select course_name from course where staff_id = '" + str(self.id) + "' order by course_name")

            for row in cur.fetchall():
                course_name.append(row)
            # print(str(course_name[0])[17:-2])

            cur = self.conn_fyp.cursor()
            cur.execute("select course_id from course where staff_id = '" +  str(self.id)+ "' order by course_name")

            for row in cur.fetchall():
                course_id.append(row)
            # print(str(course_id[0])[14:-1])

        elif self.section == 3:

            cur = self.conn_fyp.cursor()
            cur.execute(
                "select course.course_name from course inner join student_course on student_course.course_id = course.course_id where student_course.student_id = '" + str(
                    self.id) + "' order by course.course_name")

            for row in cur.fetchall():
                course_name.append(row)
            # print(str(course_name[0])[17:-2])

            cur = self.conn_fyp.cursor()
            cur.execute( "select course.course_id from course inner join student_course on student_course.course_id = course.course_id where student_course.student_id = '" + str(
                    self.id) + "' order by course.course_name")

            for row in cur.fetchall():
                course_id.append(row)
                # print(str(course_id[0])[14:-1])

        i=0
        while i<len(course_id):
            day = []
            time = []
            room = []
            time_table_id = []
            self.editAreaTable.insert(tk.INSERT, 'Course id: ' + str(course_id[i])[14:-1]+ '\n')
            self.editAreaTable.insert(tk.INSERT, 'Course name: ' + str(course_name[i])[17:-2] + '\n')
            self.editAreaTable.insert(tk.INSERT, 'TImetable (id/day/time/room)\n')
            cur = self.conn_fyp.cursor()
            cur.execute(
                "select time_table_id  from course_timetable where course_id = '" +str(course_id[i])[14:-1] + "' order by day")

            for row in cur.fetchall():
                time_table_id.append(row)
            # print(str(time_table_id[0])[18:-1])

            cur = self.conn_fyp.cursor()
            cur.execute("select day  from course_timetable where course_id = '" + str(course_id[i])[14:-1] + "' order by day")

            for row in cur.fetchall():
                day.append(row)
            # print(str(day[0])[9:-2])

            cur = self.conn_fyp.cursor()
            cur.execute("select time  from course_timetable where course_id = '" + str(course_id[i])[14:-1] + "' order by day")

            for row in cur.fetchall():
                time.append(row)
            # print(str(time[0])[10:-2])

            cur = self.conn_fyp.cursor()
            cur.execute("select room  from course_timetable where course_id = '" + str(course_id[i])[14:-1]+ "' order by day")

            for row in cur.fetchall():
                room.append(row)
            # print(str(room[0])[9:-2])

            x = 0
            while x < len(time_table_id):
                self.editAreaTable.insert(tk.INSERT,
                                              str(time_table_id[x])[18:-1] + ' ' + str(day[x])[9:-2] + ' ' + str(
                                                  time[x])[10:-2] + ' ' + str(room[x])[10:-2] + '\n')

                x += 1
            self.editAreaTable.insert(tk.INSERT, '\n\n\n')
            i+=1





        pass

    def view_timetable(self):
        self.del_list = ''

        self.left_frame.pack_forget()
        self.left_frame = Frame(self.root, background="black",
                                borderwidth=5, relief="ridge",
                                width=600)
        self.left_frame.pack(side="left",
                             fill="both",
                             expand="yes",
                             )

        self.middle_frame = Frame(self.root, width=20, background="black",
                                  borderwidth=5, relief="ridge",
                                  )
        self.middle_frame.pack(side="left",
                               fill="both",

                               )

        tk.Label(self.left_frame, bg='black', text='View Timetable',
                 font=("Helvetica", 20, "bold "), fg="white", borderwidth=5).pack()

        self.editAreaTable = tkst.ScrolledText(self.left_frame, height=8, width=69, background="black", fg="white",
                                               font=("Helvetica", 15, "bold"))
        self.editAreaTable.pack(fill="both", expand="yes", side="left")

        if self.section == 2 or self.section == 3:
            self.btnTR1.config(text="List All", font=("Helvetica", 20, "bold "), bg="grey20",
                               command=lambda: self.view_timetable_all())
        else:
            self.btnTR1.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR2.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR3.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR4.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR5.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR6.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR7.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR8.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")

        self.btnBack.config(command=lambda: self.home_page("add_order"))
        self.btnHome.config(command=lambda: self.home_page("add_order"))

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

        self.editAreaTable2 = tkst.ScrolledText(self.frameM1, height=10, width=40, background="black", fg="white",
                                                font=("Helvetica", 15, "bold"))
        self.editAreaTable2.pack(fill="both", expand="yes", side="left")

        self.editAreaTable3 = tkst.ScrolledText(self.frameM2, height=2, width=40, background="black", fg="white",
                                                font=("Helvetica", 15, "bold"))
        self.editAreaTable3.pack(fill="both", expand="yes", side="left")

        tk.Button(self.frameM5, text="7", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("7")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="8", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("8")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="9", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("9")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="<[X]", font=("Helvetica", 20, "bold "), fg="white", bg="dark red", width=4,
                  height=2, command=lambda: self.del_page_editarea("del")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)

        tk.Button(self.frameM6, text="4", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("4")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="5", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("5")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="6", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("6")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)

        tk.Button(self.frameM7, text="1", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("1")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="2", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("2")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="3", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("3")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="0", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("0")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="Search", font=("Helvetica", 20, "bold "), fg="white", bg="dark green",
                  width=8, height=2, command=lambda: self.view_timetable_search()).pack(
            side=tk.LEFT)

        self.editAreaTable2.insert(tk.INSERT, 'Input Course id to Search: ')

        if self.section == 2 or self.section == 3:
            self.view_timetable_all()

        pass




    def view_attendence_search(self):

        option_list = self.del_list
        self.del_list = ''
        self.editAreaTable3.delete("1.0", END)


        course_id=[]
        course_name=[]
        staff_id = []
        time_table_id = []

        teacher_first_name=[]
        teacher_last_name = []


        day=[]
        time=[]
        room=[]

        cur = self.conn_fyp.cursor()
        cur.execute("select course_id from course_timetable where time_table_id = '" + str(option_list) + "'")

        for row in cur.fetchall():
            course_id.append(row)
        #print(str(course_id[0])[14:-1])

        cur = self.conn_fyp.cursor()
        cur.execute("select course_name from course where course_id = '"+str(course_id[0])[14:-1]+"'")

        for row in cur.fetchall():
            course_name.append(row)
        #print(str(course_name[0])[17:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select staff_id from course where course_id = '"+str(course_id[0])[14:-1]+"'")

        for row in cur.fetchall():
            staff_id.append(row)
        #print(str(staff_id[0])[13:-1])



        cur = self.conn_fyp.cursor()
        cur.execute("select day  from course_timetable where time_table_id = '" + str(option_list) + "' order by day")

        for row in cur.fetchall():
            day.append(row)
        #print(str(day[0])[9:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select time  from course_timetable where time_table_id = '" + str(option_list) + "' order by day")

        for row in cur.fetchall():
            time.append(row)
        #print(str(time[0])[10:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select room  from course_timetable where time_table_id = '" +str(option_list) + "' order by day")

        for row in cur.fetchall():
            room.append(row)
        #print(str(room[0])[9:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select first_name from staff where staff_id = '" + str(staff_id[0])[13:-1] + "'")

        for row in cur.fetchall():
            teacher_first_name.append(row)
        #print(str(teacher_first_name[0])[16:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select last_name from staff where staff_id = '" + str(staff_id[0])[13:-1] + "'")

        for row in cur.fetchall():
            teacher_last_name.append(row)
        #print(str(teacher_last_name[0])[15:-2])




        self.editAreaTable.delete("1.0", END)
        self.editAreaTable.insert(tk.INSERT, 'Timetable id: ' + str(option_list) + '\n')
        self.editAreaTable.insert(tk.INSERT, 'Course id: ' + str(course_id[0])[14:-1] + '\n')
        self.editAreaTable.insert(tk.INSERT, 'Course name: ' + str(course_name[0])[17:-2] + '\n')
        self.editAreaTable.insert(tk.INSERT, 'Teacher name: ' + str(teacher_first_name[0])[16:-2]+' '+ str(teacher_last_name[0])[15:-2]+ '\n')
        self.editAreaTable.insert(tk.INSERT, 'Teacher staff id: ' + str(staff_id[0])[13:-1] + '\n')
        self.editAreaTable.insert(tk.INSERT, str(day[0])[9:-2] + ' ' + str(time[0])[10:-2] + ' room' + str(room[0])[10:-2] + '\n\n\n')

        self.editAreaTable.insert(tk.INSERT, 'Student List (ID/name/attendence)\n')



        student_id=[]
        student_first_name=[]
        student_last_name = []
        student_attendence=[]
        student_attendence_flag = []

        cur = self.conn_fyp.cursor()
        cur.execute("select student_course.student_id from student_course inner join course_timetable on student_course.course_id = course_timetable.course_id where course_timetable.time_table_id = '"+ str(option_list)+"' order by student_course.student_id")

        for row in cur.fetchall():
            student_id.append(row)
        print(str(student_id[0])[15:-1])

        y=0
        while y < len(student_id):
            cur = self.conn_fyp.cursor()
            cur.execute("select first_name from student where student_id = '" +str(student_id[y])[15:-1]+"'")

            for row in cur.fetchall():
                student_first_name.append(row)
            #print(str(student_first_name[0])[16:-2])

            cur = self.conn_fyp.cursor()
            cur.execute("select last_name from student where student_id = '" + str(student_id[y])[15:-1] + "'")

            for row in cur.fetchall():
                student_last_name.append(row)
            #print(str(student_last_name[0])[15:-2])

            student_attendence = []
            cur = self.conn_fyp.cursor()
            cur.execute("select Login_date from login_record where student_id = '" + str(student_id[y])[15:-1] + "' and time_table_id = '"+str(option_list)+"'")

            for row in cur.fetchall():
                student_attendence.append(row)
            #print((str(student_attendence[0])[16:-2]))
            if student_attendence != []:
                student_attendence_flag.append((str(student_attendence[0])[16:-2]))
            else:
                student_attendence_flag.append("No record")
            #print(str(student_last_name[0])[15:-1])

            y+=1


        x=0
        while x < len(student_id):
            self.editAreaTable.insert(tk.INSERT,str(student_id[x])[15:-1]+"  "+str(student_first_name[x])[16:-2] + ' ' + str(student_last_name[x])[15:-2] +":      " +str(student_attendence_flag[x])+'\n')
            x+=1
        pass

    def view_attendence_all(self):
        self.editAreaTable.delete("1.0", END)
        option_list = self.del_list
        self.del_list = ''
        self.editAreaTable3.delete("1.0", END)

        course_name=[]
        staff_id = []
        student_id = []
        course_id=[]

        teacher_first_name=[]
        teacher_last_name = []
        student_first_name = []
        student_last_name=[]



        day = []
        time = []
        room = []

        time_table_id=[]

        if self.section == 2:
            cur = self.conn_fyp.cursor()
            cur.execute(
                "SELECT course_timetable.time_table_id from course_timetable inner join course on course.course_id = course_timetable.course_id where course.staff_id = '" + str(
                    self.id) + "' order by course.course_name")
            for row in cur.fetchall():
                time_table_id.append(row)
            print(str(time_table_id[0])[18:-1])

            x=0
            while x< len(time_table_id):
                cur = self.conn_fyp.cursor()
                cur.execute("select course_id from course_timetable where time_table_id = '" +str(time_table_id[x])[18:-1]+"'")

                for row in cur.fetchall():
                    course_id.append(row)
                # print(str(course_id[0])[14:-1])

                cur = self.conn_fyp.cursor()
                cur.execute(
                    "select course_name from course where course_id = '" + str(course_id[x])[14:-1]+"'" )

                for row in cur.fetchall():
                    course_name.append(row)
                    # print(str(course_name[0])[17:-2])

                x+=1





        elif self.section == 3:

            cur = self.conn_fyp.cursor()
            cur.execute(
                "select course.course_name from course inner join student_course on student_course.course_id = course.course_id where student_course.student_id = '" + str(
                    self.id) + "' order by course.course_name")

            for row in cur.fetchall():
                course_name.append(row)
            # print(str(course_name[0])[17:-2])

            cur = self.conn_fyp.cursor()
            cur.execute( "select course.course_id from course inner join student_course on student_course.course_id = course.course_id where student_course.student_id = '" + str(
                    self.id) + "' order by course.course_name and course_timetable.timetable_id")

            for row in cur.fetchall():
                course_id.append(row)
                # print(str(course_id[0])[14:-1])

        i=0
        while i<len(time_table_id):
            day = []
            time = []
            room = []

            self.editAreaTable.insert(tk.INSERT, 'Timetable ID: ' +str(time_table_id[i])[18:-1] + '\n')
            self.editAreaTable.insert(tk.INSERT, 'Course ID: ' + str(course_id[i])[14:-1]+ '\n')
            self.editAreaTable.insert(tk.INSERT, 'Course name: ' + str(course_name[i])[17:-2] + '\n')

            print(str(time_table_id[i])[18:-1])

            cur = self.conn_fyp.cursor()
            cur.execute(
                "select day  from course_timetable where time_table_id = '" + str(time_table_id[i])[18:-1] +"'")

            for row in cur.fetchall():
                day.append(row)
            # print(str(day[0])[9:-2])

            cur = self.conn_fyp.cursor()
            cur.execute(
                "select time  from course_timetable where time_table_id = '" +str(time_table_id[i])[18:-1]+"'")

            for row in cur.fetchall():
                time.append(row)
            # print(str(time[0])[10:-2])

            cur = self.conn_fyp.cursor()
            cur.execute(
                "select room  from course_timetable where time_table_id = '" + str(time_table_id[i])[18:-1]+"'" )

            for row in cur.fetchall():
                room.append(row)
            # print(str(room[0])[9:-2])



            self.editAreaTable.insert(tk.INSERT, str(day[0])[9:-2] + ' ' + str(time[0])[10:-2] + ' room' + str(room[0])[
                                                                                                           10:-2] + '\n')

            self.editAreaTable.insert(tk.INSERT, 'Student List (ID/name/attendence)\n')

            student_id = []
            student_first_name = []
            student_last_name = []
            student_attendence = []
            student_attendence_flag = []

            cur = self.conn_fyp.cursor()
            cur.execute(
                "select student_course.student_id from student_course inner join course_timetable on student_course.course_id = course_timetable.course_id where course_timetable.time_table_id = '" + str(time_table_id[i])[18:-1] + "' order by student_course.student_id")

            for row in cur.fetchall():
                student_id.append(row)
            #print(str(student_id[0])[15:-1])

            y = 0
            while y < len(student_id):
                cur = self.conn_fyp.cursor()
                cur.execute("select first_name from student where student_id = '" + str(student_id[y])[15:-1] + "'")

                for row in cur.fetchall():
                    student_first_name.append(row)
                # print(str(student_first_name[0])[16:-2])

                cur = self.conn_fyp.cursor()
                cur.execute("select last_name from student where student_id = '" + str(student_id[y])[15:-1] + "'")

                for row in cur.fetchall():
                    student_last_name.append(row)
                # print(str(student_last_name[0])[15:-2])

                student_attendence = []
                cur = self.conn_fyp.cursor()
                cur.execute("select Login_date from login_record where student_id = '" + str(student_id[y])[15:-1] + "' and time_table_id = '" + str(time_table_id[i])[18:-1] + "'")

                for row in cur.fetchall():
                    student_attendence.append(row)
                # print((str(student_attendence[0])[16:-2]))
                if student_attendence != []:
                    student_attendence_flag.append((str(student_attendence[0])[16:-2]))
                else:
                    student_attendence_flag.append("No record")
                # print(str(student_last_name[0])[15:-1])

                y += 1

            x = 0
            while x < len(student_id):
                self.editAreaTable.insert(tk.INSERT, str(student_id[x])[15:-1] + "  " + str(student_first_name[x])[
                                                                                        16:-2] + ' ' + str(
                    student_last_name[x])[15:-2] + ":      " + str(student_attendence_flag[x]) + '\n')
                x += 1
            self.editAreaTable.insert(tk.INSERT, '\n\n\n')
            i+=1





        pass

    def view_attendence(self):
        self.del_list = ''

        self.left_frame.pack_forget()
        self.left_frame = Frame(self.root, background="black",
                                borderwidth=5, relief="ridge",
                                width=600)
        self.left_frame.pack(side="left",
                             fill="both",
                             expand="yes",
                             )

        self.middle_frame = Frame(self.root, width=20, background="black",
                                  borderwidth=5, relief="ridge",
                                  )
        self.middle_frame.pack(side="left",
                               fill="both",

                               )

        tk.Label(self.left_frame, bg='black', text='View Attendence',
                 font=("Helvetica", 20, "bold "), fg="white", borderwidth=5).pack()

        self.editAreaTable = tkst.ScrolledText(self.left_frame, height=8, width=69, background="black", fg="white",
                                               font=("Helvetica", 15, "bold"))
        self.editAreaTable.pack(fill="both", expand="yes", side="left")


        if self.section == 2 or self.section ==3:
            self.btnTR1.config(text="List All", font=("Helvetica", 20, "bold "), bg="grey20", command=lambda :self.view_attendence_all())
            self.btnTR2.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        else:
            self.btnTR1.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
            self.btnTR2.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR3.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR4.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR5.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR6.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR7.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR8.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")

        self.btnBack.config(command=lambda: self.home_page("add_order"))
        self.btnHome.config(command=lambda: self.home_page("add_order"))

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

        self.editAreaTable2 = tkst.ScrolledText(self.frameM1, height=10, width=40, background="black", fg="white",
                                                font=("Helvetica", 15, "bold"))
        self.editAreaTable2.pack(fill="both", expand="yes", side="left")

        self.editAreaTable3 = tkst.ScrolledText(self.frameM2, height=2, width=40, background="black", fg="white",
                                                font=("Helvetica", 15, "bold"))
        self.editAreaTable3.pack(fill="both", expand="yes", side="left")

        tk.Button(self.frameM5, text="7", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("7")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="8", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("8")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="9", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("9")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="<[X]", font=("Helvetica", 20, "bold "), fg="white", bg="dark red", width=4,
                  height=2, command=lambda: self.del_page_editarea("del")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)

        tk.Button(self.frameM6, text="4", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("4")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="5", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("5")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="6", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("6")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)

        tk.Button(self.frameM7, text="1", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("1")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="2", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("2")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="3", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("3")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="0", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("0")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="Search", font=("Helvetica", 20, "bold "), fg="white", bg="dark green",
                  width=8, height=2, command=lambda: self.view_attendence_search()).pack(
            side=tk.LEFT)

        self.editAreaTable2.insert(tk.INSERT, 'Input Timetable id to Search: ')

        if self.section ==2 or self.section ==3:
            self.view_attendence_all()

        pass



    def view_course_member_search_id(self):

        option_list = self.del_list
        self.del_list = ''
        self.editAreaTable3.delete("1.0", END)

        course_name=[]
        staff_id = []
        student_id = []

        teacher_first_name=[]
        teacher_last_name = []
        student_first_name = []
        student_last_name=[]

        cur = self.conn_fyp.cursor()
        cur.execute("select course_name from course where course_id = '"+str(option_list)+"'")

        for row in cur.fetchall():
            course_name.append(row)
        #print(str(course_name[0])[17:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select staff_id from course where course_id = '"+str(option_list)+"'")

        for row in cur.fetchall():
            staff_id.append(row)
        #print(str(staff_id[0])[13:-1])

        cur = self.conn_fyp.cursor()
        cur.execute("select student_course.student_id from student_course inner join student on student_course.student_id = student.student_id where student_course.course_id = '"+str(option_list)+"'  order by student.last_name")

        for row in cur.fetchall():
            student_id.append(row)
        print(str(student_id[0])[15:-1])



        cur = self.conn_fyp.cursor()
        cur.execute("select first_name from staff where staff_id = '" + str(staff_id[0])[13:-1] + "'")

        for row in cur.fetchall():
            teacher_first_name.append(row)
        print(str(teacher_first_name[0])[16:-2])

        cur = self.conn_fyp.cursor()
        cur.execute("select last_name from staff where staff_id = '" + str(staff_id[0])[13:-1] + "'")

        for row in cur.fetchall():
            teacher_last_name.append(row)
        print(str(teacher_last_name[0])[15:-2])






        self.editAreaTable.delete("1.0", END)
        self.editAreaTable.insert(tk.INSERT, 'Course id: ' + str(option_list) + '\n')
        self.editAreaTable.insert(tk.INSERT, 'Course name: ' + str(course_name[0])[17:-2] + '\n')
        self.editAreaTable.insert(tk.INSERT, 'Teacher name: ' + str(teacher_first_name[0])[16:-2]+' '+ str(teacher_last_name[0])[15:-2]+ '\n')
        self.editAreaTable.insert(tk.INSERT, 'Teacher staff id: ' + str(staff_id[0])[13:-1] + '\n\n\n')
        self.editAreaTable.insert(tk.INSERT, 'Student list (id/name)\n')

        y=0
        while y < len(student_id):
            cur = self.conn_fyp.cursor()
            cur.execute("select first_name from student where student_id = '" + str(student_id[y])[15:-1] + "'")

            for row in cur.fetchall():
                student_first_name.append(row)
            #print(str(student_first_name[0])[16:-2])

            cur = self.conn_fyp.cursor()
            cur.execute("select last_name from student where student_id = '" + str(student_id[y])[15:-1] + "'")

            for row in cur.fetchall():
                student_last_name.append(row)
            #print(str(student_last_name[0])[15:-2])

            y+=1


        x = 0
        while x < len(student_id):
            self.editAreaTable.insert(tk.INSERT, str(student_id[x])[15:-1]+' '+str(student_first_name[x])[16:-2]+' '+str(student_last_name[x])[15:-2] + '\n')



            x += 1

        pass

    def view_course_member_all(self):
        self.editAreaTable.delete("1.0", END)
        option_list = self.del_list
        self.del_list = ''
        self.editAreaTable3.delete("1.0", END)

        course_name=[]
        staff_id = []
        student_id = []
        course_id=[]

        teacher_first_name=[]
        teacher_last_name = []
        student_first_name = []
        student_last_name=[]


        if self.section == 2:
            cur = self.conn_fyp.cursor()
            cur.execute("select course_name from course where staff_id = '"+str(self.id)+"' order by course_id")

            for row in cur.fetchall():
                course_name.append(row)
            #print(str(course_name[0])[17:-2])



            cur = self.conn_fyp.cursor()
            cur.execute("select course_id from course where staff_id = '"+str(self.id)+"' order by course_id")

            for row in cur.fetchall():
                course_id.append(row)
            #print(str(course_id[0])[14:-1])

        elif self.section == 3:

            cur = self.conn_fyp.cursor()
            cur.execute("select course_id from student_course where student_id = '" + str(self.id) + "' order by course_id")

            for row in cur.fetchall():
                course_id.append(row)
            #print(str(course_id[0])[14:-1])

            x=0
            while x<len(course_id):
                cur = self.conn_fyp.cursor()
                cur.execute("select course_name from course where course_id = '" + str(course_id[x])[14:-1] + "'")

                for row in cur.fetchall():
                    course_name.append(row)
                #print(str(course_name[0])[17:-2])

                cur = self.conn_fyp.cursor()
                cur.execute("select staff_id from course where course_id = '" + str(course_id[x])[14:-1] + "'")

                for row in cur.fetchall():
                    staff_id.append(row)
                    #print(str(staff_id[0])[13:-1])

                cur = self.conn_fyp.cursor()
                cur.execute("select first_name from staff where staff_id = '" + str(staff_id[x])[13:-1] + "'")

                for row in cur.fetchall():
                    teacher_first_name.append(row)
                #print(str(teacher_first_name[0])[16:-2])

                cur = self.conn_fyp.cursor()
                cur.execute("select last_name from staff where staff_id = '" + str(staff_id[x])[13:-1] + "'")

                for row in cur.fetchall():
                    teacher_last_name.append(row)
                #print(str(teacher_last_name[0])[15:-2])


                x+=1


        i=0
        while i<len(course_id):
            #print(i)

            self.editAreaTable.insert(tk.INSERT, 'Course id: ' + str(course_id[i])[14:-1] + '\n')


            if self.section==2:
                self.editAreaTable.insert(tk.INSERT, 'Course name: ' + str(course_name[i])[17:-2] + '\n\n')
            elif self.section==3:
                self.editAreaTable.insert(tk.INSERT, 'Course name: ' + str(course_name[i])[17:-2] + '\n')
                self.editAreaTable.insert(tk.INSERT, 'Staff ID: ' + str(staff_id[i])[13:-1]+ '\n')
                self.editAreaTable.insert(tk.INSERT, 'Teacher name: ' + str(teacher_first_name[i])[16:-2]+" "+str(teacher_last_name[i])[15:-2] + '\n')

            self.editAreaTable.insert(tk.INSERT, 'Student list (id/name)\n')
            cur = self.conn_fyp.cursor()
            student_id=[]
            cur.execute("select student_course.student_id from student_course inner join student on student_course.student_id = student.student_id where student_course.course_id = '"+str(course_id[i])[14:-1]+"'  order by student.last_name")

            for row in cur.fetchall():
                student_id.append(row)
            #print(str(student_id[0])[15:-1])

            y=0
            while y<len(student_id):
                student_first_name=[]
                student_last_name=[]
                cur = self.conn_fyp.cursor()
                cur.execute("select first_name from student where student_id = '" + str(student_id[y])[15:-1] + "'")

                for row in cur.fetchall():
                    student_first_name.append(row)
                # print(str(student_first_name[0])[16:-2])

                cur = self.conn_fyp.cursor()
                cur.execute("select last_name from student where student_id = '" + str(student_id[y])[15:-1] + "'")

                for row in cur.fetchall():
                    student_last_name.append(row)
                # print(str(student_last_name[0])[15:-2])

                self.editAreaTable.insert(tk.INSERT, str(student_id[y])[15:-1] + ' ' + str(student_first_name[0])[
                                                                                       16:-2] + ' ' + str(
                    student_last_name[0])[15:-2] + '\n')

                y += 1
            self.editAreaTable.insert(tk.INSERT,  '\n\n\n')

            i+=1

        '''

        self.editAreaTable.delete("1.0", END)
        self.editAreaTable.insert(tk.INSERT, 'Course id: ' + str(option_list) + '\n')
        self.editAreaTable.insert(tk.INSERT, 'Course name: ' + str(course_name[0])[17:-2] + '\n')
        self.editAreaTable.insert(tk.INSERT, 'Teacher name: ' + str(teacher_first_name[0])[16:-2]+' '+ str(teacher_last_name[0])[15:-2]+ '\n')
        self.editAreaTable.insert(tk.INSERT, 'Teacher staff id: ' + str(staff_id[0])[13:-1] + '\n\n\n')
        self.editAreaTable.insert(tk.INSERT, 'Student list (id/name)\n')

        y=0
        while y < len(student_id):
            cur = self.conn_fyp.cursor()
            cur.execute("select first_name from student where student_id = '" + str(student_id[y])[15:-1] + "'")

            for row in cur.fetchall():
                student_first_name.append(row)
            #print(str(student_first_name[0])[16:-2])

            cur = self.conn_fyp.cursor()
            cur.execute("select last_name from student where student_id = '" + str(student_id[y])[15:-1] + "'")

            for row in cur.fetchall():
                student_last_name.append(row)
            #print(str(student_last_name[0])[15:-2])

            y+=1


        x = 0
        while x < len(student_id):
            self.editAreaTable.insert(tk.INSERT, str(student_id[x])[15:-1]+' '+str(student_first_name[x])[16:-2]+' '+str(student_last_name[x])[15:-2] + '\n')



            x += 1
        '''
        pass

    def view_course_member(self):
        self.del_list = ''

        self.left_frame.pack_forget()
        self.left_frame = Frame(self.root, background="black",
                                borderwidth=5, relief="ridge",
                                width=600)
        self.left_frame.pack(side="left",
                             fill="both",
                             expand="yes",
                             )

        self.middle_frame = Frame(self.root, width=20, background="black",
                                  borderwidth=5, relief="ridge",
                                  )
        self.middle_frame.pack(side="left",
                               fill="both",

                               )

        tk.Label(self.left_frame, bg='black', text='View Course Member',
                 font=("Helvetica", 20, "bold "), fg="white", borderwidth=5).pack()

        self.editAreaTable = tkst.ScrolledText(self.left_frame, height=8, width=69, background="black", fg="white",
                                               font=("Helvetica", 15, "bold"))
        self.editAreaTable.pack(fill="both", expand="yes", side="left")

        if self.section == 2 or self.section == 3:
            self.btnTR1.config(text="List All", font=("Helvetica", 20, "bold "), bg="grey20",
                               command=lambda: self.view_course_member_all())
        else:
            self.btnTR1.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR2.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR3.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR4.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR5.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR6.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR7.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR8.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")

        self.btnBack.config(command=lambda: self.home_page("add_order"))
        self.btnHome.config(command=lambda: self.home_page("add_order"))

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

        self.editAreaTable2 = tkst.ScrolledText(self.frameM1, height=10, width=40, background="black", fg="white",
                                                font=("Helvetica", 15, "bold"))
        self.editAreaTable2.pack(fill="both", expand="yes", side="left")

        self.editAreaTable3 = tkst.ScrolledText(self.frameM2, height=2, width=40, background="black", fg="white",
                                                font=("Helvetica", 15, "bold"))
        self.editAreaTable3.pack(fill="both", expand="yes", side="left")

        tk.Button(self.frameM5, text="7", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("7")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="8", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("8")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="9", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("9")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="<[X]", font=("Helvetica", 20, "bold "), fg="white", bg="dark red", width=4,
                  height=2, command=lambda: self.del_page_editarea("del")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM5, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)

        tk.Button(self.frameM6, text="4", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("4")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="5", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("5")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="6", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("6")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM6, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)

        tk.Button(self.frameM7, text="1", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("1")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="2", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("2")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="3", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("3")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM7, text="", font=("Helvetica", 20, "bold "), fg="white", bg="grey20", width=4, height=2,
                  command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="0", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command=lambda: self.del_page_editarea("0")).pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="", font=("Helvetica", 20, "bold "), fg="white", bg="slate blue", width=4,
                  height=2, command='').pack(
            side=tk.LEFT)
        tk.Button(self.frameM8, text="Search", font=("Helvetica", 20, "bold "), fg="white", bg="dark green",
                  width=8, height=2, command=lambda: self.view_course_member_search_id()).pack(
            side=tk.LEFT)

        self.editAreaTable2.insert(tk.INSERT, 'Input Course id to Search: ')

        if self.section==2 or self.section==3:
            self.view_course_member_all()

        pass


    def add_staff_receive(self):
        str_birth = str(self.create_input4.get()) + '-' + str(self.create_input5.get()) + '-' + str(
            self.create_input6.get())

        cur = self.conn_fyp.cursor()
        with self.conn_fyp.cursor() as cur:
            cur.execute(
                "INSERT INTO staff(first_name, last_name,  sex, date_of_birth,position,password) VALUES ('" + str(
                    self.create_input1.get()) + "','" + str(self.create_input2.get()) + "','" + str(
                    self.create_input3.get()) + "','" + str(str_birth) + "','"+str(self.create_input7.get())+"','N')")
            self.conn_fyp.commit()

        self.date_label.config(
            text=str(self.user_name[0])[15:-2] + "      Staff " + self.create_input2.get() + ":Added      " + str(
                self.date.strftime('%Y/%m/%d') + '      '))

        self.create_input1.delete(0, 'end')
        self.create_input2.delete(0, 'end')
        self.create_input3.delete(0, 'end')
        self.create_input4.delete(0, 'end')
        self.create_input5.delete(0, 'end')
        self.create_input6.delete(0, 'end')
        self.create_input7.delete(0, 'end')

        pass

    def add_staff(self):

        self.left_frame.pack_forget()
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
        self.frameL11 = tk.Frame(self.left_frame)
        self.frameL11.pack()

        self.create_title1 = tk.Label(self.frameL1, text="New Staff", font=("Helvetica", 30),
                                      fg="white",
                                      background="black")
        self.create_title1.pack(side=tk.LEFT)

        self.create_title2 = tk.Label(self.frameL3, text="Please input the followings", font=("Helvetica", 10),
                                      fg="white",
                                      background="black")
        self.create_title2.pack(side=tk.LEFT)

        self.create_label1 = tk.Label(self.frameL4, text="First Name: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label1.pack(side=tk.LEFT)

        self.create_input1 = tk.Entry(self.frameL4, text="", background="white", width=100)
        self.create_input1.pack(side=tk.LEFT)

        self.create_label2 = tk.Label(self.frameL5, text="Last Name: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label2.pack(side=tk.LEFT)

        self.create_input2 = tk.Entry(self.frameL5, text="", background="white", width=100)
        self.create_input2.pack(side=tk.LEFT)

        self.create_label3 = tk.Label(self.frameL6, text="Sex (M/F): ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label3.pack(side=tk.LEFT)

        self.create_input3 = tk.Entry(self.frameL6, text="", background="white", width=100)
        self.create_input3.pack(side=tk.LEFT)

        self.create_label4 = tk.Label(self.frameL7, text="Date of Birth (Date): ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label4.pack(side=tk.LEFT)

        self.create_input4 = tk.Entry(self.frameL7, text="", background="white", width=100)
        self.create_input4.pack(side=tk.LEFT)

        self.create_label5 = tk.Label(self.frameL8, text="Date of Birth (Month): ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label5.pack(side=tk.LEFT)

        self.create_input5 = tk.Entry(self.frameL8, text="", background="white", width=100)
        self.create_input5.pack(side=tk.LEFT)

        self.create_label6 = tk.Label(self.frameL9, text="Date of Birth (Year): ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label6.pack(side=tk.LEFT)

        self.create_input6 = tk.Entry(self.frameL9, text="", background="white", width=100)
        self.create_input6.pack(side=tk.LEFT)

        self.create_label7 = tk.Label(self.frameL10, text="Position: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label7.pack(side=tk.LEFT)

        self.create_input7 = tk.Entry(self.frameL10, text="", background="white", width=100)
        self.create_input7.pack(side=tk.LEFT)

        self.create_submit = tk.Button(self.frameL11, text='Submit', font=("Helvetica", 20, "bold "), fg="white",
                                       bg="dark green",
                                       width=12, height=2, command=lambda: self.add_staff_receive())
        self.create_submit.pack(side=tk.LEFT)
        self.btnHome.config(command=lambda: self.home_page("table_sub"))
        pass

    def add_student_receive(self):
        str_birth=str(self.create_input4.get())+'-'+str(self.create_input5.get())+'-'+str(self.create_input6.get())

        cur = self.conn_fyp.cursor()
        with self.conn_fyp.cursor() as cur:
            cur.execute(
                "INSERT INTO student(first_name, last_name,  sex, date_of_birth,face_cap,face_train) VALUES ('" + str(
                    self.create_input1.get()) + "','" + str(self.create_input2.get()) + "','" + str(
                    self.create_input3.get()) + "','" + str(str_birth) +  "','N','N')")
            self.conn_fyp.commit()

        self.date_label.config(
            text=str(self.user_name[0])[15:-2] + "      Student " + self.create_input2.get() + ":Added      " + str(
                self.date.strftime('%Y/%m/%d') + '      '))

        self.create_input1.delete(0, 'end')
        self.create_input2.delete(0, 'end')
        self.create_input3.delete(0, 'end')
        self.create_input4.delete(0, 'end')
        self.create_input5.delete(0, 'end')
        self.create_input6.delete(0, 'end')




        pass

    def add_student(self):

        self.left_frame.pack_forget()
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
        self.frameL11 = tk.Frame(self.left_frame)
        self.frameL11.pack()

        self.create_title1 = tk.Label(self.frameL1, text="New Student", font=("Helvetica", 30),
                                      fg="white",
                                      background="black")
        self.create_title1.pack(side=tk.LEFT)

        self.create_title2 = tk.Label(self.frameL3, text="Please input the followings", font=("Helvetica", 10),
                                     fg="white",
                                     background="black")
        self.create_title2.pack(side=tk.LEFT)

        self.create_label1 = tk.Label(self.frameL4, text="First Name: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label1.pack(side=tk.LEFT)

        self.create_input1 = tk.Entry(self.frameL4, text="", background="white", width=100)
        self.create_input1.pack(side=tk.LEFT)

        self.create_label2 = tk.Label(self.frameL5, text="Last Name: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label2.pack(side=tk.LEFT)

        self.create_input2 = tk.Entry(self.frameL5, text="", background="white", width=100)
        self.create_input2.pack(side=tk.LEFT)

        self.create_label3 = tk.Label(self.frameL6, text="Sex (M/F): ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label3.pack(side=tk.LEFT)

        self.create_input3 = tk.Entry(self.frameL6, text="", background="white", width=100)
        self.create_input3.pack(side=tk.LEFT)

        self.create_label4 = tk.Label(self.frameL7, text="Date of Birth (Date): ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label4.pack(side=tk.LEFT)

        self.create_input4 = tk.Entry(self.frameL7, text="", background="white", width=100)
        self.create_input4.pack(side=tk.LEFT)

        self.create_label5 = tk.Label(self.frameL8, text="Date of Birth (Month): ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label5.pack(side=tk.LEFT)

        self.create_input5 = tk.Entry(self.frameL8, text="", background="white", width=100)
        self.create_input5.pack(side=tk.LEFT)

        self.create_label6 = tk.Label(self.frameL9, text="Date of Birth (Year): ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label6.pack(side=tk.LEFT)

        self.create_input6 = tk.Entry(self.frameL9, text="", background="white", width=100)
        self.create_input6.pack(side=tk.LEFT)


        self.create_submit = tk.Button(self.frameL10, text='Submit', font=("Helvetica", 20, "bold "), fg="white",
                                       bg="dark green",
                                       width=12, height=2, command=lambda: self.add_student_receive())
        self.create_submit.pack(side=tk.LEFT)
        self.btnHome.config(command=lambda: self.home_page("table_sub"))
        pass





    def add_course_receive(self):

        cur = self.conn_fyp.cursor()
        with self.conn_fyp.cursor() as cur:
            cur.execute(
                "INSERT INTO course(course_name, staff_id) VALUES ('" + str(
                    self.create_input1.get()) + "','" + str(self.create_input2.get()) + "')" )
            self.conn_fyp.commit()

        self.date_label.config(
            text=str(self.user_name[0])[15:-2] + "      Course " + self.create_input1.get() + ":Added      " + str(
                self.date.strftime('%Y/%m/%d') + '      '))

        self.create_input1.delete(0, 'end')
        self.create_input2.delete(0, 'end')





        pass

    def add_course(self):

        self.left_frame.pack_forget()
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
        self.frameL11 = tk.Frame(self.left_frame)
        self.frameL11.pack()

        self.create_title1 = tk.Label(self.frameL1, text="New Course", font=("Helvetica", 30),
                                      fg="white",
                                      background="black")
        self.create_title1.pack(side=tk.LEFT)

        self.create_title2 = tk.Label(self.frameL3, text="Please input the followings", font=("Helvetica", 10),
                                     fg="white",
                                     background="black")
        self.create_title2.pack(side=tk.LEFT)

        self.create_label1 = tk.Label(self.frameL4, text="Course Name: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label1.pack(side=tk.LEFT)

        self.create_input1 = tk.Entry(self.frameL4, text="", background="white", width=100)
        self.create_input1.pack(side=tk.LEFT)

        self.create_label2 = tk.Label(self.frameL5, text="Staff ID: ", font=("Helvetica", 20), fg="white",
                                      background="black")
        self.create_label2.pack(side=tk.LEFT)

        self.create_input2 = tk.Entry(self.frameL5, text="", background="white", width=100)
        self.create_input2.pack(side=tk.LEFT)



        self.create_submit = tk.Button(self.frameL6, text='Submit', font=("Helvetica", 20, "bold "), fg="white",
                                       bg="dark green",
                                       width=12, height=2, command=lambda: self.add_course_receive())
        self.create_submit.pack(side=tk.LEFT)
        self.btnHome.config(command=lambda: self.home_page("table_sub"))
        pass



    def add_reco_template(self,page):
        '''
        when button clicked
        '''
        self.add_list = ''
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
                                               font=("Helvetica", 15, "bold"))
        self.editAreaTable.pack(fill="both", expand="yes", side="left")

        self.editAreaTable.insert(tk.INSERT, "")

        self.editAreaTable2 = tkst.ScrolledText(self.frameM2, height=2, width=40, background="black", fg="white",
                                                font=("Helvetica", 15, "bold"))
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


    def face_train(self):
        print('list'+str(self.add_list))

        first_name = []
        cur_fyp = self.conn_fyp.cursor()
        cur_fyp.execute(
            "select first_name from student where student_id = '" + str(self.add_list)+"'")
        for row in cur_fyp.fetchall():
            first_name.append(row)
        print(str(first_name[0])[16:-2])

        face_train = []
        cur_fyp = self.conn_fyp.cursor()
        cur_fyp.execute(
            "select face_train from student where student_id = '" + str(self.add_list) + "'")
        for row in cur_fyp.fetchall():
            face_train.append(row)
        print(str(face_train[0])[16:-2])






        if str(face_train[0])[16:-2] == 'N':
            self.date_label.config(
                text=str(self.user_name[0])[15:-2] + "      " + str(self.add_list) + str(first_name[0])[
                                                                                     16:-2] + ":Trainning      " + str(
                    self.date.strftime('%Y/%m/%d') + '      '))

            confirm_flag = vin3_face_trainning_deep.main(str(self.add_list))
            #print(confirm_flag)
            if confirm_flag == 'Success':
                #print('1')
                self.date_label.config(text=str(self.user_name[0])[15:-2] + "      " +str(self.add_list)+str(first_name[0])[16:-2] + ":Trained      " + str(
                    self.date.strftime('%Y/%m/%d') + '      '))


                cur_fyp = self.conn_fyp.cursor()
                cur_fyp.execute("update `student` set `face_train` = 'Y' where student_id = '"+str(self.add_list)+"'")
                cur_fyp.execute("commit")

                self.cur_fyp.close()
                self.db_fyp = pymysql.connect('localhost', 'root', '', 'fyp')
                self.conn_fyp = pymysql.connect(user='root',
                                            password='',
                                            db='fyp',
                                            cursorclass=pymysql.cursors.DictCursor)
                self.cur_fyp = self.db.cursor()
        else:
            self.date_label.config(text=str(self.user_name[0])[15:-2] + "      " +str(self.add_list)+str(first_name[0])[16:-2] + ":Trained At Least Once, Trainning     " + str(
                    self.date.strftime('%Y/%m/%d') + '      '))

            confirm_flag = vin3_face_trainning_deep.main(str(self.add_list))
            # print(confirm_flag)
            if confirm_flag == 'Success':
                # print('1')
                self.date_label.config(
                    text=str(self.user_name[0])[15:-2] + "      " + str(self.add_list) + str(first_name[0])[
                                                                                         16:-2] + ":Trained      " + str(
                        self.date.strftime('%Y/%m/%d') + '      '))

                cur_fyp = self.conn_fyp.cursor()
                cur_fyp.execute("update `student` set `face_train` = 'Y' where student_id = '"+str(self.add_list)+"'")
                cur_fyp.execute("commit")

                self.cur_fyp.close()
                self.db_fyp = pymysql.connect('localhost', 'root', '', 'fyp')
                self.conn_fyp = pymysql.connect(user='root',
                                                password='',
                                                db='fyp',
                                                cursorclass=pymysql.cursors.DictCursor)
                self.cur_fyp = self.db.cursor()


        self.add_list=''
        self.editAreaTable2.delete("1.0", END)
        #self.home_page("add_order")

        pass

    def face_cap(self):
        print('list'+str(self.add_list))

        first_name = []
        cur_fyp = self.conn_fyp.cursor()
        cur_fyp.execute(
            "select first_name from student where student_id = '" + str(self.add_list)+"'")
        for row in cur_fyp.fetchall():
            first_name.append(row)
        print(str(first_name[0])[16:-2])

        cap_flag = []
        cur_fyp = self.conn_fyp.cursor()
        cur_fyp.execute(
            "select face_cap from student where student_id = '" + str(self.add_list) + "'")
        for row in cur_fyp.fetchall():
            cap_flag.append(row)
        print(str(cap_flag[0])[14:-2])



        newpath = r'images/'+str(self.add_list)
        if not os.path.exists(newpath):
            os.makedirs(newpath)

        input_path='images/'+str(self.add_list)


        if str(cap_flag[0])[14:-2] == 'N':
            confirm_flag = vin3_cap_face.CatchPICFromVideo("cap_face", 0, 1000, str(input_path))
            #print(confirm_flag)
            if confirm_flag == 'Success':
                #print('1')
                self.date_label.config(text=str(self.user_name[0])[15:-2] + "      " +str(self.add_list)+str(first_name[0])[16:-2] + ":Captured      " + str(
                    self.date.strftime('%Y/%m/%d') + '      '))


                cur_fyp = self.conn_fyp.cursor()
                cur_fyp.execute("update `student` set `face_cap` = 'Y' where student_id = '"+str(self.add_list)+"'")
                cur_fyp.execute("commit")

                self.cur_fyp.close()
                self.db_fyp = pymysql.connect('localhost', 'root', '', 'fyp')
                self.conn_fyp = pymysql.connect(user='root',
                                            password='',
                                            db='fyp',
                                            cursorclass=pymysql.cursors.DictCursor)
                self.cur_fyp = self.db.cursor()
        else:
            self.date_label.config(text=str(self.user_name[0])[15:-2] + "      " +str(self.add_list)+str(first_name[0])[16:-2] + ":Has Been Captured      " + str(
                    self.date.strftime('%Y/%m/%d') + '      '))

        self.add_list=''
        self.editAreaTable2.delete("1.0", END)
        #self.home_page("add_order")

        pass



    def logout(self):
        if self.section==1 or self.section==2:
            vin3_Login_loop.main(self.root)
        elif self.section==3:
            vin3_Login_student_loop.main(self.root)

    def main_page(self, section, order_id, table_id):

        self.add_list = ''
        #self.editAreaTable2.delete("1.0", END)
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

        self.frameL11 = tk.Frame(self.left_frame)

        self.frameL11.pack()

        self.frameL12 = tk.Frame(self.left_frame)

        self.frameL12.pack()

        self.frameL13 = tk.Frame(self.left_frame)

        self.frameL13.pack()

        self.frameL14 = tk.Frame(self.left_frame)

        self.frameL14.pack()

        self.frameL15 = tk.Frame(self.left_frame)

        self.frameL15.pack()


        self.frameTablelabel = tk.Frame(self.left_frame)
        self.frameTablelabel.pack()


        tk.Label(self.frameL1, bg='black', text='Reco+',font=("Helvetica", 20, "bold "), fg="white", borderwidth=5).pack()



        self.btn_tb = [[0 for x in range(100)] for y in range(1)]
        for i in range(0, 5):
            self.btn_tb[0][i] = tk.Button(self.frameL3, text='', font=("Helvetica", 20, "bold "), background="grey20",
                                          fg='white', width=14, height=2,
                                          command='')
            self.btn_tb[0][i].pack(side=tk.LEFT)

        for i in range(5, 10):
            self.btn_tb[0][i] = tk.Button(self.frameL4, text='', font=("Helvetica", 20, "bold "), background="grey40",
                                          fg='white', width=14, height=2,
                                          command='')
            self.btn_tb[0][i].pack(side=tk.LEFT)
        for i in range(10, 15):
            self.btn_tb[0][i] = tk.Button(self.frameL5, text='', font=("Helvetica", 20, "bold "), background="grey20",
                                          fg='white', width=14, height=2,
                                          command='')
            self.btn_tb[0][i].pack(side=tk.LEFT)
        for i in range(15, 20):
            self.btn_tb[0][i] = tk.Button(self.frameL6, text='', font=("Helvetica", 20, "bold "), background="grey40",
                                          fg='white', width=14, height=2,
                                          command='')
            self.btn_tb[0][i].pack(side=tk.LEFT)
        for i in range(20, 25):
            self.btn_tb[0][i] = tk.Button(self.frameL7, text='', font=("Helvetica", 20, "bold "), background="grey20",
                                          fg='white', width=14, height=2,
                                          command='')
            self.btn_tb[0][i].pack(side=tk.LEFT)
        for i in range(25, 30):
            self.btn_tb[0][i] = tk.Button(self.frameL8, text='', font=("Helvetica", 20, "bold "), background="grey40",
                                          fg='white', width=14, height=2,
                                          command='')
            self.btn_tb[0][i].pack(side=tk.LEFT)
        for i in range(30, 35):
            self.btn_tb[0][i] = tk.Button(self.frameL9, text='', font=("Helvetica", 20, "bold "), background="grey20",
                                          fg='white', width=14, height=2,
                                          command='')
            self.btn_tb[0][i].pack(side=tk.LEFT)





        self.btn_last = tk.Button(self.frameL15, text='<', font=("Helvetica", 10, "bold "), background="grey20",
                                      fg='white', width=5, height=1,
                                      command='')
        self.btn_last.pack(side=tk.LEFT)
        self.btn_page = tk.Button(self.frameL15, text='1/1', font=("Helvetica", 10, "bold "), background="grey20",
                                  fg='white', width=8, height=1,
                                  command='')
        self.btn_page.pack(side=tk.LEFT)
        self.btn_next = tk.Button(self.frameL15, text='>', font=("Helvetica", 10, "bold "), background="grey20",
                                  fg='white', width=5, height=1,
                                  command='')
        self.btn_next.pack(side=tk.LEFT)


        #Admin/Officer
        if self.section == 1:
            self.btn_tb[0][0].config(text="Face Capture", command=lambda: self.add_reco_template('cap'))
            self.btn_tb[0][1].config(text="Face Trainning", command=lambda: self.add_reco_template('train'))

            self.btn_tb[0][5].config(text="Staff List", command=lambda: self.staff_list())
            self.btn_tb[0][6].config(text="New Staff", command=lambda: self.add_staff())
            self.btn_tb[0][7].config(text="Staff Modify", command=lambda: self.staff_modify())

            self.btn_tb[0][10].config(text="Student List", command=lambda: self.student_list())
            self.btn_tb[0][11].config(text="New Student", command=lambda: self.add_student())
            self.btn_tb[0][12].config(text="Student Modify", command=lambda: self.student_modify())

            self.btn_tb[0][15].config(text="Course List", command=lambda: self.course_list())
            self.btn_tb[0][16].config(text="New Course", command=lambda: self.add_course())
            self.btn_tb[0][17].config(text="Modify Course", command=lambda: self.course_modify())

            self.btn_tb[0][20].config(text="View\n Course Member", command=lambda: self.view_course_member())
            self.btn_tb[0][21].config(text="Add Student\n to Course", command=lambda: self.add_student_course())
            self.btn_tb[0][22].config(text="Delete Student\n from Course", command=lambda: self.del_student_course())

            self.btn_tb[0][25].config(text="View Timetable", command=lambda: self.view_timetable())
            self.btn_tb[0][26].config(text="Add Timetable", command=lambda: self.add_timetable())
            self.btn_tb[0][27].config(text="Modify Timetable", command=lambda: self.modify_timetable())

            self.btn_tb[0][30].config(text="View Attendence", command=lambda: self.view_attendence())


        #Teacher
        elif self.section == 2:

            self.btn_tb[0][0].config(text="Staff List", command=lambda: self.staff_list())

            self.btn_tb[0][1].config(text="Student List", command=lambda: self.student_list())

            self.btn_tb[0][2].config(text="Course List", command=lambda: self.course_list())

            self.btn_tb[0][3].config(text="View\n Course Member", command=lambda: self.view_course_member())

            self.btn_tb[0][4].config(text="View Timetable", command=lambda: self.view_timetable())

            self.btn_tb[0][5].config(text="View Attendence", command=lambda: self.view_attendence())

        elif self.section == 3:

            self.btn_tb[0][0].config(text="Course List", command=lambda: self.course_list())

            self.btn_tb[0][1].config(text="View\n Course Member", command=lambda: self.view_course_member())

            self.btn_tb[0][2].config(text="View Timetable", command=lambda: self.view_timetable())

            self.btn_tb[0][3].config(text="View Attendence", command=lambda: self.view_attendence())



        self.btnTR1.config(text='', font=("Helvetica", 20, "bold "), bg="grey20",
                           command='')
        self.btnTR2.config(text='', font=("Helvetica", 20, "bold "), bg="grey20",
                           command='')
        self.btnTR3.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR4.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR5.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR6.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR7.config(text='', font=("Helvetica", 20, "bold "), bg="grey20")
        self.btnTR8.config(text='LogOut', bg='grey20', command=lambda: self.logout())





        self.btnBack.config(command=lambda: self.home_page("table_sub"))
        self.btnHome.config(command=lambda: self.home_page("table_sub"))

        self.btnbag.config(command=lambda: self.bag("1"))
        self.btnrefresh.config(command=lambda: self.test_reply())

        #if section == 1:
            #pass
            #self.main_page_table()

        #elif section == 2:
            #self.switch_table(order_id, table_id)



    def __init__(self, root, id,login_method):
        self.root = root
        self.root.geometry('1920x1080')
        self.root.title("Reco+")



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
        self.position = []

        if login_method=="Staff":
            cur_fyp = self.conn_fyp.cursor()
            cur_fyp.execute("select first_name from staff where staff_id = '" + str(self.id) + "'")
            for row in cur_fyp.fetchall():
                self.user_name.append(row)



            cur_fyp = self.conn_fyp.cursor()
            cur_fyp.execute("select position from staff where staff_id = '" + str(self.id) + "'")
            for row in cur_fyp.fetchall():
                self.position.append(row)

            if str(self.position[0])[14:-2] == "Admin" or str(self.position[0])[14:-2] == "Officer" or str(
                    self.position[0])[14:-2] == "admin" or str(self.position[0])[14:-2] == "officer":
                self.section = 1
            else:
                self.section = 2
        elif login_method=="Student":
            cur_fyp = self.conn_fyp.cursor()
            cur_fyp.execute("select first_name from student where student_id = '" + str(self.id) + "'")
            for row in cur_fyp.fetchall():
                self.user_name.append(row)

            self.section = 3
        #print(str(self.position[0])[14:-2])





        self.date = datetime.datetime.now()
        self.date_label = tk.Label(self.frameRt, text=str(self.user_name[0])[16:-2] + "      " + str(
            self.date.strftime('%Y/%m/%d') + '      '), font=("Helvetica", 20, "bold"), bg='black', fg="white")
        self.date_label.pack(side=tk.LEFT)




        self.clock1 = clock.Clock(self.frameRt)
        self.clock1.pack(side=tk.LEFT)
        #self.clock1.configure(font=("Helvetica", 20, "bold"), bg='dark green', fg="white")

        #self.btnbag = tk.Button(self.frameRt, text='Bag: 0', font=("Helvetica", 10, "bold "), width=20,height=1, bg="black", fg="white", command=lambda: self.bag("1"))
        #self.btnbag.pack(side=tk.LEFT)

        self.btnrefresh = tk.Button(self.frameRt, text='⟳', font=("Helvetica", 10, "bold "), width=5,
                                    height=1, bg="black", fg="white", command='')
        self.btnrefresh.pack(side=tk.LEFT)
        self.btnnotification = tk.Button(self.frameRt, text='Notifications', font=("Helvetica", 10, "bold "), width=20,
                                    height=1, bg="black", fg="white", command='')
        self.btnnotification.pack(side=tk.LEFT)
        self.btnnewnoti = tk.Button(self.frameRt, text='+', font=("Helvetica", 10, "bold "), width=5,
                                    height=1, bg="black", fg="white", command='')
        self.btnnewnoti.pack(side=tk.LEFT)

        if self.section == 1:
            self.date_label.config(bg='dark green')
            self.clock1.configure(font=("Helvetica", 20, "bold"), bg='dark green', fg="white")
            self.btnrefresh.config(bg="dark green")
            self.btnnotification.config(bg="dark green")
            self.btnnewnoti.config(bg="dark green")
            self.frameRt.config(background="dark green")
        elif self.section == 2:
            self.date_label.config(bg='dark red')
            self.clock1.configure(font=("Helvetica", 20, "bold"), bg='dark red', fg="white")
            self.btnrefresh.config(bg="dark red")
            self.btnnotification.config(bg="dark red")
            self.btnnewnoti.config(bg="dark red")
            self.frameRt.config(background="dark red")
        elif self.section == 3:
            self.date_label.config(bg='midnight blue')
            self.clock1.configure(font=("Helvetica", 20, "bold"), bg='midnight blue', fg="white")
            self.btnrefresh.config(bg="midnight blue")
            self.btnnotification.config(bg="midnight blue")
            self.btnnewnoti.config(bg="midnight blue")
            self.frameRt.config(background="midnight blue")


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

        self.btnBack = tk.Button(self.frame_bottom_nvaigation, text='< BACK', font=("Helvetica", 10, "bold "), width=88,
                                 height=1, bg="black", fg="white")
        self.btnBack.pack(side=tk.LEFT)

        self.btnHome = tk.Button(self.frame_bottom_nvaigation, text='O HOME', font=("Helvetica", 10, "bold "), width=88,
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


        self.main_page(self.section, [], '')


def main(id,login_method, window):
    root = tk.Tk()
    window.destroy()
    Gui(root, id,login_method)

    root.mainloop()


if __name__ == '__main__':
    sys.exit(main())

