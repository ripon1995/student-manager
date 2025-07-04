import uuid
from django.db import models


class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=20, verbose_name='First Name')
    last_name = models.CharField(max_length=20, verbose_name='Last Name')
    guardian_name = models.CharField(max_length=30, verbose_name='Guardian Name', null=True, blank=True)
    contact_number = models.CharField(max_length=20, verbose_name='Contact Number')
    guardian_contact_number = models.CharField(max_length=20, verbose_name='Guardian Contact Number', null=True,
                                               blank=True)
    start_date = models.DateField(auto_now_add=True, verbose_name='Start Date')

    class Meta:
        db_table = 'student'
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' - ' + str(self.start_date.month) + '/' + str(
            self.start_date.year)
