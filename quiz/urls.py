from django.urls import path,include
from . import views

dept_patterns = [
    path('',views.dept,name='departments'),
    path('<int:pk>',views.dept_detail,name='departments-detail'),
    path('<int:pk>/words',views.dept_word,name='departments-words'),
]

word_patterns = [
    path('',views.word,name='words'),
    path('<int:pk>',views.word_detail,name='words-detail'),
]


urlpatterns = [
    path('departments/',include(dept_patterns)),
    path('word/',include(word_patterns)),
]
