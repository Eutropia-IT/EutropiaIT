from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404

# model
from dashboard.models import Client, Project, Employee, Blog
# Create your views here.

# service
from .serviceItem import web_dev, app_dev, product_design, seo, digital_marketing, it_consultaant


def index(request):
    context = {
        "company" : Client.objects.all(),
        "project" : Project.objects.all(),
        "employee" : Employee.objects.all()
    }
    return render(request, 'index.html', context)

def about(request):
    context = {
        "banner" : {
            "title" : "About US"
        }
    }
    return render(request, 'about.html', context)

def services(request, service):
    if service == 'web-development':
        return render(request, 'services.html', web_dev)
    elif service == 'app-development':
        return render(request, 'services.html', app_dev)
    elif service == 'product-design':
        return render(request, 'services.html', product_design)
    elif service == 'techenical-seo':
        return render(request, 'services.html', seo)
    elif service == 'digital-marketing':
        return render(request, 'services.html', digital_marketing)
    elif service == 'it-consultaant':
        return render(request, 'services.html', it_consultaant)
    
    raise Http404     
    


def portfolio(request):
    context = {
        "banner" : {
            "title" : "Portfolio"
        },
        "portfolio" : Project.objects.all(),
    }
    return render(request, 'portfolio.html', context)

def project(request, title):
    context = {
        "banner" : {
            "title" : "Portfolio"
        },
        'project' : get_object_or_404(Project, title=title)
    }
    
    return render(request, 'project.html', context)

def blogs(request):
    context = {
        "banner" : {
            "title" : "Blog"
        },
        'blogs' : Blog.objects.all().order_by('-id')
        
    }
    return render(request, 'blogs.html', context)


def blog(request, title):
    try:
        blog = Blog.objects.get(title=title)
        context = {
            "banner" : {
                "title" : blog.title
            },
            'blog' : blog
            
        }
        return render(request, 'blog.html', context)
    except:
        raise Http404     


def contact(request):
    context = {
            "banner" : {
                "title" : "Contact Us"
            },
        }
    return render(request, 'contacts.html', context)