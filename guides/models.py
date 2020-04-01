from django.db import models


class Guide(models.Model):
    title = models.CharField(max_length=255)


# A guide has steps in a particular order


class Step(models.Model):
    title = models.CharField(max_length=255)


# A step has actions in a particular order


class Action(models.Model):
    text = models.TextField()


# A step has verifications in a particular order


class Verification(models.Model):
    text = models.TextField()
