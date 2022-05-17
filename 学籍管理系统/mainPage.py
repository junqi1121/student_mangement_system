from logging import root
import tkinter as tk

from requests import delete
from views import AboutFrame, GradeFrame, InsertFrame, BaseFrame, DeleteFrame, SortFrame


class MainPage:
    def __init__(self, master: tk.Tk):
        self.root = master
        self.root.geometry('800x600')
        self.root.title('学生信息管理系统 v0.0.1')
        self.create_page()

    def create_page(self):

        self.insert_frame = InsertFrame(self.root)
        self.base_frame = BaseFrame(self.root)
        self.delete_frame = DeleteFrame(self.root)
        self.sort_frame = SortFrame(self.root)
        self.about_frame = AboutFrame(self.root)
        self.grade_frame = GradeFrame(self.root)

        menubar = tk.Menu(self.root)
        menubar.add_command(label='数据录入与删除', command=self.show_insert)
        menubar.add_command(label='基本情况查询', command=self.show_base)
        menubar.add_command(label='成绩查询', command=self.show_grade)

        # menubar.add_command(label='删除信息', command=self.show_delete)
        menubar.add_command(label='排序', command=self.show__sort)
        menubar.add_command(label='关于', command=self.show_about)
        self.root['menu'] = menubar

    # 数据录入已完成
    def show_insert(self):
        self.insert_frame.pack()
        self.base_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.sort_frame.pack_forget()
        self.about_frame.pack_forget()
        self.grade_frame.pack_forget()
    # 基本信息查询

    def show_base(self):
        self.insert_frame.pack_forget()
        self.base_frame.pack()
        self.delete_frame.pack_forget()
        self.sort_frame.pack_forget()
        self.about_frame.pack_forget()
        self.grade_frame.pack_forget()
    # 删除信息

    def show_delete(self):
        self.insert_frame.pack_forget()
        self.base_frame.pack_forget()
        self.delete_frame.pack()
        self.sort_frame.pack_forget()
        self.about_frame.pack_forget()
        self.grade_frame.pack_forget()
    # 排序显示

    def show__sort(self):
        self.insert_frame.pack_forget()
        self.base_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.sort_frame.pack()
        self.about_frame.pack_forget()
        self.grade_frame.pack_forget()
    # 关于

    def show_about(self):
        self.about_frame.pack()
        self.insert_frame.pack_forget()
        self.base_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.sort_frame.pack_forget()
        self.grade_frame.pack_forget()

    # 成绩查询

    def show_grade(self):
        self.grade_frame.pack()
        self.insert_frame.pack_forget()
        self.base_frame.pack_forget()
        self.delete_frame.pack_forget()
        self.sort_frame.pack_forget()
        self.about_frame.pack_forget()


if __name__ == '__main__':
    root = tk.Tk()
    MainPage(root)
    root.mainloop()
