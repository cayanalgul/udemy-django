from django.shortcuts import get_object_or_404, render,redirect,reverse
from django.contrib.auth.decorators import login_required
from article.models import Article,Comment
from .forms import Aritcleform
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")
    
@login_required(login_url="user:login")
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {

        "articles":articles
    }
    return render(request,"dashboard.html",context)

@login_required(login_url="user:login")
def addarticle(request):
    form = Aritcleform(request.POST or None, request.FILES or None)
    context = {
        "form":form
    }
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        messages.success(request,"Başarıyla Makaleniz Yüklend")
        return redirect("index")

   
    return render(request,"addarticle.html",context)

def details(request,id):
   
    article = get_object_or_404(Article,id=id)
    comments = article.comment.all()
    
    context={
        "article":article,
        "comments":comments
    }
    return render(request,"details.html",context)

@login_required(login_url="user:login")
def updateArticle(request,id):
    
    article = Article.objects.filter(id=id).first()
    form = Aritcleform(request.POST or None,request.FILES or None,instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()

        messages.success(request,"Başarıyla Makaleniz Güncellendi")
        return redirect("index")
    return render(request,"update.html",{"form":form})

@login_required(login_url="user:login")
def deleteArticle(request,id):
    article = get_object_or_404(Article,id=id)

    article.delete()
    messages.success(request,"Makale Silindi")

    return redirect("article:dashboard")



def articles(request):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = Article.objects.filter(title__contains=keyword)
        return render(request,"articles.html",{"articles":articles})

    articles = Article.objects.all()

    return render(request,"articles.html",{"articles":articles})



def addComment(request,id):
    
    article = get_object_or_404(Article,id=id)

    if request.method == "POST":
        comment_author = request.POST.get("comment-author")
        comment_content = request.POST.get("comment-content")

        newComment = Comment(comment_author = comment_author , comment_content = comment_content)
        newComment.article = article
        newComment.save()

    return redirect(reverse("article:details",kwargs = {"id":id}))
