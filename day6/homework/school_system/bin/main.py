# Author:haha

from day6.homework.school_system.core.school import School
from day6.homework.school_system.core.course import Course
from day6.homework.school_system.core.student import Student
from day6.homework.school_system.core.classse import Classes
from day6.homework.school_system.core.teacher import Teacher
import pickle
class Run():
    def __init__(self):
        self.info={}

    def get_info(self):
        info_file = open(r'../db/info.json', 'rb')
        info = pickle.load(info_file)
        info_file.close()
        return info
    def create_school(self,name,addr,info={}):
        if name in info:
            print('已存在该名字学校，请重新取名！')
        else:
            school=School(name,addr)
            school_data={}
            school_data['addr']=addr
            school_data['tea_list']={}
            school_data['course_list']={}
            self.info[name]=school_data
            school_file=open(r'../db/info.json', 'wb')
            pickle.dump(self.info,school_file)
            school_file.close()
            return school

    def run(self):
        while True:
            info = self.get_info()
            for i in info:
                print(i)
            print(info)
            choose_school=input('请选择学校：')
            if choose_school in info:
                choose_part=input('请输入自己的角色：s(student)/t(teacher)/a(admin):')
                if choose_part=='s':
                    self.student_part(choose_school)
                elif choose_part=='a':
                    self.admin_part(choose_school)
                elif choose_part=='t':
                    self.teacher_part(choose_school)
            else:
                print('输入错误，请重新输入！')

    def student_part(self,school_obj):
        while True:
            print('''
            学生视图业务：
            注册:1
            交学费：2
            查看信息：3
            退出：4
            返回：5
            ''')
            choose_business=input('请输入业务序号：')
            if choose_business =='1':
                stu_name=input('请输入学生姓名：')
                stu_age=input('请输入学生年龄：')
                stu_sex=input('请输入学生性别：')
                stu=Student(stu_name,stu_age,stu_sex)
                info=self.get_info()
                stu.register(school_obj,info)
            elif choose_business=='2':
                stu=Student('','','')
                info=self.get_info()
                stu.pay_tuition(school_obj,info)
            elif choose_business=='3':
                stu=Student('','','')
                info=self.get_info()
                stu.look_info(school_obj,info)

            elif choose_business=='4':
                exit('已退出！')
            elif choose_business == '5':
                break
            else:
                print('输入错误，请重新输入！')


    def admin_part(self,school_obj):
        while True:
            print('''
            管理员视图业务：
            创建课程:1
            创建班级：2
            创建讲师：3
            退出：4
            返回：5
            ''')
            choose_business=input('请输入业务序号：')
            info = self.get_info()
            school_class = School(school_obj, info[school_obj]['addr'])
            if choose_business == '1':
                course_name=input('请输入课程名字：')
                if course_name not in info[school_obj]['course_list']:
                    course_price=input('请输入课程价格：')
                    course_cycle=input('请输入课程周期：')
                    course=Course(course_name,course_price,course_cycle)
                    school_class.create_course(course,info)
                else:
                    print('已存在该课程，请重新输入！')
            elif choose_business=='2':
                classes=Classes('')
                info=self.get_info()
                school_class.create_class(classes,info[school_obj]['course_list'],info)
            elif choose_business=='3':
                teacher=Teacher('')
                info=self.get_info()
                school_class.creat_teacher(teacher,info[school_obj]['course_list'],info)
            elif choose_business=='4':
                exit('已退出！')
            elif choose_business=='5':
                break
            else:
                print('输入错误，请重新输入！')

    def teacher_part(self,school_obj):
        while True:
            print('''
            讲师视图业务：
            选择班级:1
            查看学生信息：2
            修改学生成绩：3
            退出：4
            返回：5
            ''')
            choose_business=input('请输入业务序号：')
            info = self.get_info()
            school_class = School(school_obj, info[school_obj]['addr'])
            if choose_business == '1':
                teacher=Teacher('')
                teacher.update_class(school_class,school_obj,info)
            elif choose_business == '2':
                teacher=Teacher('')
                teacher.look_stu_list(school_class,school_obj,info)
            elif choose_business == '3':
                teacher=Teacher('')
                teacher.update_stu_list(school_class,school_obj,info)
            elif choose_business == '4':
                exit('已退出！')
            elif choose_business == '5':
                break
            else:
                print('输入错误，请重新输入！')

    def update_info(self):
        info=self.get_info()
        print(info)
        del info['beijing_school']['tea_list']
        print(info)
        info_file = open(r'../db/info.json', 'wb')
        pickle.dump(info,info_file)
        info_file.close()

if __name__ == '__main__':
    run=Run()
    # beijing_school=run.create_school('beijing_school','beijing')
    # info=run.get_info()
    # shanghai_school=run.create_school('shanghai_school','shanghai',info)
    #
    # info=run.get_info()
    # linux_course = Course('linux', '10000', '7month')
    # python_course = Course('python', '8000', '5month')
    # go_course = Course('go', '5000', '3month')
    # beijing_school.create_course(linux_course,info)
    # beijing_school.create_course(python_course,info)
    # shanghai_school.create_course(go_course,info)
    #
    # info=run.get_info()
    # py1_claas = Classes('py1')
    # py2_claas = Classes('p2')
    # l1_claas = Classes('l1')
    # l2_claas = Classes('l2')
    # go1_claas = Classes('go1')
    # beijing_school.create_class(py1_claas,info['beijing_school']['course_list'].keys(),info)
    # beijing_school.create_class(py2_claas,info['beijing_school']['course_list'].keys(),info)
    # beijing_school.create_class(l1_claas,info['beijing_school']['course_list'].keys(),info)
    # beijing_school.create_class(l2_claas,info['beijing_school']['course_list'].keys(),info)
    # shanghai_school.create_class(go1_claas,info['shanghai_school']['course_list'].keys(),info)
    # run.update_info()
    run.run()
