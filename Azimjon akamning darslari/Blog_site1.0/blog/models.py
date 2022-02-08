from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Person(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    phone=models.CharField(max_length=30, null=True, blank=True)
    photo=models.ImageField(null=True, blank=True)

    def __str__(self):
        if self.user.first_name and self.user.last_name:
            return f'{self.user.first_name}  {self.user.last_name}'
        elif self.user.first_name:
            return self.user.first_name
        elif self.user.last_name:
            return self.user.last_name
        else:
            return self.user.username




class Author(models.Model):
    full_name=models.CharField(max_length=255)
    spesialist=models.CharField(max_length=255)
    bio=models.TextField()
    reting=models.IntegerField(default=0)

    def __str__(self):
        return  self.full_name



class Article(models.Model):
    author=models.ForeignKey(Author, related_name='articles',on_delete=models.SET_NULL, null=True, blank=True)
    name=models.CharField(max_length=255)
    content=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)
    view_count=models.IntegerField(default=0)

    @property
    def like(self):
        return self.reactions.filter(react='like').count()
    @property
    def dislike(self):
        return  self.reactions.filter(react='dislike').count()

    def setreaction(self, react, person):
        current_react=self.reactions.filter(person=person)
        current_reaction=current_react[0] if current_react else None
        if not current_reaction:
            reaction=Reaction.objects.create(
                article=self,
                person=person,
                react=react
            )
        elif current_reaction.react==react:
            current_reaction.delete()
        else:
            current_reaction.react=react
            current_reaction.save()

    def setcommit(self,person,commit):
        new_commit=Commit.objects.create(
            article=self,
            person=person,
            commit=commit
        )


    def __str__(self):
        return self.name


class Reaction(models.Model):
    article=models.ForeignKey(Article,related_name='reactions', on_delete=models.CASCADE)
    person=models.ForeignKey(Person, related_name='reacts',on_delete=models.SET_NULL, null=True,blank=True)
    react=models.CharField(max_length=10, null=True, blank=True)
    def __str__(self):
        return f"{self.person}'s react for {self.article}"

class Commit(models.Model):
    article=models.ForeignKey(Article,related_name='comments', on_delete=models.CASCADE)
    person=models.ForeignKey(Person, related_name='comments',on_delete=models.SET_NULL, null=True,blank=True)
    commit=models.TextField()

    def __str__(self):
        return f"{self.person}'s comment for {self.article}: {self.commit}"

