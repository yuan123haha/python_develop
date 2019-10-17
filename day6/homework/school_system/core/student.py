# Author:haha

from .member import Member
import pickle

class Student(Member):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
        self.grade={}
        self.score=0
        self.ispay_tuition='n'
        self.uid=0

    def update_info(self,info):
        info_file = open(r'../db/info.json', 'wb')
        pickle.dump(info, info_file)
        info_file.close()

    def register(self,school_obj,info):
        course_obj,class_obj,choose_class,choose_course=self.choose_class(school_obj,info)
        stu_data={}
        stu_data['age']=self.age
        stu_data['sex']=self.sex
        stu_data['grade']={}
        stu_data['grade'][choose_course]=choose_class
        stu_data['score']=''
        stu_data['ispay_tuition']='n'
        stu_data['uid']=len(class_obj)+1

        course_obj['class_list'][choose_class][self.name]=stu_data
        print('''
        student[%s] register info
        studentName:%s
        studentAge:%s
        studentSex:%s
        studentGrade:%s
        isPay_Tuition:n
        studentId:%s
        ''' % (self.name,self.name,self.age,self.sex,stu_data['grade'],stu_data['uid']))
        self.update_info(info)

    def pay_tuition(self,school_obj,info):
        while True:
            course_obj,class_obj,choose_class,choose_course=self.choose_class(school_obj,info)
            stu_name = input('请输入学生姓名：')
            if stu_name in class_obj:
                stu_id= int(input('请输入学生ID号：'))
                if stu_id == class_obj[stu_name]['uid']:
                    if class_obj[stu_name]['ispay_tuition']=='n':
                        print('课程学费还未交，需交%s'%course_obj['price'])
                        class_obj[stu_name]['ispay_tuition']='y'
                        self.update_info(info)
                        print('已交该课程学费')
                        break
                    else:
                        print('该课程学费已交！不能重复交付，已退出。。。')
                        break
                else:print('输入学号不匹配，请重新输入！')
            else:
                print('学生不存在，请重新输入！')

    def look_info(self,school_obj,info):
        course_obj,class_obj,choose_class,choose_course=self.choose_class(school_obj,info)
        while True:
            stu_name = input('请输入学生姓名：')
            if stu_name in class_obj:
                stu_id = int(input('请输入学生ID号：'))
                if stu_id == class_obj[stu_name]['uid']:
                    print('''
                    student[%s] info
                    studentName:%s
                    studentAge:%s
                    studentSex:%s
                    studentGrade:%s
                    isPay_Tuition:%s
                    studentId:%s
                    ''' % (stu_name,stu_name,class_obj[stu_name]['age'],class_obj[stu_name]['sex'],class_obj[stu_name]['grade'],class_obj[stu_name]['ispay_tuition'],class_obj[stu_name]['uid']))
                    return
                else:print('输入学号不匹配，请重新输入！')
            else:print('该学生不存在，请重新输入！')

    def choose_class(self,school_obj,info):
        for i in info[school_obj]['course_list']:
            print(i)
        while True:
            choose_course =input('请选择课程：')
            if choose_course in info[school_obj]['course_list']:
                for i in info[school_obj]['course_list'][choose_course]['class_list']:
                    print(i)
                while True:
                    choose_class =input('请选择班级：')
                    if choose_class in info[school_obj]['course_list'][choose_course]['class_list']:
                        course_obj=info[school_obj]['course_list'][choose_course]
                        class_obj=info[school_obj]['course_list'][choose_course]['class_list'][choose_class]
                        return course_obj,class_obj,choose_class,choose_course
                    else:
                        print('输入错误，请重新输入')
            else:
                print('输入错误，请重新输入')