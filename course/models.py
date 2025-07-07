import uuid
from django.db import models

from student.models import Student


class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, verbose_name='Course Title')
    description = models.CharField(max_length=100, verbose_name='Course Description', null=True, blank=True)
    course_fee = models.IntegerField(default=1000, verbose_name='Course Fee(BDT)')
    days = models.CharField(max_length=30, verbose_name='Days', help_text='e.g. sat/mon/wed')
    time = models.CharField(max_length=20, verbose_name='Time', help_text='e.g. 4 PM')
    capacity = models.IntegerField(default=40, verbose_name='Capacity')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    students = models.ManyToManyField(Student, verbose_name='Students', blank=True, related_name='courses')
    course_quote = models.CharField(max_length=200, verbose_name='Course Quote', null=True, blank=True)

    class Meta:
        db_table = 'course'
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ['-created_at']

    def __str__(self):
        return self.title + ' - ' + str(self.created_at.month) + '/' + str(self.created_at.year)
