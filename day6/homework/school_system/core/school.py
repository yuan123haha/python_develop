# Author:haha
import pickle,os

class School(object):
    def __init__(self,name,addr):
        self.name=name
        self.addr=addr

    def update_info(self,info):
        info_file = open(r'../db/info.json', 'wb')
        pickle.dump(info, info_file)
        info_file.close()

    def create_class(self,classes_obj,course_list,info):
        while True:
            for i in course_list:
                print(i)
            choose_course=input('请输入匹配的课程：')
            if choose_course in course_list:
                for i in course_list[choose_course]['class_list']:
                    print(i)
                class_name = input('请输入新班级名字：')
                if class_name not in course_list[choose_course]['class_list']:
                    class_data={}
                    info[self.name]['course_list'][choose_course]['class_list'][class_name]=class_data
                    print('school:[%s] create class [%s] belongs to course [%s]'%(self.name,class_name,choose_course))
                    self.update_info(info)
                    break
                else:print('班级已存在，请重新输入！')
            else:
                print('输入错误，请重新输入！')

    def create_course(self,obj,info):
        print('school:[%s] create course [%s]'%(self.name,obj.name))
        course_data={}
        course_data['cycle']=obj.cycle
        course_data['price']=obj.price
        course_data['class_list']={}
        course_data['tea_list']={}

        info[self.name]['course_list'][obj.name]=course_data
        self.update_info(info)


    def creat_teacher(self,obj,course_list,info):
        while True:
            for i in course_list:
                print(i)
            choose_course=input('请输入匹配的课程：')
            if choose_course in course_list:
                for i in course_list[choose_course]['class_list']:
                    print(i)
                choose_class = input('请输入匹配的班级：')
                if choose_class in course_list[choose_course]['class_list']:
                    teacher_name = input('请输入讲师姓名：')
                    if teacher_name not in course_list[choose_course]['tea_list']:
                        print('school:[%s] creat teacher [%s] in course[%s] class[%s]'%(self.name,obj.name,choose_course,choose_class))
                        teacher_data = []
                        teacher_data.append(choose_class)
                        course_list[choose_course]['tea_list'][teacher_name]=teacher_data
                    elif choose_class not in course_list[choose_course]['tea_list'][teacher_name]:
                        course_list[choose_course]['tea_list'][teacher_name].append(choose_class)
                        print('school:[%s] creat teacher [%s] in course[%s] class[%s]'%(self.name,obj.name,choose_course,choose_class))
                    else:print('该班级已经被该老师带了！')
                    self.update_info(info)
                    break
                else:print('班级不存在，请重新输入！')
            else:print('输入错误，请重新输入！')