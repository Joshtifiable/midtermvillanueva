from django.db import models

# Create your models here.

class Post(models.Model):
    title_text = models.CharField(max_length=100)
    date_created = models.DateTimeField('date created')
    date_updated = models.DateTimeField('date updated')
    content_text = models.CharField(max_length=100)
    #is_active = forms.BooleanField(initial=True)

    def __str__(self):
        return 'Title: {}'.format(self.title_text)
        return 'Content: {}'.format(self.content_text)


class Comment(models.Model):
    post = models.ForeignKey(Post,
                on_delete=models.CASCADE, related_name='choices',
                blank=True, null=True)
    date_created = models.DateTimeField(max_length=100)
    content = models.CharField(max_length=100)

    def __str__(self):
        return 'Choice: {}'.format(self.choice_text)
