from django.shortcuts import render, redirect
from .models import  *
from django.shortcuts import  get_object_or_404


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
    person=Person.objects.get(user=request.user)
    article=Article.objects.get(id=id)
    article.setreaction(react=react ,person=person)
    return  redirect('article_detail', id)
