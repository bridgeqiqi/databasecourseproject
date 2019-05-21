# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    admin = models.ForeignKey('PersonalInformation', models.DO_NOTHING, primary_key=True)
    admin_name = models.CharField(max_length=10)
    admin_sex = models.CharField(max_length=2)
    admin_age = models.IntegerField()
    yxh = models.ForeignKey('Faculty', models.DO_NOTHING, db_column='yxh')

    class Meta:
        managed = True
        db_table = 'admin'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Choosecourse(models.Model):
    course = models.ForeignKey('Course', models.DO_NOTHING, primary_key=True)
    student = models.ForeignKey('Student', models.DO_NOTHING)
    teacher = models.ForeignKey('Teacher', models.DO_NOTHING)
    class_time = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'choosecourse'
        unique_together = (('course', 'student', 'teacher'),)


class Course(models.Model):
    course_id = models.CharField(primary_key=True, max_length=8)
    teacher = models.ForeignKey('Teacher', models.DO_NOTHING)
    course_name = models.CharField(max_length=20)
    teacher_name = models.CharField(max_length=10)
    credit = models.IntegerField()
    class_time = models.CharField(max_length=100)
    class_location = models.CharField(max_length=10)
    yxh = models.ForeignKey('Faculty', models.DO_NOTHING, db_column='yxh')
    cur_stu_num = models.IntegerField()
    total_stu_num = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'course'
        unique_together = (('course_id', 'teacher'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Faculty(models.Model):
    yxh = models.CharField(primary_key=True, max_length=20)
    faculty_name = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'faculty'


class Grade(models.Model):
    course = models.ForeignKey(Course, models.DO_NOTHING, primary_key=True)
    student = models.ForeignKey('Student', models.DO_NOTHING)
    teacher = models.ForeignKey('Teacher', models.DO_NOTHING)
    routine_score = models.FloatField()
    exam_score = models.FloatField()
    total_score = models.FloatField()

    class Meta:
        managed = True
        db_table = 'grade'
        unique_together = (('course', 'student', 'teacher'),)


class PersonalInformation(models.Model):
    username = models.CharField(primary_key=True, max_length=8)
    psd = models.CharField(max_length=16)
    identifier = models.CharField(max_length=10)

    class Meta:
        managed = True
        db_table = 'personal_information'


class Student(models.Model):
    student = models.ForeignKey(PersonalInformation, models.DO_NOTHING, primary_key=True)
    student_name = models.CharField(max_length=10)
    student_sex = models.CharField(max_length=2)
    student_age = models.IntegerField()
    yxh = models.ForeignKey(Faculty, models.DO_NOTHING, db_column='yxh')

    class Meta:
        managed = True
        db_table = 'student'


class Teacher(models.Model):
    teacher = models.ForeignKey(PersonalInformation, models.DO_NOTHING, primary_key=True)
    teacher_name = models.CharField(max_length=10)
    teacher_sex = models.CharField(max_length=2)
    teacher_age = models.IntegerField()
    yxh = models.ForeignKey(Faculty, models.DO_NOTHING, db_column='yxh')

    class Meta:
        managed = True
        db_table = 'teacher'


class Constants(models.Model):
    id = models.IntegerField(primary_key=True)
    is_choosing_course = models.CharField(max_length=8)
    is_uploading_score = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'constants'