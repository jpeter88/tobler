from django.views import generic
#from .models import Album

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'


