#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:王凯龙

from tkinter import Button, Tk, Label, messagebox
from tkinter import filedialog, dialog
import os
import Stitcher
import cv2

window = Tk()
window.title('图像拼接大作业-WKL-DHC')
window.geometry('400x500+550+200')
window['background'] = 'lightcyan'

img_left = None
img_right = None
S = None


def open_right():
    global img_right
    if img_right is None:
        file_path = filedialog.askopenfilename(title=u'选择图片', initialdir=(os.path.expanduser(r'./imgs')))
        img_right = cv2.imread(file_path)
        messagebox.showinfo(title='', message='读取成功')
    else:
        messagebox.showwarning(title='WARNING', message='已经读过了')


def open_left():
    global img_left
    if img_left is None:
        file_path = filedialog.askopenfilename(title=u'选择图片', initialdir=(os.path.expanduser(r'./imgs')))
        img_left = cv2.imread(file_path)
        messagebox.showinfo(title='', message='读取成功')
    else:
        messagebox.showwarning(title='WARNING', message='已经读过了')


def sift():
    global S
    if img_left is None or img_right is None:
        messagebox.showwarning(title='WARNING', message='请先读取图片')
    elif S is None:
        messagebox.showinfo(title='', message='运行时间较长，\n完成后会有提醒，\n请勿进行其余操作！')
        A = Stitcher.Stitcher(img_left, img_right)
        S = A
        messagebox.showinfo(title='', message='运行成功')
    else:
        messagebox.showinfo(title='', message='已计算完毕')


def show_right():
    global S
    if S is None:
        messagebox.showwarning(title='WARNING', message='请先进行SIFT')
    else:
        S.s2.Show_d()


def show_left():
    global S
    if S is None:
        messagebox.showwarning(title='WARNING', message='请先进行SIFT')
    else:
        S.s1.Show_d()


def show_match():
    global S
    if S is None:
        messagebox.showwarning(title='WARNING', message='请先进行SIFT')
    else:
        S.Show_h()


def show_result():
    global S
    if S is None:
        messagebox.showwarning(title='WARNING', message='请先进行SIFT')
    else:
        cv2.imshow('result', S.result)
        cv2.waitKey(0)


def save_file():
    global S
    if S is None:
        messagebox.showwarning(title='WARNING', message='请先进行SIFT')
    else:
        file_path = filedialog.asksaveasfilename(title=u'选择文件夹', initialdir=(os.path.expanduser('.')))
        cv2.imwrite(file_path, S.result)
        messagebox.showinfo(title='', message='保存成功')


def clear_all():
    global S
    global img_right
    global img_left
    S = img_right = img_left = None


l = Label(window, text=u'图像拼接--designed by WKL-DHC', bg='lightcyan', font=('systemfixed', 17), width=30, height=2)
l.place(x=21, y=30, anchor='nw')
bt_left = Button(window, text='选择左侧图片', bg='yellow', overrelief='sunken', font=('systemfixed', 14), command=open_left)
bt_right = Button(window, text='选择右侧图片', bg='yellow', overrelief='sunken', font=('systemfixed', 14), command=open_right)
bt_sift = Button(window, text='SIFT处理', bg='coral', overrelief='sunken', font=('systemfixed', 14), command=sift)
bt_showL = Button(window, text='显示左图关键点', bg='skyblue', overrelief='sunken', font=('systemfixed', 14), command=show_left)
bt_showR = Button(window, text='显示右图关键点', bg='skyblue', overrelief='sunken', font=('systemfixed', 14), command=show_right)
bt_show = Button(window, text='关键点匹配图', bg='violet', overrelief='sunken', font=('systemfixed', 14), command=show_match)
bt_show2 = Button(window, text='图像拼接结果', bg='violet', overrelief='sunken', font=('systemfixed', 14), command=show_result)
bt_show3 = Button(window, text='保存结果', bg='turquoise', overrelief='sunken', font=('systemfixed', 14), command=save_file)
bt_all = Button(window, text='清空结果', bg='turquoise', overrelief='sunken', font=('systemfixed', 14), command=clear_all)
bt_show4 = Button(window, text='关闭程序', bg='tomato', height=3, width=20, overrelief='sunken', font=('systemfixed', 14), command=window.destroy)
bt_left.place(x=10, y=100, anchor='nw')
bt_right.place(x=155, y=100, anchor='nw')
bt_sift.place(x=300, y=100, anchor='nw')
bt_showL.place(x=30, y=163, anchor='nw')
bt_showR.place(x=223, y=163, anchor='nw')
bt_show.place(x=39, y=225, anchor='nw')
bt_show2.place(x=233, y=225, anchor='nw')
bt_show3.place(x=59, y=286, anchor='nw')
bt_all.place(x=250, y=286, anchor='nw')
bt_show4.place(x=95, y=365, anchor='nw')


window.mainloop()
