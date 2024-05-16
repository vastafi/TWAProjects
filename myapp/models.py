
from django.db import models

class About(models.Model):
    text = models.TextField()

    def __str__(self):
        return "About me"
    
class Work(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()


class Review(models.Model):git
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=1000)
    comment = models.TextField()

    def __str__(self):
        return f"Review by {self.name} from {self.company}"
