from django import template

register = template.Library()

@register.filter
def index(List, i):
    return List[int(i)]

@register.filter
def entry_num_array(List):
    return range(len(List))

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)