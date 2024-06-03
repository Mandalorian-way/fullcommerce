from django import template

register = template.Library()

@register.simple_tag
def progress_percentage(value,total):
    percent = (value/total) * 100
    return percent

@register.simple_tag
def discount_money(original,discount):
    return round(original - (original*discount/100))