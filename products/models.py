from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name= _('parent'), null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(_('title'),max_length=50)
    description = models.TextField(_('description') , blank=True)
    avatar = models.ImageField(_('avatar'), upload_to='categories/', blank=True)
    is_enable = models.BooleanField(_('is enable'), default=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        db_table = 'categories'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Product(models.Model):
    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'), upload_to='products/', blank=True)
    is_enable = models.BooleanField(_('is enable'), default=True)
    categories = models.ManyToManyField('Category', verbose_name=_('categories'))
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.title


class File(models.Model):
    product = models.ForeignKey('Product', verbose_name=_('product'), on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=50)
    file = models.FileField(_('file'), upload_to='files/%Y/%m/%d/', blank=True)
    is_enable = models.BooleanField(_('is enable'), default=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_time = models.DateTimeField(_('updated time'), auto_now=True)

    class Meta:
        db_table = 'files'
        verbose_name = _('file')
        verbose_name_plural = _('files')
