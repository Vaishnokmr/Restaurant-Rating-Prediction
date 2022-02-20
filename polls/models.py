from django.db import models


class details(models.Model):
    online_order = models.CharField(max_length=100)
    book_table = models.CharField(max_length=100)
    votes = models.CharField(max_length=100)
    locations =  models.CharField(max_length=100)
    rest_type =  models.CharField(max_length=100)
    cuisines =  models.CharField(max_length=100)
    cost =  models.CharField(max_length=100)

