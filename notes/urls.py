# notes/urls.py
from django.urls import path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'notes', NoteViewSet)

urlpatterns = router.urls

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='user-registration'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
    path('notes/create/', NoteCreateAPIView.as_view(), name='note-create'),
    path('notes/<str:pk>/', NoteRetrieveAPIView.as_view(), name='note-retrieve'),
    path('notes/delete/<str:pk>/', NoteDeleteAPIView.as_view(), name='note-delete'),
    path('notes/update/<str:pk>/', NoteUpdateAPIView.as_view(), name='note-update'),

]