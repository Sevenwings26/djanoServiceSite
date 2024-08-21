from django.db import models


# Create your models here.
class GeneralInfo(models.Model):
    company_name = models.CharField(max_length=222, default="Company Name")
    location = models.CharField(max_length=300)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    open_hours = models.CharField(max_length=100, blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
        # blank = true - allows an admin to create record without passing value to it.. 
        # null = True - allow the database to store empty value, allows users...
    def __str__(self):
        return self.company_name


class Service(models.Model):
    icon = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=355, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    user_image = models.CharField(max_length=225, blank=True, null=True)
    star_count = [
        (1,'One'),
        (2,'Two'),
        (3,'Three'),
        (4,'Four'),
        (5,'Five'),
    ]
    rating_count = models.IntegerField(choices=star_count)
    
    username = models.CharField(max_length=200)
    user_job_title = models.CharField(max_length=100)
    review = models.TextField()

    def __str__(self):
        return f"{self.username} - job-tile {self.user_job_title}"
    

