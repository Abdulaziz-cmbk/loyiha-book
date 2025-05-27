from django.shortcuts import render,redirect
from .models import *
from .forms import *

def home(request):
    return render(request, 'index.html')  


#author
def author_view(request):
    authors = Author.objects.filter(is_deleted=False)
    
    search = request.GET.get('search', None)
    if search:
        authors = authors.filter(full_name__icontains=search)

    context = {
        'authors':authors
    }
    return render(request, 'author/author.html', context=context)

def author_create(request):
    if request.method == "POST":
        forms = AuthorForms(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('author_view')
    else:
        forms = AuthorForms()
    context = {
        "forms": forms
    }
    return render(request, 'author/author_create.html', context=context)


def author_update(request, pk):
    author = Author.objects.get(pk=pk)
    if request.method == "POST":
        forms = AuthorForms(request.POST, instance=author)
        if forms.is_valid():
            forms.save()
            return redirect('author_view')
    else:
        forms = AuthorForms(instance=author)
    
    context = {
        'forms': forms
    }
    return render(request, 'author/author_update.html', context=context)

def author_delete(request, pk):
    author = Author.objects.get(pk=pk)
    author.is_deleted = True
    author.save()
    return redirect('author_view')


#references

def reference_view(request):
    book_category = References.objects.filter(type="kitob_turi", is_deleted=False)
    gender = References.objects.filter(type='jinsi',is_deleted=False)

    context = {
        "book_category": book_category,
        "genders": gender
    }
    return render(request, 'reference/reference.html', context=context)


def reference_create(request):
    if request.method == "POST":
        forms = ReferenceForms(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('reference_view')
    else:
        forms = ReferenceForms()
    context = {
        "forms": forms
    }
    return render(request, 'reference/reference_create.html', context=context)

def reference_update(request, pk):
    references = References.objects.get(pk=pk)
    if request.method == "POST":
        forms = ReferenceForms(request.POST, instance=references)
        if forms.is_valid():
            forms.save()
            return redirect('reference_view')
    else:
        forms = ReferenceForms(instance=references)
    
    context = {
        'forms': forms
    }
    return render(request, 'reference/reference_update.html', context=context)

def reference_delete(request, pk):
    reference = References.objects.get(pk=pk)
    reference.is_deleted = True
    reference.save()
    return redirect('reference_view')
