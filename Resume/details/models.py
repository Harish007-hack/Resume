from django.db import models

# Create your models here.

class UserInfo(models.Model):
    skillLang = models.CharField(max_length=1000,)
    skillImg = models.ImageField()
    skillLibrary_1 = models.CharField(max_length=1000,blank=True)
    skillLibrary_2 = models.CharField(max_length=1000,blank=True)
    skillLibrary_3 = models.CharField(max_length=1000,blank=True)
    skillLibrary_4 = models.CharField(max_length=1000,blank=True)
    


    def __str__(self) -> str:
        return self.skillLang
    

class Certificates(models.Model):
    Language = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    skillcertificate_link = models.URLField(blank=True)
    skillcertificate_logo = models.ImageField(blank=True)
    skillcertificate_organiser = models.CharField(max_length=1000,blank=True)


    def __str__(self) -> str:
        return self.Language.skillLang + " Certificates"


class Projects(models.Model):
    projectname = models.CharField(max_length=1000)
    projectdescription = models.TextField(max_length=10000)
    projectphoto = models.ImageField()
    projecturl = models.URLField(blank=True)

    def __str__(self) -> str:
        return self.projectname


class customerinfo(models.Model):
    first_name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=1000)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.first_name + " " +self.last_name