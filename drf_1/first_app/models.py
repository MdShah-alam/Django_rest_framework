from django.db import models

# Create your models here.

class StudentData(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=30)
    roll = models.IntegerField()
    
    def __str__(self):
        return f'name : {self.name} , roll : {self.roll}'
    
class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(StudentData , on_delete=models.CASCADE , related_name='courses' , default=None)
    name = models.CharField(max_length=30)
    marks = models.IntegerField()
    
    def __str__(self):
        return f'name : {self.name} , marks : {self.marks}'
    