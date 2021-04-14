from django.db import models




# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField() #slug field is for -@12 number+symballs+text
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True) #it will take date from instace created
    # add in thumbnail later
    # add in author later


    #created to show self.title (model.title) in string format
    def __str__(self): 
        return self.title

    def snippet(self):
        return self.body[:50] + '......'

    

