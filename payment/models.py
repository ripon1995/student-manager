from django.db import models

from course.models import Course
from student.models import Student


class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_for_month = models.CharField(max_length=7)  # Format: YYYY-MM
    date = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='payments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='payments')

    def __str__(self):
        return f"Payment of {self.amount} on {self.date.strftime('%Y-%m-%d %H:%M:%S')}"

    class Meta:
        db_table = 'payment'
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'
        ordering = ['-date']  # Orders by date descending by default
