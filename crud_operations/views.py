from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, \
    UpdateAPIView
from .models import Post
from .serializers import PostSerializer, UserRegistrationSerializer  # , UserLoginSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
# from django.contrib.auth import logout, authenticate, login
# from rest_framework import status
# from rest_framework.views import APIView
# from rest_framework.response import Response


#  User view
class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    authentication_classes = []
    permission_classes = (AllowAny,)


# class UserLoginView(APIView):
#     authentication_classes = []
#     permission_classes = (AllowAny,)
#
#     def post(self, request):
#         serializer = UserLoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         username = serializer.data.get('username')
#         password = serializer.data.get('password')
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return Response({'msg': 'Login Success'}, status=status.HTTP_200_OK)
#         else:
#             return Response({'errors': {'non_field_errors': ['Username or Password is not Valid']}},
#                             status=status.HTTP_404_NOT_FOUND)
#
#
# class LogoutView(APIView):
#     def post(self, request):
#         logout(request)
#         return Response({"detail": "Logged out successfully."}, status=status.HTTP_200_OK)


# Post Views

class CreatePost(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class ListPost(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        # Filter posts by title
        title = self.request.query_params.get('title', None)
        if title:
            queryset = queryset.filter(title__icontains=title)

        # Filter posts by body
        body = self.request.query_params.get('body', None)
        if body:
            queryset = queryset.filter(body__icontains=body)

        # Filter posts by author (assuming the author's username is used)
        author = self.request.query_params.get('author', None)
        if author:
            queryset = queryset.filter(author__username__icontains=author)

        return queryset


class RetrievePost(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UpdatePost(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class DeletePost(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
