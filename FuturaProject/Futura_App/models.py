from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class Login(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_trainer = models.BooleanField(default=False)


class Technologies(models.Model):
    name = models.CharField(max_length=100,null=True, blank=True)

    def __str__(self):
        return self.name


class Trainer(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name='nurse')
    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=250, null=True, blank=True)
    technology = models.ForeignKey(Technologies, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name='students')
    date = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=250, null=True, blank=True)
    location = models.CharField(max_length=250, null=True, blank=True)
    district = models.CharField(max_length=250, null=True, blank=True)
    qualification = models.CharField(max_length=250, null=True, blank=True)
    branch = models.CharField(max_length=250, null=True, blank=True)
    college = models.CharField(max_length=250, null=True, blank=True)
    year_of_passout = models.CharField(max_length=250, null=True, blank=True)
    university = models.CharField(max_length=250, null=True, blank=True)
    phone_no = models.CharField(max_length=250, null=True, blank=True)
    whatsapp_no = models.CharField(max_length=250, null=True, blank=True)
    email_id = models.EmailField(null=True, blank=True)
    guardian_name = models.CharField(max_length=250, null=True, blank=True)
    guardian_phno = models.CharField(max_length=250, null=True, blank=True)
    internship_project = models.CharField(max_length=250, null=True, blank=True)
    mod_of_class = models.CharField(max_length=250, null=True, blank=True)
    technology = models.ForeignKey(Technologies, on_delete=models.CASCADE, null=True, blank=True)
    duration = models.CharField(max_length=250, null=True, blank=True)
    How_do_you_reach_us = models.CharField(max_length=250, null=True, blank=True)
    staff = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Sections(models.Model):
    technology=models.ForeignKey(Technologies, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name


class Evaluation(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING, null=True, blank=True)
    technology = models.ForeignKey(Technologies, on_delete=models.CASCADE, null=True, blank=True)
    evaluation_date = models.DateField(null=True, blank=True)
    evaluation_section = models.ForeignKey(Sections, on_delete=models.DO_NOTHING, null=True, blank=True)
    mcq=models.IntegerField(null=True, blank=True)
    machine_test=models.IntegerField(null=True, blank=True)
    evaluation=models.IntegerField(null=True, blank=True)
    total_mark=models.IntegerField(null=True, blank=True)





class Slot(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.start_time.strftime('%H:%M:%S')} - {self.end_time.strftime('%H:%M:%S')}"



class Schedule(models.Model):
    date =models.DateField()
    trainers = models.ForeignKey(Trainer, on_delete=models.DO_NOTHING, null=True, blank=True)
    students = models.ManyToManyField(Student, null=True,blank=True)
    slot = models.ForeignKey(Slot, on_delete=models.DO_NOTHING, null=True, blank=True)
    technology=models.ForeignKey(Technologies,on_delete=models.CASCADE,null=True, blank=True)




class Person(models.Model):
    name = models.CharField(max_length=250, null=True)
    mod = models.CharField(max_length=250, null=True)
    technology = models.CharField(max_length=250, null=True)
    join_date = models.DateField(null=True)
    duration = models.CharField(max_length=250, null=True)
    staff = models.CharField(max_length=250, null=True)
    month = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name or f"Person {self.id}"

class Attendance(models.Model):
    date=models.DateField()
    schedule=models.ForeignKey(Schedule,on_delete=models.DO_NOTHING,null=True, blank=True)
    students=models.ForeignKey(Student,on_delete=models.DO_NOTHING,null=True, blank=True)
