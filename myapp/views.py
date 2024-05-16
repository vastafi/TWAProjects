
from .models import About
from .models import Work
from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

# Create your views here.
def home(request):
        my_work_list = Work.objects.all()  
        return render(request, 'home.html', {'work_list': my_work_list})


def about(request):
    about = About.objects.first()  # Extrage primul obiect din tabelul About
    return render(request, "about.html", {'about': about})

def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirecționează utilizatorul către pagina principală după adăugarea recenziei
        
    else:
        form = ReviewForm()
    return render(request, 'review.html', {'form': form})

def Works(request):
    my_work_list = Work.objects.all()  
    return render(request, 'base.html', {'work_list': my_work_list})

