from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def highlight(title, keyword):
	marked_keyword = title.replace(keyword, '<mark class="bg-warning">{}</mark>'.format(keyword))
	return mark_safe(marked_keyword)