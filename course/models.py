import uuid
from django.db import models

from student.models import Student


class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50, verbose_name='Course Title')
    description = models.CharField(max_length=100, verbose_name='Course Description', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    students = models.ManyToManyField(Student, verbose_name='Students', blank=True, related_name='courses')

    class Meta:
        db_table = 'course'
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ['-created_at']

    def __str__(self):
        return self.title + ' - ' + str(self.created_at.month) + '/' + str(self.created_at.year)
