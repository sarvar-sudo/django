from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.views.generic.list import ListView

from .models import movie,ViewUser,live_chanel, channelviews
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect

from .forms import commentt, site_comment
# Create your views here.
def live_channel(request):
    live_ch = live_chanel.objects.all()
    
    context = {
        'live_ch':live_ch,
    }
    return render(request, 'movie/live.html',context)

def index(request):
    kino = movie.objects.all()[:4]
    kino1 = movie.objects.all()[4:]
    live_ch = live_chanel.objects.all()[:4]

    if request.method == 'POST':
            form2 = site_comment(request.POST)
            if form2.is_valid():
                comment = form2.save(commit=False)
                comment.user = request.user
                comment.save()
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        form3 = site_comment()
    context = {
        'kino':kino,
        'kino1':kino1,
        'live_ch':live_ch,

    }
    return render(request, 'movie/index1.html', context)
def about(request):
    return render(request, 'Site1/index.html') 

def channel_detail(request, id):
    live_ch = live_chanel.objects.get(id=id)
    another_channel = live_chanel.objects.all()[4:8]
    views_count = get_object_or_404(live_chanel, id=id)
    views_user = channelviews.objects.filter(user=request.user, livechannel=live_ch)
    if not views_user:
        views_count.see = views_count.see + 1
        views_count.save()
        new_view_user = channelviews.objects.create(user=request.user, livechannel=live_ch)
        new_view_user.save()
    context = {
        'live_ch':live_ch,
        'another_channel':another_channel
       
    }
    return render(request, 'movie/live_chanel.html', context) 

@login_required(login_url='/register/login/')  
def movie_detail(request, id):
    movie1 = movie.objects.get(id=id)
    another_movie = movie.objects.all()[8:12]

    views_count = get_object_or_404(movie, id=id)
    views_user = ViewUser.objects.filter(user=request.user, movie2=movie1)
    if not views_user:
        views_count.see = views_count.see + 1
        views_count.save()
        new_view_user = ViewUser.objects.create(user=request.user, movie2=movie1)
        new_view_user.save()
    context = {
        'movie1':movie1,
        'another_movie':another_movie
       
    }
    return render(request, 'movie/movie-details.html', context)    

class QidirishView(ListView):
    model = movie
    template_name = 'movie/search.html'
    context_object_name = 'javob'
    
    def get_queryset(self):
        data = self.request.GET.get('q')
        return movie.objects.filter(
            Q(name__icontains=data)|Q(about__icontains=data)
        )