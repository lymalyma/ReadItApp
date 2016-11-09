from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=70, help_text="Use pen name, not real name")
    review = models.TextField(blank=True, null=True)
    date_reviewed = models.DateTimeField(blank=True, null=True)
    is_favourite = models.BooleanField(default=False, verbose_name="Favorite?") #we can have default
                                                      #values in our model fiel
    def __str__(self):
        return self.title



# new things: help_text to help the user in the admin see what the field is about
# verbose_name makes the is_favourite field appear differently in the admin interface
