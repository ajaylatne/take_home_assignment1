from django.urls import path
from .views import CreatePost, ListPost, \
    RetrievePost, UpdatePost, DeletePost
from .views import RegisterUserView # LogoutView, UserLoginView

urlpatterns = [
    # path('login/', UserLoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('POST/api/posts/', CreatePost.as_view(), name="create-post"),
    path('GET/api/posts/', ListPost.as_view(), name="list-post"),
    path('GET/api/posts/<int:pk>/', RetrievePost.as_view(), name="create-post"),
    path('PUT/api/posts/<int:pk>/', UpdatePost.as_view(), name="update-post"),
    path('DELETE/api/posts/<int:pk>/', DeletePost.as_view(), name="delete-post"),
]
