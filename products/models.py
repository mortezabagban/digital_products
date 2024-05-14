from django.db import models
from django.utils.translation import gettext_lazy as _

class Category(models.Model):# انواع دسته بندی محصولات 
    parent=models.ForeignKey('self',verbose_name=_('parent'),blank=True,null=True,on_delete=models.CASCADE)
    title=models.CharField(_('Title'),max_length=50)
    description = models.TextField(_('Description'),blank=True)
    avatar=models.ImageField(_('Avatar'),blank=True,upload_to='Categoryies/')
    is_enable=models.BooleanField(_('is_enable'),default=True)
    created_time=models.DateTimeField(_('created_time'),auto_now_add=True)
    updated_timme=models.DateTimeField(_('updated_timme'),auto_now_add=True)
    class Meta:
        db_table='categoryies'
        verbose_name=_('Category')
        verbose_name_plural=_('Categories')

    def __str__(self):
       return self.title

class Product(models.Model):#محصولات 
    title = models.CharField(_('Title'), max_length=50)
    description = models.TextField(_('Description'), blank=True)
    avatar = models.ImageField(_('Avatar'), blank=True, upload_to='products/')
    is_enable = models.BooleanField(_('is_enable'), default=True)
    categoryies=models.ManyToManyField('Category',verbose_name=_('Category'),blank=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_timme = models.DateTimeField(_('updated timme'), auto_now_add=True)
    class Meta:
        db_table = 'Product'
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
         return self.title
class File(models.Model):#میشه فایل هارو گذاشت داخل محصول ولی اگر سریال لایز باشد خلیلی سخت خواد شد 
    FILE_AUDIO=1
    FILE_VIDEO=2
    FILE_PDF=3
    FILE_TYPES=(
        ( FILE_AUDIO,_('audio')),
        ( FILE_VIDEO,_('video')),
        ( FILE_PDF,_('pdf'))

    )

    product=models.ForeignKey('Product',verbose_name=_('product'),related_name='files',on_delete=models.CASCADE)
    title = models.CharField(_('Title'), max_length=50)
    file_type=models.PositiveSmallIntegerField(_('file_type'),choices=FILE_TYPES)
    file=models.FileField(_('File'),blank=True,upload_to='files/%Y/%m/%d/')
    is_enable = models.BooleanField(_('is_enable'), default=True)
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    updated_timme = models.DateTimeField(_('updated timme'), auto_now_add=True)

    class Meta:
        db_table = 'files'
        verbose_name = _('File')
        verbose_name_plural = _('files')

    def __str__(self):
         return self.title
    




