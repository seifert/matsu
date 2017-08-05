
from django import template

from matsu.core.models import Category

register = template.Library()


@register.inclusion_tag('core/category-item.html')
def category_item(tree_path, current_category=None):
    category = Category.objects.get(tree_path=tree_path)
    return {'category': category, 'current_category': current_category}
