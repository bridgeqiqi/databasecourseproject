from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
# Create your views here.
from modelapp import models
import json
import pymysql


def test(request):
    return HttpResponse("hello")

def test2(request):
    userlist = models.Admin.objects.all()
    real_userlist = serializers.serialize('json',userlist)
    print(real_userlist)
    return HttpResponse(real_userlist)

# 查询所有学生信息
def search_studentinfo_all(request):
    response = {}
    try:
        studentlist = models.Student.objects.all()
        real_studentlist = serializers.serialize('json',studentlist)
        response['data'] = json.loads(real_studentlist)
        response['msg'] = 'success'
        response['error'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error'] = 1
    return JsonResponse(response)

# 查询所有老师信息
def search_teacherinfo_all(request):
    response = {}
    try:
        teacherlist = models.Teacher.objects.all()
        real_teacherlist = serializers.serialize('json',teacherlist)
        response['data'] = json.loads(real_teacherlist)
        response['msg'] = 'success'
        response['error'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error'] = 1
    return JsonResponse(response)

# 查询所有课程信息
def search_courseinfo_all(request):
    response = {}
    try:
        courselist = models.Course.objects.all()
        real_courselist = serializers.serialize('json',courselist)
        response['data'] = json.loads(real_courselist)
        response['msg'] = 'success'
        response['error'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error'] = 1
    return JsonResponse(response)

# 插入一条学生信息
def insert_studentinfo(request):
    response = {}
    if request.method == 'POST':
        try:
            print(request)
            student_id = request.POST['student_id']
            student_name = request.POST['student_name']
            student_sex = request.POST['student_sex']
            student_age = request.POST['student_age']
            faculty = request.POST['faculty']
            print(student_id)
            print(student_name)
            print(faculty)
            models.PersonalInformation.objects.create(username=student_id,psd=student_id,identifier='学生')
            student_id = models.PersonalInformation.objects.get(username=student_id)
            faculty = models.Faculty.objects.get(yxh=faculty)
            models.Student.objects.create(student=student_id,student_name=student_name,student_age=student_age,student_sex=student_sex,yxh=faculty)
            response['msg'] = "success"
            response['error'] = 0
        except Exception as e:
            print(e)
            response['msg'] = str(e)
            response['error'] = 1
    else:
        response['msg'] = 'require get method'
        response['msg'] = 1
    return JsonResponse(response)

# 插入一条老师信息
def insert_teacherinfo(request):
    response = {}
    if request.method == 'POST':
        try:
            print(request)
            teacher_id = request.POST['teacher_id']
            teacher_name = request.POST['teacher_name']
            teacher_sex = request.POST['teacher_sex']
            teacher_age = request.POST['teacher_age']
            faculty = request.POST['faculty']
            print(teacher_id)
            print(teacher_name)
            models.PersonalInformation.objects.create(username=teacher_id,psd=teacher_id,identifier='教师')
            teacher_id = models.PersonalInformation.objects.get(username=teacher_id)
            faculty = models.Faculty.objects.get(yxh=faculty)
            models.Teacher.objects.create(teacher=teacher_id,teacher_name=teacher_name,teacher_age=teacher_age,teacher_sex=teacher_sex,yxh=faculty)
            response['msg'] = "success"
            response['error'] = 0
        except Exception as e:
            print(e)
            response['msg'] = str(e)
            response['error'] = 1
    else:
        response['msg'] = 'require post method'
        response['msg'] = 1
    return JsonResponse(response)

# 插入一条课程信息
def insert_courseinfo(request):
    response = {}
    if request.method == 'POST':
        try:
            print(request)
            course_id = request.POST['course_id']
            teacher = request.POST['teacher_id']
            course_name = request.POST['course_name']
            teacher_name = request.POST['teacher_name']
            credit = request.POST['credit']
            class_time = request.POST['class_time']
            class_location = request.POST['class_location']
            total_stu_num = request.POST['total_stu_num']
            # print(models.Teacher.objects.get(teacher=teacher).yxh_id)
            yxh = models.Faculty.objects.get(yxh=models.Teacher.objects.get(teacher=teacher).yxh_id)
            teacher = models.Teacher.objects.get(teacher=teacher)

            models.Course.objects.create(course_id=course_id,teacher=teacher,course_name=course_name,
                                         teacher_name=teacher_name,credit=credit,class_time=class_time,
                                         class_location=class_location,yxh=yxh,cur_stu_num=0,total_stu_num=total_stu_num)
            response['msg'] = "success"
            response['error'] = 0
        except Exception as e:
            print(e)
            response['msg'] = str(e)
            response['error'] = 1
    else:
        response['msg'] = 'require post method'
        response['msg'] = 1
    return JsonResponse(response)

# 修改学生信息
def update_studentinfo(request):
    response = {}
    if request.method == 'POST':
        try:
            student_id = request.POST['student_id']
            student_name = request.POST['student_name']
            student_sex = request.POST['student_sex']
            student_age = request.POST['student_age']
            yxh = request.POST['faculty']

            faculty = models.Faculty.objects.get(yxh=yxh)

            student = models.Student.objects.get(student=student_id,student_name=student_name,student_sex=student_sex)
            student.student_age = student_age
            student.yxh = faculty

            student.save()

            response['msg'] = "success"
            response['error'] = 0
        except Exception as e:
            print(e)
            response['msg'] = str(e)
            response['error'] = 1
    else:
        response['msg'] = 'require post method'
        response['msg'] = 1
    return JsonResponse(response)

# 修改教师信息
def update_teacherinfo(request):
    response = {}
    if request.method == 'POST':
        try:
            teacher_id = request.POST['teacher_id']
            teacher_name = request.POST['teacher_name']
            teacher_sex = request.POST['teacher_sex']
            teacher_age = request.POST['teacher_age']
            yxh = request.POST['faculty']

            faculty = models.Faculty.objects.get(yxh=yxh)

            teacher = models.Teacher.objects.get(teacher=teacher_id,teacher_name=teacher_name,teacher_sex=teacher_sex)
            teacher.teacher_age = teacher_age
            teacher.yxh = faculty

            teacher.save()

            response['msg'] = "success"
            response['error'] = 0
        except Exception as e:
            print(e)
            response['msg'] = str(e)
            response['error'] = 1
    else:
        response['msg'] = 'require post method'
        response['msg'] = 1
    return JsonResponse(response)

# 修改课程信息
def update_courseinfo(request):
    response = {}
    if request.method == 'POST':
        try:
            course_id = request.POST['course_id']
            course_name = request.POST['course_name']
            credit = request.POST['credit']
            teacher_id = request.POST['teacher_id']
            teacher_name = request.POST['teacher_name']
            class_time = request.POST['class_time']
            class_location = request.POST['class_location']
            total_stu_num = request.POST['total_stu_num']

            course = models.Course.objects.get(course_id=course_id,teacher=teacher_id)
            course.class_time = class_time
            course.class_location = class_location
            course.total_stu_num = total_stu_num

            course.save()

            response['msg'] = "success"
            response['error'] = 0
        except Exception as e:
            print(e)
            response['msg'] = str(e)
            response['error'] = 1
    else:
        response['msg'] = 'require post method'
        response['msg'] = 1
    return JsonResponse(response)

# 删除学生信息
def delete_studentinfo(request):
    response = {}
    if request.method == 'POST':
        try:
            student_id = request.POST['student_id']

            student = models.Student.objects.get(student=student_id)
            student_ = models.Choosecourse.objects.filter(student=student)
            if student_:
                response['msg'] = "学生已选课，不能删除"
                response['error'] = 1
            else:
                models.Student.objects.filter(student=student).delete()
                models.PersonalInformation.objects.filter(username=student_id).delete()
                response['msg'] = "success"
                response['error'] = 0
        except Exception as e:
            print(e)
            response['msg'] = str(e)
            response['error'] = 1
    else:
        response['msg'] = 'require post method'
        response['msg'] = 1
    return JsonResponse(response)

# 删除教师信息
def delete_teacherinfo(request):
    response = {}
    if request.method == 'POST':
        try:
            teacher_id = request.POST['teacher_id']

            teacher = models.Teacher.objects.get(teacher=teacher_id)
            teacher_ = models.Course.objects.filter(teacher=teacher)
            if teacher_:
                response['msg'] = "教师已开课，不能删除"
                response['error'] = 1
            else:
                models.Teacher.objects.filter(teacher=teacher).delete()
                models.PersonalInformation.objects.filter(username=teacher_id).delete()
                response['msg'] = "success"
                response['error'] = 0
        except Exception as e:
            print(e)
            response['msg'] = str(e)
            response['error'] = 1
    else:
        response['msg'] = 'require post method'
        response['msg'] = 1
    return JsonResponse(response)


# 删除课程信息
def delete_courseinfo(request):
    response = {}
    if request.method == 'POST':
        try:
            course_id = request.POST['course_id']
            teacher_id = request.POST['teacher_id']

            db = pymysql.connect('localhost', 'root', 'mysql', 'databaseteaching', port=3306, use_unicode=True,
                                 charset='utf8')
            cursor = db.cursor()
            sql = "select sum(grade.total_score) from grade " \
                  "where grade.course_id = '%s' and grade.teacher_id = '%s'" % (course_id, teacher_id)
            print(sql)
            cursor.execute(sql)
            score = cursor.fetchall()[0][0]
            db.close()
            print(score)
            if score is None or score<5:
                print("true")
                models.Choosecourse.objects.filter(course=course_id,teacher=teacher_id).delete()
                course = models.Course.objects.get(course_id=course_id,teacher=teacher_id)
                course.class_time = '不开'
                course.total_stu_num = 0
                course.cur_stu_num = 0
                course.save()
                response['msg'] = "success"
                response['error'] = 0
            else:
                response['msg'] = "课程已经进行，不能删除"
                response['error'] = 1
        except Exception as e:
            print(e)
            response['msg'] = str(e)
            response['error'] = 1
    else:
        response['msg'] = 'require post method'
        response['msg'] = 1
    return JsonResponse(response)


# 教师端
def search_courseinfo_ownedby(request):
    response = {}
    if request.method == 'POST':
        # try:
        teacher_id = request.POST['teacher_id']
        teacher = models.Teacher.objects.get(teacher=teacher_id)
        courselist = models.Course.objects.filter(teacher=teacher)
        real_courselist = serializers.serialize('json',courselist)
        response['data'] = json.loads(real_courselist)
        response['msg'] = 'success'
        response['error'] = 0
        # except Exception as e:
        #     response['msg'] = str(e)
        #     response['error'] = 1
    else:
        response['msg'] = 'require post method'
        response['error'] = 1

    return JsonResponse(response)


def search_studentinfo_by_id(request):
    response = {}
    if request.method == 'POST':
        try:
            course_id = request.POST['course_id']
            teacher_id = request.POST['teacher_id']

            db = pymysql.connect('localhost', 'root', 'mysql', 'databaseteaching', port=3306, use_unicode=True,
                                 charset='utf8')
            cursor = db.cursor()
            sql = "select * from student,choosecourse,faculty where student.yxh = faculty.yxh and student.student_id=choosecourse.student_id and choosecourse.course_id='%s' and choosecourse.teacher_id='%s';"%(course_id,teacher_id)
            print(sql)
            cursor.execute(sql)
            studentlist = cursor.fetchall()
            db.close()
            # print(studentlist)
            studentdict = []
            for list in studentlist:
                temp_dict = dict()
                temp_dict['student_id'] = list[0]
                temp_dict['student_name'] = list[1]
                temp_dict['student_sex'] = list[2]
                temp_dict['student_age'] = list[3]
                temp_dict['faculty'] = list[10]
                studentdict.append(temp_dict)
            print(studentdict)
            response['data'] = studentdict
            response['msg'] = 'success'
            response['error'] = 0
        except Exception as e:
            response['msg'] = str(e)
            response['error'] = 1
    else:
        response['msg'] = 'require post method'
        response['error'] = 1

    return JsonResponse(response)


# 根据课程号和教师号 查询所有选了这门课的学生的情况和成绩
def search_score_by_id(request):
    response = {}
    if request.method == 'POST':
        # try:
        course_id = request.POST['course_id']
        teacher_id = request.POST['teacher_id']

        db = pymysql.connect('localhost', 'root', 'mysql', 'databaseteaching', port=3306, use_unicode=True,
                             charset='utf8')
        cursor = db.cursor()
        sql = "select student.student_name,student.student_id,grade.routine_score,grade.exam_score,grade.total_score from student,grade " \
                "where student.student_id = grade.student_id and grade.course_id = '%s' and grade.teacher_id = '%s'" % (course_id,teacher_id)
        print(sql)
        cursor.execute(sql)
        studentlist = cursor.fetchall()
        print(studentlist)
        db.close()

        studentdict = []
        for list in studentlist:
            temp_dict = dict()
            temp_dict['student_name'] = list[0]
            temp_dict['student_id'] = list[1]
            temp_dict['routine_score'] = list[2]
            temp_dict['exam_score'] = list[3]
            temp_dict['total_score'] = list[4]
            studentdict.append(temp_dict)
        print(studentdict)

        # studentlist = models.Grade.objects.filter(course=course_id,teacher=teacher_id)
        # real_studentlist = serializers.serialize('json', studentdict)
        response['data'] = studentdict
        response['msg'] = 'success'
        response['error'] = 0
        # except Exception as e:
        #     response['msg'] = str(e)
        #     response['error'] = 1
        #     print(e)
    else:
        response['msg'] = 'require post method'
        response['error'] = 1
    return JsonResponse(response)


# 登分
def upload_grade(request):
    response = {}
    if request.method == 'POST':
        course_id = request.POST['course_id']
        student_id = request.POST['student_id']
        teacher_id = request.POST['teacher_id']
        routine_score = request.POST['routine_score']
        exam_score = request.POST['exam_score']

        print(routine_score)
        print(exam_score)
        print(course_id)
        print(teacher_id)
        print(student_id)

        db = pymysql.connect('localhost', 'root', 'mysql', 'databaseteaching', port=3306, use_unicode=True,
                             charset='utf8')
        cursor = db.cursor()
        sql = "update grade set grade.routine_score='%s',grade.exam_score='%s' where grade.course_id='%s' and grade.student_id='%s' and grade.teacher_id='%s';" % (float(routine_score),float(exam_score),course_id,student_id,teacher_id)
        print(sql)
        cursor.execute(sql)
        print(cursor.fetchall())
        db.commit()
        db.close()


        response['msg'] = 'success'
        response['error'] = 0
    else:
        response['msg'] = 'require post method'
        response['error'] = 1
    return JsonResponse(response)


#根据关键字搜索课程
def search_courseinfo_by(request):
    response = {}
    if request.method == 'POST':
        # try:
        course_id = request.POST['course_id']
        course_name = request.POST['course_name']
        class_time = request.POST['class_time']
        teacher_id = request.POST['teacher_id']
        teacher_name = request.POST['teacher_name']

        course_id_str = str(course_id).strip()
        course_name_str = str(course_name).strip()
        class_time_str = str(class_time).strip()
        teacher_id_str = str(teacher_id).strip()
        teacher_name_str = str(teacher_name).strip()

        if teacher_id_str!='':
            teacher = models.Teacher.objects.get(teacher=teacher_id_str)

        courselist = models.Course.objects.all()
        if course_id_str!='':
            courselist = courselist.filter(course_id=course_id_str)
        if course_name_str!='':
            courselist = courselist.filter(course_name=course_name_str)
        if class_time_str!='':
            courselist = courselist.filter(class_time=class_time_str)
        if teacher_id_str!='' and teacher:
            courselist = courselist.filter(teacher=teacher)
        if teacher_name_str!='':
            courselist = courselist.filter(teacher_name=teacher_name_str)
        real_courselist = serializers.serialize('json', courselist)
        response['data'] = json.loads(real_courselist)
        response['msg'] = 'success'
        response['error'] = 0
        # except Exception as e:
        #     response['msg'] = str(e)
        #     response['error'] = 1
    return JsonResponse(response)



# 选课
def choose_course(request):
    response = {}
    if request.method == 'POST':

        course_id = request.POST['course_id']
        teacher_id = request.POST['teacher_id']
        student_id = request.POST['student_id']
        class_time = request.POST['class_time']

        course = models.Course.objects.get(course_id=course_id)
        teacher = models.Teacher.objects.get(teacher=teacher_id)
        student = models.Student.objects.get(student=student_id)

        models.Choosecourse.objects.create(course=course,teacher=teacher,student=student,class_time=class_time)


        response['msg'] = 'success'
        response['error'] = 0
    else:
        response['msg'] = 'require post method'
        response['error'] = 0
    return JsonResponse(response)

# 查询我选过的课
def search_my_course(request):
    response = {}
    if request.method == 'POST':

        student_id = request.POST['student_id']

        db = pymysql.connect('localhost', 'root', 'mysql', 'databaseteaching', port=3306, use_unicode=True,
                             charset='utf8')
        cursor = db.cursor()
        sql = "select * from choosecourse,course where choosecourse.student_id='%s' and choosecourse.course_id=course.course_id and course.teacher_id=choosecourse.teacher_id and course.class_time=choosecourse.class_time" % (student_id)
        print(sql)
        cursor.execute(sql)
        courselist = cursor.fetchall()
        db.close()
        print(courselist)

        mycourselist = []
        for list in courselist:
            temp_dict = dict()
            temp_dict['course_id'] = list[0]
            temp_dict['course_name'] = list[6]
            temp_dict['credit'] = list[8]
            temp_dict['class_time'] = list[3]
            temp_dict['teacher_id'] = list[2]
            temp_dict['teacher_name'] = list[7]
            temp_dict['class_location'] = list[10]
            mycourselist.append(temp_dict)
        print(mycourselist)
        response['data'] = mycourselist
        response['msg'] = 'success'
        response['error'] = 0
    else:
        response['msg'] = 'require post method'
        response['error'] = 0
    return JsonResponse(response)


# 退课
def quit_course(request):
    response = {}
    if request.method == 'POST':
        student_id = request.POST['student_id']
        teacher_id = request.POST['teacher_id']
        course_id = request.POST['course_id']

        student = models.Student.objects.get(student=student_id)
        teacher = models.Teacher.objects.get(teacher=teacher_id)
        course = models.Course.objects.get(course_id=course_id)

        if models.Grade.objects.get(student=student,teacher=teacher,course=course).total_score > 0:
            response['msg'] = '已登分不能退课'
            response['error'] = 1
        else:
            models.Choosecourse.objects.get(student=student,teacher=teacher,course=course).delete()
            response['msg'] = 'success'
            response['error'] = 0
    else:
        response['msg'] = 'require post method'
        response['error'] = 0
    return JsonResponse(response)


# 查找我选的所有课的成绩
def my_score_all(request):
    response = {}
    if request.method == 'POST':

        student_id = request.POST['student_id']

        db = pymysql.connect('localhost', 'root', 'mysql', 'databaseteaching', port=3306, use_unicode=True,
                             charset='utf8')
        cursor = db.cursor()
        sql = "select * from choosecourse,course,grade where choosecourse.student_id='%s' and choosecourse.course_id=course.course_id and" \
              " course.teacher_id=choosecourse.teacher_id and course.class_time=choosecourse.class_time and" \
              " choosecourse.course_id=grade.course_id and choosecourse.teacher_id=grade.teacher_id and choosecourse.student_id=grade.student_id" % (
            student_id)
        print(sql)
        cursor.execute(sql)
        courselist = cursor.fetchall()
        db.close()
        print(courselist)

        mycourselist = []
        for list in courselist:
            temp_dict = dict()
            temp_dict['course_id'] = list[0]
            temp_dict['course_name'] = list[6]
            temp_dict['credit'] = list[8]
            temp_dict['class_time'] = list[3]
            temp_dict['teacher_id'] = list[2]
            temp_dict['student_id'] = list[1]
            temp_dict['teacher_name'] = list[7]
            temp_dict['total_score'] = list[19]
            mycourselist.append(temp_dict)
        print(mycourselist)
        response['data'] = mycourselist
        response['msg'] = 'success'
        response['error'] = 0
    else:
        response['msg'] = 'require post method'
        response['error'] = 0
    return JsonResponse(response)



# 核对用户名和密码
def check_login(request):
    response = {}
    if request.method == 'POST':
        # try:
        username = request.POST['username']
        password = request.POST['password']
        if models.PersonalInformation.objects.filter(username=username,psd=password):
            response['identifier'] = models.PersonalInformation.objects.filter(username=username,psd=password).get(username=username).identifier
            response['msg'] = 'login success'
            response['error'] = 0
        else:
            response['msg'] = 'login fail'
            response['error'] = 1
    else:
        response['msg'] = 'require post method'
        response['error'] = 1
    return JsonResponse(response)

# 开放选课
def start_choose_course(request):
    response = {}
    try:
        constants = models.Constants.objects.get(id=1)
        constants.is_choosing_course = 'true'
        constants.save()
        response['msg'] = '开放选课'
        response['error'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error'] = 1
    return JsonResponse(response)

# 禁止选课
def stop_choose_course(request):
    response = {}
    try:
        constants = models.Constants.objects.get(id=1)
        constants.is_choosing_course = 'false'
        constants.save()
        response['msg'] = '禁止选课'
        response['error'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error'] = 1
    return JsonResponse(response)

# 开放登分
def start_upload_score(request):
    response = {}
    try:
        constants = models.Constants.objects.get(id=1)
        constants.is_uploading_score = 'true'
        constants.save()
        response['msg'] = '开放登分'
        response['error'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error'] = 1
    return JsonResponse(response)

# 禁止登分
def stop_upload_score(request):
    response = {}
    try:
        constants = models.Constants.objects.get(id=1)
        constants.is_uploading_score = 'false'
        constants.save()
        response['msg'] = '禁止登分'
        response['error'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error'] = 1
    return JsonResponse(response)

# 查询是否开始选课
def search_choose_course(request):
    response = {}
    try:
        response['data'] = models.Constants.objects.get(id=1).is_choosing_course
        response['msg'] = 'success'
        response['error'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error'] = 1
    return JsonResponse(response)

# 查询是否开始登分
def search_upload_score(request):
    response = {}
    try:
        response['data'] = models.Constants.objects.get(id=1).is_uploading_score
        response['msg'] = 'success'
        response['error'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error'] = 1
    return JsonResponse(response)

# 查询是否开始登分
def search_two_states(request):
    response = {}
    try:
        response['is_upload_score'] = models.Constants.objects.get(id=1).is_uploading_score
        response['is_choose_course'] = models.Constants.objects.get(id=1).is_choosing_course
        response['msg'] = 'success'
        response['error'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error'] = 1
    return JsonResponse(response)


# def search_coursescore_by_id(request):
#
#     if request.method == 'POST':
#         kh = request.POST['course_id']
#         jsh = request.POST['teacher_id']
#         Manager
