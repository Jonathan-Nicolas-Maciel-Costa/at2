from django.shortcuts import render, get_object_or_404
from .models import disco

# Create your views here.

def index_view (request):

    discos = disco.objects.all()
    context = {'discos': discos}
    
    return render(request, 'index.html',  context)

def detalhes_view (request, discos_id):

    discos = get_object_or_404(disco, id=discos_id)
    #discos = disco.objects.get(id=discos_id)
    context = {
        'discos': discos
    }
    return render (request, 'detalhes.html', context)

    