from django.shortcuts import render,redirect
from .models import *
from .forms import *

def home(request):
    books = Book.objects.filter(is_deleted=False)
    context = {
        'books':books
    }
    return render(request, 'index.html',context=context)  


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

#book
def book_create(request):

    if request.method == "POST":
        forms = BookForms(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect(home)
    else:
        forms = BookForms()
    context = {
        "forms": forms
    }
    return render(request, 'book/book_create.html', context=context)

#expence

def expence_view(request):
    expences = Expence.objects.filter(is_deleted=False)
    context = {
        'expences':expences
    }
    return render(request, 'expence/expence.html',context=context) 

def expence_update(request, pk):
    expences = Expence.objects.get(pk=pk)
    if request.method == "POST":
        forms = ExpenceForms(request.POST, instance=expences)
        if forms.is_valid():
            forms.save()
            return redirect('expence_view')
    else:
        forms = ExpenceForms(instance=expences)
    
    context = {
        'forms': forms
    }
    return render(request, 'expence/expence_update.html', context=context)


def expence_delete(request, pk):
    expence = Expence.objects.get(pk=pk)
    expence.is_deleted = True
    expence.save()
    return redirect('expence_view')


def expence_create(request):

    if request.method == "POST":
        forms = ExpenceForms(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('expence_view')
    else:
        forms = ExpenceForms()
    context = {
        "forms": forms
    }
    return render(request, 'expence/expence_create.html', context=context)

#sell
def sell_view(request):
    sells = Sell.objects.filter(is_deleted=False)
    context = {
        'sells':sells
    }
    return render(request, 'sell/sell.html',context=context) 


def sell_update(request, pk):
    sells = Sell.objects.get(pk=pk)
    if request.method == "POST":
        forms = SellForms(request.POST, instance=sells)
        if forms.is_valid():
            forms.save()
            return redirect('sell_view')
    else:
        forms = SellForms(instance=sells)
    
    context = {
        'forms': forms
    }
    return render(request, 'sell/sell_update.html', context=context)

def sell_delete(request, pk):
    sells = Sell.objects.get(pk=pk)
    sells.is_deleted = True
    sells.save()
    return redirect('sell_view')


def sell_create(request):

    if request.method == "POST":
        forms = SellForms(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('sell_view')
    else:
        forms = SellForms()
    context = {
        "forms": forms
    }
    return render(request, 'sell/sell_create.html', context=context)

#staff


def staff_view(request):
    staffs = Staff.objects.filter(is_deleted=False)
    staff_payments = Staff_payment.objects.filter(is_deleted=False)
    staff_works = Staff_work .objects.filter(is_deleted=False)
    context = {
        'staffs':staffs,
        'staff_payments':staff_payments,
        'staff_works':staff_works
        
    }
    return render(request, 'staff/staff.html',context=context) 

def staff_update(request, pk):
    staffs = Staff.objects.get(pk=pk)
    if request.method == "POST":
        forms = StaffForm(request.POST, instance=staffs)
        if forms.is_valid():
            forms.save()
            return redirect('staff_view')
    else:
        forms = StaffForm(instance=staffs)
    
    context = {
        'forms': forms
    }
    return render(request, 'staff/staff_update.html', context=context)

def staff_delete(request, pk):
    staffs = Staff.objects.get(pk=pk)
    staffs.is_deleted = True
    staffs.save()
    return redirect('staff_view')

def staff_create(request):

    if request.method == "POST":
        forms = StaffForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('staff_view')
    else:
        forms = StaffForm()
    context = {
        "forms": forms
    }
    return render(request, 'staff/staff_create.html', context=context)


#income_calc

def income_calc_view(request):
    
    expences = Expence.objects.filter(is_deleted=False)
    sells = Sell.objects.filter(is_deleted=False)
    outputs = Output.objects.filter(is_deleted=False)
    staff_payments = Staff_payment.objects.filter(is_deleted=False)

# Calculate sums
    sell_sum = sum(sell.total_price for sell in sells)
    expence_sum = sum(expence.total_price for expence in expences)
    output_sum = sum(output.price for output in outputs)
    staff_payment_sum = sum(payment.price for payment in staff_payments)

    context = {
    'expence_sum': expence_sum,
    'sell_sum': sell_sum,
    'output_sum': output_sum,
    'staff_payment_sum': staff_payment_sum,
    'profit': sell_sum - (expence_sum + output_sum + staff_payment_sum),
}

    return render(request, 'income_calc.html', context=context)

def staff_payment_update(request, pk):
    staffs = Staff_payment.objects.get(pk=pk)
    if request.method == "POST":
        forms = Staff_paymentForm(request.POST, instance=staffs)
        if forms.is_valid():
            forms.save()
            return redirect('staff_view')
    else:
        forms = Staff_paymentForm(instance=staffs)
    
    context = {
        'forms': forms
    }
    return render(request, 'staff/staff_payment_upgrade.html', context=context)

def staff_payment_delete(request, pk):
    staffs = Staff_payment.objects.get(pk=pk)
    staffs.is_deleted = True
    staffs.save()
    return redirect('staff_view')
