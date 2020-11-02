from django.db import models
# from DjangoUeditor.models import UEditorField
from datetime import datetime

from apps.users.models import BaseModel
from apps.organizations.models import Teacher
from apps.organizations.models import CourseOrg
# 1. important points
# chapters layers : session -> chapters
'''
4 part of a course
 course Lesson sessions(video) course_resources
'''


# 2. detail char
# 3. char type

class Course(BaseModel):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="insturctpr")
    course_org = models.ForeignKey(CourseOrg, null=True, blank=True, on_delete=models.CASCADE, verbose_name="course_org")

    name = models.CharField(verbose_name="course_name", max_length=100)
    description = models.CharField(verbose_name="course_desc", max_length=300)
    learn_times = models.IntegerField(default=0, verbose_name="learn_time(in mins)")
    difficulty = models.CharField(verbose_name="difficulty",
                                  choices=(("easy", "easy"), ("medium", "medium"), ("hard", "hard")), max_length=6)
    students = models.IntegerField(default=0, verbose_name='students_num')
    fav_nums = models.IntegerField(default=0, verbose_name='fav_nums')
    click_nums = models.IntegerField(default=0, verbose_name="click_nums")
    # notice = models.CharField(verbose_name="notice", max_length=300, default="")
    category = models.CharField(default=u"backend", max_length=20, verbose_name="category")
    tag = models.CharField(default="", verbose_name="course_tag", max_length=10)
    youneed_know = models.CharField(default="", max_length=300, verbose_name="youneed_know")
    teacher_tell = models.CharField(default="", max_length=300, verbose_name="teacher_tell")
    # is_classics = models.BooleanField(default=False, verbose_name="is_classics")
    detail = models.TextField(verbose_name="detail")
    is_banner = models.BooleanField(default=False, verbose_name="is_banner")
    image = models.ImageField(upload_to="courses/%Y/%m", verbose_name="image", max_length=100)

    class Meta:
        verbose_name = "course_info"
        verbose_name_plural = verbose_name


class Lesson(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(verbose_name=u"lesson_name", max_length=100)
    learn_times = models.IntegerField(default=0, verbose_name="learn_time(in mins)")

    # on_delete when deleted,
    # on_delete = SET_NULL , null = True
    class Meta:
        verbose_name = "lesson_info"
        verbose_name_plural = verbose_name


class Video(BaseModel):
    lesson = models.ForeignKey(Lesson, verbose_name="lesson", on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name=u"video_name")
    learn_times = models.IntegerField(default=0, verbose_name=u"video_time(in mins)")
    url = models.CharField(max_length=200, verbose_name=u"url")

    class Meta:
        verbose_name = "video"
        verbose_name_plural = verbose_name


class CourseResource(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="course")
    name = models.CharField(max_length=100, verbose_name=u"course_resource_name")
    file = models.FileField(upload_to="course/resource/%Y/%m", verbose_name="download_url", max_length=200)

    class Meta:
        verbose_name = "video_resource"
        verbose_name_plural = verbose_name
