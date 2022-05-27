from django.db import models

class user(models.Model):
	email=models.CharField(max_length=100,null=False,blank=False)
	password=models.CharField(max_length=20,null=False,blank=False)

class userface(models.Model):
	email=models.CharField(max_length=100,null=False,blank=False)
	url=models.CharField(max_length=100,null=False,blank=False)

class studentface(models.Model):
	studentid=models.CharField(max_length=30,null=False,blank=False)
	url=models.CharField(max_length=100,null=False,blank=False)

class attendence(models.Model):
	studentid=models.CharField(max_length=30,null=False,blank=False)
	datetime=models.CharField(max_length=30,null=False,blank=False)
	status=models.CharField(max_length=30,null=False,blank=False)

types = [('Student', 'Student '), ('Employee', 'Employee')]


class Profile(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    date = models.DateField()
    phone = models.BigIntegerField()
    email = models.EmailField()
    ranking = models.IntegerField()
    profession = models.CharField(max_length=200)
    status = models.CharField(choices=types, max_length=20, null=True, blank=False, default='employee')
    present = models.BooleanField(default=False)
    image = models.ImageField()
    updated = models.DateTimeField(auto_now=True)
    shift = models.TimeField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class LastFace(models.Model):
    last_face = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.last_face