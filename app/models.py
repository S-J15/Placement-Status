from django.db import models

class Division(models.Model):
    div=models.CharField(max_length=2)

    def __str__(self):
        return self.div
    
class Status(models.Model):
    status=models.CharField(max_length=10)

    def __str__(self):
        return self.status

class Student(models.Model):
    prn=models.CharField(max_length=10,unique=True)
    name=models.CharField(max_length=25)
    email=models.EmailField(default="stud@mitwpu.edu.in",null=False)
    phn = models.CharField(max_length=10, blank=True, null=True)
    status=models.ForeignKey(Status,on_delete=models.CASCADE,related_name="s_status")
    div = models.ForeignKey(Division, on_delete=models.CASCADE, related_name="students")
    doc = models.FileField(upload_to='documents/', null=True, blank=True)

    def __str__(self):
        return self.name

