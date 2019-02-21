from django import template
register = template.Library()

@register.filter
def indexer(List, i):
    return List[i]


@register.filter
def diction(dict, key):
    return getattr(dict, key)
