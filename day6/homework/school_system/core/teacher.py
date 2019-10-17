# Author:haha
from .member import Member
import pickle

class Teacher(Member):

    def update_info(self,info):
        info_file = open(r'../db/info.json', 'wb')
        pickle.dump(info, info_file)
        info_file.close()

    def look_stu_list(self,school_class,school_obj,info):
        course_obj, teacher_name, choose_course = self.choose_class(school_class, school_obj, info)
        while True:
            for i in course_obj['tea_list'][teacher_name]:
                print(i)
            choose_class = input('请输入班级：')
            if choose_class in course_obj['tea_list'][teacher_name]:
                print('class[%s] stu_list'%choose_class)
                for i in course_obj['class_list'][choose_class]:
                    print(i)
                choose_stu=input('请输入学生姓名：')
                if choose_stu in course_obj['class_list'][choose_class]:
                    print(course_obj['class_list'][choose_class][choose_stu])
                    return choose_stu,choose_course,choose_class
                else:print('学生不存在！')
            else:print('班级不存在，请重新输入！')

    def update_stu_list(self,school_class,school_obj,info):
        choose_stu,choose_course,choose_class=self.look_stu_list(school_class,school_obj,info)
        new_score = int(input('请输入成绩分数：'))
        info[school_obj]['course_list'][choose_course]['class_list'][choose_class][choose_stu]['score']=new_score
        self.update_info(info)

    def choose_class(self,school_class,school_obj,info):
        while True:
            for i in info[school_obj]['course_list']:
                print(i)
            choose_course = input('请输入选择的课程：')
            if choose_course in info[school_obj]['course_list']:
                teacher_name = input('请输入讲师姓名：')
                if teacher_name in info[school_obj]['course_list'][choose_course]['tea_list']:
                    return info[school_obj]['course_list'][choose_course],teacher_name,choose_course
                else:print('该老师没有在该课程代课,请重新输入！')
            else:print('输入错误，请重新输入！')

    def update_class(self,school_class,school_obj,info):
        course_obj,teacher_name,choose_course=self.choose_class(school_class,school_obj,info)
        while True:
            for i in course_obj['class_list']:
                print(i)
            choose_class = input('请输入选择的班级：')
            if choose_class in course_obj['class_list']:
                if choose_class not in course_obj['tea_list']:
                    info[school_obj]['course_list'][choose_course]['tea_list'][teacher_name].append(choose_class)
                    self.update_info(info)
                    break
                else:print('讲师[%s]已经带了这个班,请重新输入！'%teacher_name)
            else:print('班级不存在，请重新输入！')
