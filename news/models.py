from django.db import models
from django.contrib.auth.models import User
from .notes import *


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating_author = models.IntegerField(default=0)

    def update_rating(self):
        self.rating_author = 0
        for post_ in Post.objects.all():
            if post_.author_id == self.id:
                self.rating_author += post_.rating_post * 3
            for comments_to_post in Comment.objects.filter(post=post_.id):
                if comments_to_post.user_id == self.id:
                    self.rating_author += comments_to_post.rating_comment
        for comment_author in Comment.objects.all():
            if comment_author.user_id == self.id:
                self.rating_author += comment_author.rating_comment
        self.save()


class Category(models.Model):
    name_category = models.CharField(unique=True, max_length=2, choices=category)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    type_of_post = models.CharField(max_length=2, choices=type_post)
    time_in = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    rating_post = models.IntegerField(default=0)
    post_category = models.ManyToManyField(Category, through='PostCategory')

    @property
    def rating(self):
        return self.rating_post

    @rating.setter
    def rating(self, value):
        self.rating_post = value if value >= 0 and isinstance(value, int) \
            else 0
        self.save()

    def like(self):
        self.rating_post += 1
        self.save()

    def dislike(self):
        self.rating_post -= 1
        self.save()

    @property
    def preview(self):
        return self.text[:124] + '...'

    def __str__(self):
        return f'{self.title}, {self.time_in}, {self.text[:20]}, {self.author}'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text_comment = models.TextField()
    time_in = models.DateTimeField(auto_now_add=True)
    rating_comment = models.IntegerField(default=0)

    @property
    def rating(self):
        return self.rating_comment

    @rating.setter
    def rating(self, value):
        self.rating_comment = value if value >= 0 and isinstance(value, int) \
            else 0
        self.save()

    def like(self):
        self.rating_comment += 1
        self.save()

    def dislike(self):
        self.rating_comment -= 1
        self.save()


