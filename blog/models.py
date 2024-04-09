from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from read_statistics.models import ReadNumExpandMethod,ReadDetail
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation


# Create your models here.
class BlogType(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name


class Blog(models.Model, ReadNumExpandMethod):
    title = models.CharField(max_length=50)
    blog_type = models.ForeignKey(BlogType, on_delete=models.CASCADE)
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # 外键关联主键，当删除时不做任何操作
    # content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # object_id = models.PositiveIntegerField()
    # read_details = GenericForeignKey('content_type', 'object_id')
    # read_details = GenericForeignKey(ReadDetail)

    read_details = GenericRelation('read_statistics.ReadDetail')
    created_time = models.DateTimeField(auto_now_add=True)  # 自动添加创建时间
    last_updated_time = models.DateTimeField(auto_now=True)  # 自动修改最后跟新时间

    def get_url(self):
        return reverse('blog_detail', kwargs={'blog_pk': self.pk})

    def get_email(self):
        return self.author.email

    def __str__(self):
        return "<Blog:%s>" % self.title

    class Meta:
        ordering = ['-created_time']
