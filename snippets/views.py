from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics
from django.http import HttpResponse


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return self.retrieve(request, *args, **kwargs)
        else:
            return HttpResponse("You are not authenticated, please log in and try again!")