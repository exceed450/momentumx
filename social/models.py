from django.db import models
from django.contrib.auth.models import User


class InvestmentIdea(models.Model):
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    date_added = models.DateTimeField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    picture_or_video_URL =  models.CharField(max_length=250, blank=True, null=True)
    recommendations = models.IntegerField(blank=True, null=True, default=0)


class IdeaComment(models.Model):
    comment = models.CharField(max_length=250)
    date_added = models.DateTimeField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    idea = models.ForeignKey(InvestmentIdea, on_delete=models.CASCADE)


class PlanComment(models.Model):
    title = models.CharField(max_length=250)
    date_added = models.DateTimeField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)


class InvestmentPlan(models.Model):
    date_added = models.DateTimeField()
    comments = models.ForeignKey(PlanComment, on_delete=models.CASCADE)
    recommendations = models.IntegerField()


class Recommendations(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField()
    like = models.BooleanField()

