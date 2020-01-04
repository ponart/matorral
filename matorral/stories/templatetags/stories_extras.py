from django import template
from django.utils.safestring import mark_safe
from django.utils.text import Truncator

import markdown

register = template.Library()


@register.filter()
def render_markdown(text, truncate_words=None):
    html = markdown.markdown(text)

    if truncate_words:
        truncator = Truncator(html)
        html = truncator._truncate_html(truncate_words, '...', html, truncate_words, truncate_words)

    return mark_safe(html)
