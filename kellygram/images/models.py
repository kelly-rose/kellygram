from django.db import models
from kellygram.users import models as user_models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

@python_2_unicode_compatible
class Image(TimeStampedModel):
    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()
    creator = models.ForeignKey(user_models.User, null=True,related_name='images')

    @property
    def like_count(self):
        return self.likes.all().count()     #Image class has likes...(F_Key)

    def __str__(self):  # def __unicode__(self):
        return '{} - {}'.format(self.location,self.caption)

    class Meta:
        ordering = ['-updated_at']

@python_2_unicode_compatible
class Comment(TimeStampedModel):
    message = models.TextField()
    creator = models.ForeignKey(user_models.User, null=True)
    image = models.ForeignKey(Image, null=True,related_name='comments')

    def __str__(self):  # def __unicode__(self):
        return self.message

@python_2_unicode_compatible
class Like(TimeStampedModel):
    creator = models.ForeignKey(user_models.User, null=True)
    image = models.ForeignKey(Image, null=True,related_name='likes')

    def __str__(self):  # def __unicode__(self):
        return 'User: {} - Image Caption: {}'.format(self.creator.username, self.image.caption)
