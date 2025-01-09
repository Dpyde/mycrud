from django.db import models


class Author(models.Model):
    name=  models.CharField(max_length=100)
    id= models.IntegerField(primary_key=True)
    class Meta:
        ordering=['name']
        db_table='authors'       
        
         
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,null=False,blank=False,default=None)
    published_date = models.DateField()
    description = models.TextField()
    class Meta:
        ordering =['title','author','published_date','description']
        db_table='books'        