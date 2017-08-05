
import markdown

from django.utils.html import escape
from django.utils.safestring import mark_safe


def render_markdown(raw_text):
    return mark_safe(markdown.markdown(escape(raw_text)))
