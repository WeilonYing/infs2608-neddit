from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Subneddit(models.Model):
    id = models.CharField(
        verbose_name="Course Code", max_length=8, primary_key=True)
    name = models.CharField(verbose_name="Course Name", max_length=100)
    subscribed = models.ManyToManyField(
        get_user_model(), related_name="Subscriber", blank=True)
    admin = models.ManyToManyField(
        get_user_model(), related_name="Admin")
    sidebar = models.TextField(verbose_name="Sidebar Text", blank=True)

    def __str__(self):
        return self.id + ' (' + self.name + ')'


class Post(models.Model):
    def makepath(instance, filename):
        return '{0}/{1}/%Y-%m-%d-%H-%M-%S/{2}'.format(
            instance.subneddit.id, instance.author.username, filename)

    subneddit = models.ForeignKey(Subneddit, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    submitDate = models.DateTimeField()
    isTextPost = models.BooleanField()
    content = models.TextField()
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE)
    notefile = models.FileField(upload_to=makepath, blank=True, null=True)

    def __str__(self):
        return self.title + '-' + self.subneddit.id + '-' + self.author.username


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parentComment = models.ForeignKey(
        'Comment', on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField()
    submitDate = models.DateTimeField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return ('Comment on ' + self.post.title + ' by ' + self.author.username
            + ' (' + str(self.submitDate) + ')')


class PostVotes(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    voteVal = models.IntegerField()

    def __str__(self):
        return self.post.title + '-' + self.user.username + '-' + str(self.voteVal)


class CommentVotes(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    voteVal = models.IntegerField()

    def __str__(self):
        return str(self.comment) + '-' + str(self.voteVal)
