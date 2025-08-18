from django import template
from django.urls import reverse

register = template.Library()

@register.simple_tag
def anchor(home, hotel):
    return reverse(home) + '#' + hotel
