from .views import ChapterCreate,CharacterUpdate,CharacterDelete,CharacterList, CharacterDetail, CustomLoginView, RegisterPage, CharacterCreate, home, ChapterDelete, ChapterDetail, ChapterList, ChapterUpdate, DetailCreate, DetailDelete, DetailDetail, DetailsList, DetailUpdate, DetailView
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name="home"), 
    path('character-update/<int:pk>/', CharacterUpdate.as_view(), name='character-update'),
    path('character-delete/<int:pk>/', CharacterDelete.as_view(), name='character-delete'),
    path('character/<int:pk>', CharacterDetail.as_view(), name="character"), 
    path('characters/', CharacterList.as_view(), name="characters"),
    path('create-character/', CharacterCreate.as_view(), name="new-character"), 
    
    path('chapter-update/<int:pk>/', ChapterUpdate.as_view(), name='chapter-update'),
    path('chapter-delete/<int:pk>/', ChapterDelete.as_view(), name='chapter-delete'),
    path('chapter/<int:pk>', ChapterDetail.as_view(), name="chapter"), 
    path('chapters/', ChapterList.as_view(), name="chapters"),
    path('create-chapter/', ChapterCreate.as_view(), name="new-chapter"), 

    path('detail-update/<int:pk>/', DetailUpdate.as_view(), name='detail-update'),
    path('detail-delete/<int:pk>/', DetailDelete.as_view(), name='detail-delete'),
    path('detail/<int:pk>', DetailDetail.as_view(), name="detail"), 
    path('details/', DetailsList.as_view(), name="details"),
    path('create-detail/', DetailCreate.as_view(), name="new-detail"), 
    
    path('login/', CustomLoginView.as_view(), name="login"), 
    path('register/', RegisterPage.as_view(), name="register")
]