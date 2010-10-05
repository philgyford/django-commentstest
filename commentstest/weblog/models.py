from django.db import models

# Create your models here.

class Entry(models.Model):
    title = models.CharField(blank=False, max_length=200)
    body = models.TextField(blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    enable_comments = models.BooleanField(default=True)
    
    def __unicode__(self):
        return self.title




from django.contrib.comments.moderation import CommentModerator, moderator, AlreadyModerated

class EntryModerator(CommentModerator):
    enable_field = 'enable_comments'

try:
    moderator.register(Entry, EntryModerator)
except AlreadyModerated:
    # Safeguard against the models module being imported multiple
    # times (thus registering multiple times and throwing this error)
    pass