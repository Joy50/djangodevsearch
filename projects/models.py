from django.db import models
import uuid
from users.models import Profile

# Create your models here.
class Project(models.Model):
    owner = models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True,null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True,blank=True)
    feature_image = models.ImageField(null=True,blank=True,default="icon.svg")
    demo_link = models.CharField(max_length=2000)
    source_link =  models.CharField(max_length=2000)
    tags = models.ManyToManyField('Tag',blank=True)
    vote_total = models.IntegerField(default = 0, null= True, blank = True)
    vote_ratio = models.IntegerField(default = 0, null= True, blank = True)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True, editable = False)

    def __str__(self):
        return self.title
    
class Review(models.Model):
    VOTE_TYPE = (
        ('up',"UP Vote"),
        ('down',"Down Vote")
    )
    owner = models.ForeignKey(Profile,null=True,blank=True,on_delete=models.CASCADE)
    project = models.ForeignKey(Project,on_delete = models.CASCADE)
    body = models.TextField(null=True, blank = True)
    value = models.CharField(max_length = 200,choices = VOTE_TYPE)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True, editable = False)
    
    def __str__(self):
        return self.value
    

class Tag(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True, editable = False)

    def __str__(self):
        return self.name    
