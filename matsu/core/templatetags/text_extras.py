
from django import template

from matsu.utils.text import render_markdown

register = template.Library()

register.filter('render_markdown', render_markdown)
