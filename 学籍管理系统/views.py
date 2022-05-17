from cgitb import strong
import tkinter as tk
from tkinter import ttk
from requests import delete


from setuptools import Command
from database import db


class AboutFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        tk.Label(self, text="关于作品：本作品由python库tkinter制作").pack()
        tk.Label(self, text="关于作者：刘金超 202131201053    罗庆宏 202131201067").pack()
        tk.Label(self, text="完成时间：2022年5月16日").pack()


class GradeFrame(tk.Frame):

    def __init__(self, root):
        super().__init__(root)

        self.table_view = tk.Frame()
        self.table_view.pack()
        self.create_page()

    def create_page(self):

        columns = ('1', '2', '3', '4')
        columns_values = ('1', '2', '3', '4')
        self.tree_view = ttk.Treeview(self, show='headings', columns=columns)
        self.tree_view.column('1', width=100, anchor='center')
        self.tree_view.column('2', width=100, anchor='center')
        self.tree_view.column('3', width=100, anchor='center')
        self.tree_view.column('4', width=100, anchor='center')
        self.tree_view.heading('1', text='--1--')
        self.tree_view.heading('2', text='--2--')
        self.tree_view.heading('3', text='--3--')
        self.tree_view.heading('4', text='--4--')
        self.tree_view.pack(fill=tk.BOTH, expand=True)
        self.search = tk.StringVar()
        tk.Entry(self, textvariable=self.search).pack(pady=5)
        tk.Button(self, text="点此以学号查询成绩",
                  command=self.show_base_info_1).pack(
            anchor=tk.E, pady=5)

    def show_base_info_1(self):
        # 删除旧的数据
        for i in map(self.tree_view.delete, self.tree_view.get_children('')):
            pass

        key = self.search.get()
        students = db.base_info()
        grade = db.grade_info()

        index = 0
        count = 0
        all = 0

        for i in students:
            list1 = i.split()
            # print(list1)
            if key == list1[0]:
                self.tree_view.insert(
                    '', index+1, values=('学号:'+list1[0], '姓名:'+list1[1], '', ''))
                for j in grade:
                    if key == j[0]:
                        self.tree_view.insert(
                            '', index+1, values=('课程编号:'+str(j[1]), '课程名称:'+str(j[2]), '综合成绩:'+str(j[7]), '实得学分'+str(j[8])))
                        count += 1
                        all += j[8]
                self.tree_view.insert(
                    '', count+2, values=('共修:'+str(count)+'科', '实得总学分:'+str(all), '', ''))


class InsertFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        # # tk.Label(self, text="录入页面").pack()
        # self.id = tk.StringVar()
        # self.subject_id = tk.StringVar()
        # self.subject_name = tk.StringVar()
        # self.credit = tk.StringVar()
        # self.usual_grade = tk.StringVar()
        # self.trail_grade = tk.StringVar()
        # self.test_grade = tk.StringVar()
        self.status = tk.StringVar()
        # self.comprehensive_grade = 0
        # self.get_credit = 0
        self.create_page()

    def create_page(self):
        tk.Label(self).grid(row=0, pady=10)
        tk.Button(self, text='点此键一键录入', command=self.record_info).grid(
            row=1, column=1, pady=10)
        tk.Label(self, textvariable=self.status).grid(
            row=9, column=2, pady=10, sticky=tk.E)
        tk.Button(self, text='删除数据后点此键一键刷新', command=self.delete).grid(
            row=1, column=3, pady=10)
        tk.Label(self, textvariable=self.status).grid(
            row=9, column=2, pady=10, sticky=tk.E)
        # tk.Label(self, text='学号').grid(row=1, column=1, pady=10)
        # tk.Entry(self, textvariable=self.id).grid(row=1, column=2, pady=10)

        # tk.Label(self, text='课程编号').grid(row=2, column=1, pady=10)
        # tk.Entry(self, textvariable=self.subject_id).grid(
        #     row=2, column=2, pady=10)

        # tk.Label(self, text='课程名称').grid(row=3, column=1, pady=10)
        # tk.Entry(self, textvariable=self.subject_name).grid(
        #     row=3, column=2, pady=10)

        # tk.Label(self, text='学分').grid(row=4, column=1, pady=10)
        # tk.Entry(self, textvariable=self.credit).grid(row=4, column=2, pady=10)

        # tk.Label(self, text='平时成绩').grid(row=5, column=1, pady=10)
        # tk.Entry(self, textvariable=self.usual_grade).grid(
        #     row=5, column=2, pady=10)

        # tk.Label(self, text='实验成绩').grid(row=6, column=1, pady=10)
        # tk.Entry(self, textvariable=self.trail_grade).grid(
        #     row=6, column=2, pady=10)

        # tk.Label(self, text='卷面成绩').grid(row=7, column=1, pady=10)
        # tk.Entry(self, textvariable=self.test_grade).grid(
        #     row=7, column=2, pady=10)

        # tk.Button(self, text='录入', command=self.record_info).grid(
        #     row=8, column=2, pady=10, sticky=tk.E)
        # tk.Label(self, textvariable=self.status).grid(
        #     row=9, column=2, pady=10, sticky=tk.E)

        # tk.Label(self, text='综合成绩为：').grid(
        #     row=10, column=1, pady=10)
        # tk.Label(self, textvariable=self.comprehensive_grade).grid(
        #     row=10, column=2, pady=10)

        # tk.Label(self, text='实得学分为：').grid(
        #     row=11, column=1, pady=10)
        # tk.Label(self, textvariable=self.get_credit).grid(
        #     row=11, column=2, pady=10)

    def record_info(self):
        db.read_grade_info()
        self.status.set('录入数据成功！')

    def delete(self):
        self.status.set('刷新数据成功！')
        with open('A.txt', 'r', encoding='utf-8') as f:
            x = f.readlines()
        num = []
        for i in x:
            num.append(i.split()[0])
        grade = db.grade_info()
        list1 = []
        for i in range(len(grade)):
            if grade[i][0] in num:
                i += 1
                i -= 1
            else:
                list1.append(i)
        lines = open('B.txt', encoding='utf-8') .readlines()
        strr = lines[0]
        for i in range(1, len(lines)):
            if i-1 not in list1:
                strr += lines[i]
        open('B.txt', 'w+', encoding='utf-8') .writelines(strr)


class BaseFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        self.table_view = tk.Frame()
        self.table_view.pack()
        self.create_page()

    def create_page(self):
        # self.search = tk.StringVar()
        # tk.Label(self).grid(row=0, pady=10)
        # tk.Label(self, text='输入查询条件').grid(row=1, column=1, pady=10)
        # tk.Entry(self, textvariable=self.search).grid(row=1, column=2, pady=10)
        # tk.Button(self, text="点此以姓名查询",
        #           command=self.show_page).grid(row=2, column=1, pady=5)
        # tk.Button(self, text="点此以学号查询",
        #           command=self.show_base_info).grid(row=2, column=2, pady=5)
        # tk.Button(self, text="点此以宿舍号查询",
        #           command=self.show_base_info).grid(row=2, column=3, pady=5)
        columns = ('id', 'name', 'sex', 'dorm', 'phone')
        columns_values = ('学号', '姓名', '性别', '宿舍号码', '电话号码')
        self.tree_view = ttk.Treeview(self, show='headings', columns=columns)
        self.tree_view.column('id', width=100, anchor='center')
        self.tree_view.column('name', width=100, anchor='center')
        self.tree_view.column('sex', width=100, anchor='center')
        self.tree_view.column('dorm', width=100, anchor='center')
        self.tree_view.column('phone', width=100, anchor='center')
        self.tree_view.heading('id', text='学号')
        self.tree_view.heading('name', text='姓名')
        self.tree_view.heading('sex', text='性别')
        self.tree_view.heading('dorm', text='宿舍号码')
        self.tree_view.heading('phone', text='电话号码')
        self.tree_view.pack(fill=tk.BOTH, expand=True)
        self.search = tk.StringVar()
        tk.Entry(self, textvariable=self.search).pack(pady=5)
        tk.Button(self, text="点此以学号查询",
                  command=self.show_base_info_1).pack(
            anchor=tk.E, pady=5)
        tk.Button(self, text="点此以姓名查询",
                  command=self.show_base_info_2).pack(
            anchor=tk.E, pady=5)
        tk.Button(self, text="点此以宿舍号查询",
                  command=self.show_base_info_3).pack(
            anchor=tk.E, pady=5)

    def show_base_info_1(self):
        # 删除旧的数据
        for i in map(self.tree_view.delete, self.tree_view.get_children('')):
            pass
        key = self.search.get()
        students = db.base_info()
        index = 0

        for i in students:
            list1 = i.split()
            # print(list1)
            if key in list1:
                self.tree_view.insert(
                    '', index+1, values=(list1[0], list1[1], list1[2], list1[3], list1[4]))

    def show_base_info_2(self):
        # 删除旧的数据
        for i in map(self.tree_view.delete, self.tree_view.get_children('')):
            pass
        key = self.search.get()
        students = db.base_info()
        index = 0

        for i in students:
            list1 = i.split()
            # print(list1)
            if key == list1[1]:
                self.tree_view.insert(
                    '', index+1, values=(list1[0], list1[1], list1[2], list1[3], list1[4]))

    def show_base_info_3(self):
        # 删除旧的数据
        for i in map(self.tree_view.delete, self.tree_view.get_children('')):
            pass
        key = self.search.get()
        students = db.base_info()
        index = 0

        for i in students:
            list1 = i.split()
            # print(list1)
            if key == list1[3]:
                self.tree_view.insert(
                    '', index+1, values=(list1[0], list1[1], list1[2], list1[3], list1[4]))

        # if a == 2:
        #     for i in students:
        #         list1 = i.split()
        #         if key == list1[0]:
        #             self.tree_view.insert(
        #                 '', index+1, values=(list1[0], list1[1], list1[2], list1[3], list1[4]))

        # if a == 3:
        #     pass


class DeleteFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        tk.Label(self, text="删除页面").pack()


class SortFrame(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        self.table_view = tk.Frame()
        self.table_view.pack()
        self.create_page()

    def create_page(self):

        columns = ('1', '2', '3', '4')
        columns_values = ('1', '2', '3', '4')
        self.tree_view = ttk.Treeview(self, show='headings', columns=columns)
        self.tree_view.column('1', width=100, anchor='center')
        self.tree_view.column('2', width=100, anchor='center')
        self.tree_view.column('3', width=100, anchor='center')
        self.tree_view.column('4', width=100, anchor='center')
        self.tree_view.heading('1', text='--1--')
        self.tree_view.heading('2', text='--2--')
        self.tree_view.heading('3', text='--3--')
        self.tree_view.heading('4', text='--4--')
        self.tree_view.pack(fill=tk.BOTH, expand=True)
        tk.Button(self, text="点此以实得学分降序排名成绩",
                  command=self.show_base_info_1).pack(
            anchor=tk.E, pady=5)
        tk.Button(self, text="点此以实得学分升序排名成绩",
                  command=self.show_base_info_2).pack(
            anchor=tk.E, pady=5)

        tk.Button(self, text="点此以综合成绩降序排名成绩",
                  command=self.show_base_info_3).pack(
            anchor=tk.E, pady=5)

        tk.Button(self, text="点此以综合成绩升序排名成绩",
                  command=self.show_base_info_4).pack(
            anchor=tk.E, pady=5)

    def show_base_info_1(self):
        # 删除旧的数据
        for i in map(self.tree_view.delete, self.tree_view.get_children('')):
            pass

        students = db.base_info()
        grade = db.grade_info()

        count = [0 for i in range(len(students))]
        all = [0 for i in range(len(students))]

        for i in range(len(students)):
            list1 = students[i].split()
            for j in grade:
                if list1[0] == j[0]:
                    count[i] += j[8]
        rank = sorted(count, reverse=True)
        for i in range(len(rank)):
            num = count.index(rank[i])
            self.tree_view.insert(
                '', i+1, values=('学号:'+students[num].split()[0], '姓名:'+students[num].split()[1], '实得学分：'+str(rank[i]), '排名：'+str(i+1)))
            count[num] = -999

    def show_base_info_2(self):
        # 删除旧的数据
        for i in map(self.tree_view.delete, self.tree_view.get_children('')):
            pass

        students = db.base_info()
        grade = db.grade_info()

        count = [0 for i in range(len(students))]
        all = [0 for i in range(len(students))]

        for i in range(len(students)):
            list1 = students[i].split()
            for j in grade:
                if list1[0] == j[0]:
                    count[i] += j[8]
        rank = sorted(count)
        for i in range(len(rank)):
            num = count.index(rank[i])
            self.tree_view.insert(
                '', i+1, values=('学号:'+students[num].split()[0], '姓名:'+students[num].split()[1], '实得学分：'+str(rank[i]), '排名：'+str(len(rank)-i)))
            count[num] = -999

    def show_base_info_3(self):
        # 删除旧的数据
        for i in map(self.tree_view.delete, self.tree_view.get_children('')):
            pass

        students = db.base_info()
        grade = db.grade_info()

        count = [0 for i in range(len(students))]
        all = [0 for i in range(len(students))]

        for i in range(len(students)):
            list1 = students[i].split()
            for j in grade:
                if list1[0] == j[0]:
                    all[i] += j[7]
        rank = sorted(all, reverse=True)
        for i in range(len(rank)):
            num = all.index(rank[i])
            self.tree_view.insert(
                '', i+1, values=('学号:'+students[num].split()[0], '姓名:'+students[num].split()[1], '综合成绩：'+str(rank[i]), '排名：'+str(i+1)))
            all[num] = -9999

    def show_base_info_4(self):
        # 删除旧的数据
        for i in map(self.tree_view.delete, self.tree_view.get_children('')):
            pass

        students = db.base_info()
        grade = db.grade_info()

        count = [0 for i in range(len(students))]
        all = [0 for i in range(len(students))]

        for i in range(len(students)):
            list1 = students[i].split()
            for j in grade:
                if list1[0] == j[0]:
                    all[i] += j[7]
        rank = sorted(all)
        for i in range(len(rank)):
            num = all.index(rank[i])
            self.tree_view.insert(
                '', i+1, values=('学号:'+students[num].split()[0], '姓名:'+students[num].split()[1], '综合成绩：'+str(rank[i]), '排名：'+str(len(rank)-i)))
            all[num] = -9999
