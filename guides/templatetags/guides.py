from django import template
from markdown2 import markdown as mark

register = template.Library()


@register.filter
def markdown(text: str):
    return mark(text, safe_mode=True)
