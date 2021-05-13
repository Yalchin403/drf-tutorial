from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics
from django.http import HttpResponse
from django.contrib.auth.models import User
from snippets.serializers import UserSerializer
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly


permission_cls = [IsOwnerOrReadOnly]
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = permission_cls

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = permission_cls

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return self.retrieve(request, *args, **kwargs)
        else:
            return HttpResponse("You are not authenticated, please log in and try again!")


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer