from django.shortcuts import render,get_object_or_404
from .models import *

# Create your views here.
def faqa_pare(request):
    lajmet = Lajmi.objects.all()
    if not lajmet:
        recent =[]
    else:
        recent = Lajmi.objects.all().order_by('-data')[0]
    context = {'lajmet':lajmet,'recent':recent}
    return render(request, 'lajmet/index.html',context)

def lajmet(request):
    lajmet = Lajmi.objects.all()
    return render(request, 'lajmet/lista_lajmeve.html',{'lajmet':lajmet})

def lajmi(request,slug):
    lajmi = get_object_or_404(Lajmi,slug=slug)
    return render(request, 'lajmet/lajmi.html', {'lajmi':lajmi} )


def kontaktet(request):
    return render(request, 'lajmet/kontaktet.html')

def mbi_ne(request):
    return render(request, 'lajmet/mbi_ne.html')