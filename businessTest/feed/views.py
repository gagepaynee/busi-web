from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from feed.models import Article

# Create your views here.

"""def article_list(request):
    articles = Article.objects.all().order_by('-created_date')
    ranks ={}
    mainlinks = {}
    counter = 0  
    for article in articles:
        links = {}
        rankings = {}
        if article.network1_name != '':
            network = article.network1_name
            link = article.network1_link
            links[network] = link
            ranking1 = article.network1_likes - article.network1_dislikes
            rankings[network] = ranking1
        if article.network2_name != '':
            network = article.network2_name
            link = article.network2_link
            links[network] = link
            ranking2 = article.network2_likes - article.network2_dislikes
            rankings[network] = ranking2
        if article.network3_name != '':
            network = article.network3_name
            link = article.network3_link
            links[network] = link
            ranking3 = article.network3_likes - article.network3_dislikes
            rankings[network] = ranking3
        
        newrank = sorted(rankings, key=rankings.__getitem__, reverse=True)
        mainlinks[article.title] = links
        ranks[article.title] = newrank
        counter += 1
    
    
    return render(request, 'feed/index.html', 
    {'articles': articles, 'ranks': ranks, 'mainlinks': mainlinks})"""

def article_list(request):
    articles = Article.objects.all()
    for a in articles:
        rank = a.likes - a.dislikes
        a.rank = rank
        a.save()
    articles = Article.objects.all().order_by('-rank')
    for a in articles:
        network = a.networks.all()
        for n in network:
            rank = n.likes - n.dislikes
            n.rank = rank
            n.save()
        network = a.networks.all().order_by('-rank')
        a.networks= network
        a.save()
    articles = Article.objects.all().order_by('-rank')
    
    return render(request, 'feed/index.html', 
    {'articles': articles})


def vote(request):
    if request.method == "POST":
        print "post"