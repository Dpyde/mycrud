from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    description = models.TextField()
    class Meta:
        ordering =['title','author','published_date','description']
        db_table='books'
        
    def __str__(self):
        return self.title