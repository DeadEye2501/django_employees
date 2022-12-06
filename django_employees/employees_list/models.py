from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    head_department = models.ForeignKey(
        to='Department', on_delete=models.CASCADE, null=True, blank=True,
        related_name='subdepatments', verbose_name='Отдел')

    @property
    def has_subdepartments(self):
        return self.subdepatments.exists()

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100, verbose_name='ФИО')
    position = models.CharField(max_length=100, verbose_name='Должность')
    job_started = models.DateField(verbose_name='Начало работы')
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Зарплата')
    department = models.ForeignKey(
        to=Department, on_delete=models.SET_NULL, null=True, blank=True, default=None,
        related_name='employees', verbose_name='Отдел')

    def __str__(self):
        dep = self.department if self.department else 'без отдела'
        return self.name
