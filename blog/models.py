from django.db import models
from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class Tag(models.Model):
    value = models.TextField(max_length=100)

    def __str__(self):
        return self.value

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    title = models.TextField(max_length=100)
    slug = models.SlugField()
    summary = models.TextField(max_length=500)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="posts")
    comments = GenericRelation('Comment')

    def __str__(self):
        return self.title

class Comment(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    created_at = models.DateTimeField(auto_now_add=True, default=timezone.now)
    modified_at = models.DateTimeField(auto_now=True, default=timezone.now)


# In [1]: from django.contrib.contenttypes.models import ContentType

# In [2]: from blog.models import Post, Comment
  
# In [3]: post_type = ContentType.objects.get_for_model(Post)
  
# In [4]: p = Post.objects.first()
  
# In [5]: c = Comment.objects.filter(content_type=post_type, object_id=p.pk)
  
# In [6]: c
# Out[6]: <QuerySet [<Comment: Comment object (1)>, <Comment: Comment object (2)>]>

# p = Post.objects.first()
# p.comments.all()
# c1 = p.comments.all()[0]
# p.comments.remove(c1)