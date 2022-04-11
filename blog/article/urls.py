from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views

app_name = "article"

urlpatterns=[

    path('dashboards/',views.dashboard,name="dashboard"),
    path('addarticle/',views.addarticle,name="addarticle"),
    path('article/<int:id>',views.details,name="details"),
    path('update/<int:id>',views.updateArticle,name="update"),
    path('delete/<int:id>',views.deleteArticle,name="delete"),
    path('',views.articles,name="articles"),
    path('comment/<int:id>',views.addComment,name="comment"),
]