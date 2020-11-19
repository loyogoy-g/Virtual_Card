from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Student(models.Model):
    choice = [
    ('7 Rizal', '7 Rizal'),
    ('7 Bonifacio', '7 Bonifacio'),
    ('7 Del Pilar', '7 Del Pilar'),
    ('8 Nakpil', '8 Nakpil'),
    ('8 Bernal', '8 Bernal'),
    ('8 Joaquin', '8 Joaquin'),
    ('9 Shakespeare', '9 Shakespeare'),
    ('9 Dickens', '9 Dickens'),
    ('9 Twain', '9 Twain'),
    ('10 Einstein', '10 Einstein'),
    ('10 Franklin', '10 Franklin'),
    ('10 Newton', '10 Newton'),
    ('11 ABM', '11 ABM'),
    ('11 GAS/HUMSS', '11 GAS/HUMSS'),
    ('11 STEM', '11 STEM'),
    ('12 ABM', '12 ABM'),
    ('12 GAS/HUMSS', '12 GAS/HUMSS'),
    ('12 STEM', '12 STEM')
  ]
    Name = models.CharField(max_length=100, unique=True)
    LRN = models.CharField(max_length=100, unique=True)
    Status = models.BooleanField(verbose_name="Block Access", default=False)
    Section = models.CharField(max_length=100, choices=choice)
    Quarter = models.CharField(verbose_name="What Quarter ?", choices=[('1', 'First Quarter'), ('2', 'Second Quarter'),('1', 'Third Quarter'),('1', 'Fourth Quarter'),], max_length=100, null=False)

    def __str__(self):
        return self.Name

class FirstQuarter(models.Model):
    Subject = models.CharField(max_length=100)
    Grade = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    Student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="firstgrade")

    def __str__(self):
        return self.Subject

class SecondQuarter(models.Model):
    Subject = models.CharField(max_length=100)
    Grade = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    Student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="secondgrade")

    def __str__(self):
        return self.Subject

class ThirdQuarter(models.Model):
    Subject = models.CharField(max_length=100)
    Grade = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    Student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="thirdgrade")

    def __str__(self):
        return self.Subject

class FourthQuarter(models.Model):
    Subject = models.CharField(max_length=100)
    Grade = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    Student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="fourthgrade")

    def __str__(self):
        return self.Subject