from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def filter_multi(x,y):
    return x*y

@register.simple_tag
def simple_tag_multi(x,y):
    return x*y

@register.simple_tag
def my_input(id,args):
    result="<input type='text' id='%s' class='%s'/>"%(id,args,)
    return mark_safe(result)