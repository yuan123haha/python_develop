# Author:haha

class School(object):
    def __init__(self,name,addr):
        self.name=name
        self.addr=addr
        self.student=[]
        self.staff=[]

    def enroll(self,stu_obj):
        print('%s enroll student[%s]'%(self.name,stu_obj.name))
        self.student.append(stu_obj)

    def hire(self,staff_obj):
        print('%s hire staff[%s]'%(self.name,staff_obj.name))
        self.staff.append(staff_obj)

class SchoolMenber(object):
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    def tell(self):
        print('[%s] is telling... '%self.name)

class Teacher(SchoolMenber):
    def __init__(self,name,age,sex,salary,course):
        super(Teacher,self).__init__(name,age,sex)
        self.salary=salary
        self.course=course

    def tell(self):
        print('''
        info of Teacher[%s]
        TeacherName:%s
        TeacherAge:%s
        TeacherSex:%s
        TeacherSalary:%s
        TeacherCourse:%s
        '''%(self.name,self.name,self.age,self.sex,self.salary,self.course))

    def teach(self):
        print('teacher [%s] teach course[%s]'%(self.name,self.course))

class Student(SchoolMenber):
    def __init__(self,name,age,sex,stu_id,grade):
        super(Student,self).__init__(name,age,sex)
        self.stu_id=stu_id
        self.grade=grade

    def tell(self):
        print('''
        info of Student[%s]
        StudentName:%s
        StudentAge:%s
        StudentSex:%s
        StudentStu_id:%s
        StudentGrade:%s
        ''' % (self.name, self.name, self.age, self.sex, self.stu_id, self.grade))

    def pay_tuition(self,amount):
        print('student[%s] has pay_tuition $[%s]'%(self.name,amount))

school=School('川化','青白江')
t1=Teacher('YoYo',35,'F',5000,'Python')
t2=Teacher('QQ',40,'M',8000,'go')

s1=Student('haha',15,'F',25,'Python')
s2=Student('enen',19,'M',31,'go')

t1.tell()
#输出：
'''
        info of Teacher[YoYo]
        TeacherName:YoYo
        TeacherAge:35
        TeacherSex:F
        TeacherSalary:5000
        TeacherCourse:Python
'''
s1.tell()
#输出：
'''
        info of Student[haha]
        StudentName:haha
        StudentAge:15
        StudentSex:F
        StudentStu_id:25
        StudentGrade:Python
'''
school.enroll(s1)
#输出：川化 enroll student[haha]
school.enroll(s2)
#输出：川化 enroll student[enen]
school.hire(t1)
#输出：川化 hire staff[YoYo]
school.hire(t2)
#输出：川化 hire staff[QQ]

school.student[0].pay_tuition(500)
#输出：student[haha] has pay_tuition $[500]
print(school.staff)
#输出：[<__main__.Teacher object at 0x00000000027FAE80>, <__main__.Teacher object at 0x00000000027FAEB8>]

for staff in school.staff:
    staff.teach()
#输出：
'''
teacher [YoYo] teach course[Python]
teacher [QQ] teach course[go]
'''