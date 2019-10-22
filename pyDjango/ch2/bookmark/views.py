from django.views.generic import ListView, DetailView
from bookmark.models import bookmark

# Create your views here.

#--- ListView
class BookmarkLV(ListView):
    model = Bookmark

#--- DetailView
class BookmakrDV(DetailView):
    model = Bookmark
