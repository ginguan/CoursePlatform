from django.db import models
# from DjangoUeditor.models import UEditorField

from apps.users.models import BaseModel
from apps.users.models import UserProfile


class City(BaseModel):
    name = models.CharField(max_length=20, verbose_name=u"city_name")
    desc = models.CharField(max_length=200, verbose_name=u"description")

    class Meta:
        verbose_name = "city"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseOrg(BaseModel):
    tag = models.CharField(default="popular", max_length=10, verbose_name="organization_tag")
    name = models.CharField(max_length=50, verbose_name="机构名称")
    # desc = UEditorField(verbose_name="description", width=600, height=300, imagePath="courses/ueditor/images/",
                       # filePath="courses/ueditor/files/", default="")
    description =models.TextField(verbose_name="description")
    category = models.CharField(default="pxjg", verbose_name="organization_catergory", max_length=4,
                                choices=(("orga", "organization"), ("self", "self-employed"), ("univ", "university")))
    click_nums = models.IntegerField(default=0, verbose_name="clicked_num")
    fav_nums = models.IntegerField(default=0, verbose_name="fav_num")
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name="logo", max_length=100)
    address = models.CharField(max_length=150, verbose_name="org_address")
    students = models.IntegerField(default=0, verbose_name="student_num")
    course_nums = models.IntegerField(default=0, verbose_name="course_num")

    is_auth = models.BooleanField(default=False, verbose_name="is_verified")
    is_gold = models.BooleanField(default=False, verbose_name="is_golden")

    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="org_city")

    def courses(self):
        courses = self.course_set.filter(is_classics=True)[:3]
        return courses

    class Meta:
        verbose_name = "organization"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Teacher(BaseModel):
    user = models.OneToOneField(UserProfile, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="user")
    org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, verbose_name="teacher_org")
    name = models.CharField(max_length=50, verbose_name=u"teacher_name")
    work_years = models.IntegerField(default=0, verbose_name="work_years")
    work_company = models.CharField(max_length=50, verbose_name="work_company")
    work_position = models.CharField(max_length=50, verbose_name="work_position")
    points = models.CharField(max_length=50, verbose_name="points")
    click_nums = models.IntegerField(default=0, verbose_name="click_nums")
    fav_nums = models.IntegerField(default=0, verbose_name="fav_nums")
    age = models.IntegerField(default=18, verbose_name="age")
    image = models.ImageField(upload_to="teacher/%Y/%m", verbose_name="profile_pic", max_length=100)

    class Meta:
        verbose_name = "teacher"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def course_nums(self):
        return self.course_set.all().count()
