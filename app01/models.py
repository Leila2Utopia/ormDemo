from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    create_time = models.DateTimeField()
    memo = models.CharField(max_length=32, default="")

    #与publish建立一对多的关系，外键字段建立在多的一方
    publish = models.ForeignKey(to="Publish", default=1)

    #与author表建立多对多的关系，ManyToManyField可以建立在两个模型中的任意一个，自动创建第三张表
    author = models.ManyToManyField("Author")

    def __str__(self):return self.title


class Publish(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)

class Author(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):return self.name
