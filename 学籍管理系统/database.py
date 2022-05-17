class MysqlDatabases:
    def __init__(self):
        # 获取用户名和密码
        with open('user_info.txt', 'r') as f:
            list1 = f.readlines()

        list_username = []
        list_password = []
        for i in list1:
            list_username.append(i.split()[0])
            list_password.append(i.split()[1])
        self.user = list_username
        self.password = list_password

        # 获取学生的基本信息 读取A.txt
        with open('A.txt', 'r', encoding='UTF-8') as ff:
            list2 = ff.readlines()
        self.stu_base_info = []
        for i in range(1, len(list2)):
            self.stu_base_info.append(list2[i])

    def read_info(self):
        # 获取学生的基本信息 读取A.txt
        with open('A.txt', 'r', encoding='UTF-8') as ff:
            list2 = ff.readlines()
        self.stu_base_info = []
        for i in range(1, len(list2)):
            self.stu_base_info.append(list2[i])
        # 读取学生的成绩信息 读取B.txt
        with open('B.txt', 'r', encoding='UTF-8') as fff:
            list3 = fff.readlines()
        self.stu_grade_info = []
        for i in range(1, len(list3)):
            self.stu_grade_info.append(list3[i].split())

    def check_login(self, username, password):

        if username in self.user:
            if password == self.password[self.user.index(username)]:
                return True, "登录成功"
            else:
                return False, "登陆失败，输入密码错误"
        else:
            return False, "登陆失败，您输入的用户名不存在"

    def base_info(self):
        self.read_info()
        return self.stu_base_info

    def grade_info(self):
        self.read_info()
        for i in self.stu_grade_info:
            comprehensive = 0
            if i[5] == '-1':
                comprehensive = round(int(i[4])*0.3+int(i[6])*0.7, 2)
            else:
                comprehensive = round(
                    int(i[4])*0.15+int(i[5])*0.15+int(i[6])*0.7, 2)
            i.append(comprehensive)
            credit = 0
            if comprehensive < 60:
                credit = 0
            elif comprehensive < 70:
                credit = round(0.6*int(i[3]), 2)
            elif comprehensive < 80:
                credit = round(0.75*int(i[3]), 2)
            elif comprehensive < 90:
                credit = round(0.8*int(i[3]), 2)
            elif comprehensive <= 100:
                credit = round(int(i[3]), 2)
            i.append(credit)
        return self.stu_grade_info


db = MysqlDatabases()
if __name__ == '__main__':
    print(db.check_login('root', '123456'))
    print(db.grade_info())
