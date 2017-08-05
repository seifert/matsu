
from django.shortcuts import render, get_object_or_404

from matsu.core.models import Category


def category(request, path):
    category = get_object_or_404(Category, tree_path=path)
    context = {
        'category': category,
    }
    templates = [
        'core/{}/category.html'.format(category.tree_path),
        'core/category.html',
    ]
    return render(request, templates, context)
