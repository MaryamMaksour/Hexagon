from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    industry_sector = models.TextField(max_length=100)
    target_market = models.TextField(max_length=100)
    unique_value_proposition = models.TextField()
    key_objectives = models.TextField()
    
    
class Project2(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    customer_segments = models.TextField()
    value_proposition = models.TextField()
    channels = models.TextField()
    customer_relationships = models.TextField()
    revenue_streams = models.TextField()
    key_resources = models.TextField()
    key_activities = models.TextField()
    key_partners = models.TextField()
    cost_structure = models.TextField()

class questions(models.Model):
    name = models.TextField()
    title = models.TextField()
    description = models.TextField()
    
    def __str__(self):
        return self.title
    