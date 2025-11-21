from django.shortcuts import render
from rest_framework import viewsets

class ServerListViewSet(viewsets.ModelViewSet):
    def list(self, request, *args, **kwargs):
        return render(request, 'server/server_list.html')