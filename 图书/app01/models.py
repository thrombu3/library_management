from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    publish_time = models.DateTimeField(auto_now_add=True)
    xiaoliang = models.IntegerField()
    kucun = models.IntegerField()

    publish = models.ForeignKey(to='Publish')
    authors = models.ManyToManyField(to='Author')

    def __str__(self):
        return '书籍对象:%s'%self.title

class Publish(models.Model):
    name = models.CharField(max_length=255)
    addr = models.CharField(max_length=255)

    def __str__(self):
        return '出版社对象:%s'%self.name


class Author(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()

    author_detail = models.OneToOneField(to='AuthorDetail')

    def __str__(self):
        return '作者对象:%s'%self.name


class AuthorDetail(models.Model):
    phone = models.BigIntegerField()
    addr = models.CharField(max_length=255)

    def __str__(self):
        return '作者详情表:%s'%self.addr