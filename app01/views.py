from django.shortcuts import render,HttpResponse
from .models import *

# Create your views here.
def my_day(request,year):
    return HttpResponse(year)

def my_day2(request,year,month='3'):
    return HttpResponse('%s-%s'%(year,month))

def my_day3(request,year,month,day):
    return HttpResponse('%s-%s-%s' % (year, month, day))

def my_day4(request,year):
    return render(request,'my_day.html')

def my_hello(request):
    return HttpResponse('hello')

def index(request):
    import datetime
    s='hello'
    l=[1,2,3]
    dic={"name":'lary',"age":18}
    date = datetime.date(2000,3,12)

    class Person(object):
        def __init__(self,name):
            self.name = name

    person_l=Person("lily")
    person_j=Person('jerry')
    person_t=Person('tom')

    person_li=[person_l, person_j, person_t]

    return render(request,'index.html',{"l":l,"dic":dic,"date":date,"person_list":person_li,"s":s})

def query(request):
    #all() 查询所有结果
    book_list=Book.objects.all()
    print(book_list)                #<QuerySet [<Book: book1>, <Book: book2>, <Book: book3>]>

    #filter()它包含了与所给筛选条件相匹配的对象
    book_list = Book.objects.filter(id=1)
    print(book_list)                #<QuerySet [<Book: book1>]>

    #get() model对象 有且只有一个查询结果时才有意义 如果超过一个或者没有都会抛出异常
    book = Book.objects.get(id=2)
    print(book)                     #<Book: book2>

    #order_by()  model对象 对查询结果排序
    book = Book.objects.all().order_by("-id")
    print(book)    #<QuerySet [<Book: book3>, <Book: book2>, <Book: book1>]>

    #count()  返回匹配查询对象的数量
    book = Book.objects.all().order_by("-id").count()
    print(book)    #3

    #exists() 如果Queryset包含数据，则返回true，否则返回false
    book  = Book.objects.all().exists()
    if book:
        print("OK")

    #values()  返回一个valueQureyset 是一个可迭代的字典序列
    book = Book.objects.all().values()
