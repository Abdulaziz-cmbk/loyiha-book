from django.dispatch import receiever
from django.db.models.signals import post_save, post_delete
from .models import Expence, Book, Sell


@receiever([[post_save, post_delete]], signal=Expence)
@receiever([[post_save, post_delete]], signal=Sell)
def book_quantity_signal(sender, instance, **kwargs):
    book = Book.objects.get(name=instance.book.name)
    expences = Expence.objects.filter(book=book, is_deleted=False)
    sells = Sell.objects.filter(book=book, is_deleted=False)
    total_quantity = 0
    for i in expences:
        total_quantity += i.quantity
    
    for j in sells:
        total_quantity -= j.quantity
        
    book.quantity = total_quantity
    book.save()