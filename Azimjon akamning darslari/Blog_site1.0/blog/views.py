from django.shortcuts import render, redirect
from .models import  *
from django.shortcuts import  get_object_or_404
from django.http import JsonResponse

# Create your views here.


def articles(request):
    articles=Article.objects.all().order_by('-created_date')
    return render(
    request=request,
        template_name='index.html',
        context={
            'articles':articles
        }
    )

def article_detail(request, id):
    if request.method=='POST':
        if request.user.username:
            commit=request.POST.get("comment", None)
            person=Person.objects.get(user=request.user)
            article=Article.objects.get(id=id)
            if commit: # agar commit bo'sh bo'lmasa uni yaratadi
                article.setcommit(commit=commit,person=person)

    article=Article.objects.get(id=id)
    # article=get_object_or_404(Article,id=id)
    # likes=article.reactions.filter(reaction='like').count()
    # dislikes = article.reactions.filter(reaction='dislike').count()
    return render(
        request=request,
        template_name='article_detail.html',
        context={
            'article':article  if article else None
        }
    )
def reaction(request,id,react):
    if request.user.username:
        person=Person.objects.get(user=request.user)
        article=Article.objects.get(id=id)
        article.setreaction(react=react ,person=person)
        # return  redirect('article_detail', id)
    return JsonResponse({
        'likes':article.like,
        'dislikes':article.dislike
    })

def persons_view(request):
    persons=Person.objects.all()
    return render(
        request=request,
        template_name='persons.html',
        context={
            'persons':persons
        }
    )
