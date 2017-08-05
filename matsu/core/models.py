
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class Category(models.Model):

    title = models.CharField(_("Title"), max_length=50)
    tree_path = models.SlugField(_("Tree path"), max_length=255)
    content = models.TextField(_("Content"), blank=True)

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', args=[self.tree_path])
