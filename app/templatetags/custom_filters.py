from django import template 
from app.models import *

register=template.Library()


def data_order_by(queryset,field):
    return queryset.order_by(field)

register.filter("order_by",data_order_by)



def filter_image_by_image_type(queryset,query):
    return queryset.filter(img_type=query)


register.filter("filter_image_by_image_type",filter_image_by_image_type)


def get_element(element):
    element_path={
        "p":"components/p.html",
        "h1":"components/h1.html"
    }
    return element_path[element]


register.filter("get_element",get_element)


def enquiry_Form(value):
    element_path="components/form.html"
    return element_path
