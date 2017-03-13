from account.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, HttpResponseRedirect

from .forms import NewsCreateForm
from .models import News


@login_required
def create(request, news_id=None):
    creation_form = NewsCreateForm()
    if request.method == 'POST':
        creation_form = NewsCreateForm(request.POST or None, request.FILES)
        if creation_form.is_valid():
            news = creation_form.save(commit=False)
            news.publisher = request.user
            news.save()
            return HttpResponseRedirect(reverse('cartoview_news.list'))
    return render(request, template_name='cartoview_news/create.html', context={'form': creation_form})


def list_news(request):
    return render(request, template_name='cartoview_news/list.html',
                  context={'news': News.objects.all().order_by('-date_created')})


def details(request, news_id):
    obj = News.objects.filter(id=news_id).first()
    return render(request, template_name='cartoview_news/details.html', context={'obj': obj})


@login_required
def edit(request, news_id=None):
    obj = News.objects.filter(id=news_id).first()
    creation_form = NewsCreateForm(instance=obj)
    if request.method == 'POST':
        creation_form = NewsCreateForm(request.POST or None, request.FILES, instance=obj)
        if creation_form.is_valid():
            news = creation_form.save()
            return HttpResponseRedirect(reverse('cartoview_news.list'))
    return render(request, template_name='cartoview_news/update.html', context={'form': creation_form})


@login_required
def delete(request, news_id):
    from django.conf import settings
    print 'cartoview_news' in settings.INSTALLED_APPS
    if request.method == 'POST':
        News.objects.filter(id=news_id).delete()
        return HttpResponseRedirect(reverse('cartoview_news.list'))
    return render(request, template_name='cartoview_news/delete.html',
                  context={'object': News.objects.filter(id=news_id).first()})
