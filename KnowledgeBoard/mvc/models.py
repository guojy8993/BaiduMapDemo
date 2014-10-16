#author guojingyu
#date      Oct 11, 2014
from django.db import models

class Doc(models.Model):
    #id auto field :primary key ,auto_increment
    title = models.CharField(max_length=50,null=False,blank=False)
    content = models.CharField(max_length=1000)
    create_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50,blank=False,null=False)
    
    def __str__(self):
        return " CreateAt:<%s> Title:<%s> Content:<%s> Author:<%s> "%(str(self.create_at),self.title,self.content,self.author)

class User(models.Model):
    
    user = models.CharField(max_length=50,null=False,blank=False)
    password = models.CharField(max_length=50,null=False,blank=False)
    email = models.EmailField(max_length=50,null=False,blank=False)
    create_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return " User: %s  %s %s"%(self.user,self.email,self.create_date)