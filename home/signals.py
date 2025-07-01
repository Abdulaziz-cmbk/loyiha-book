from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from .models import *


@receiver([post_save, post_delete], sender=Expence)
@receiver([post_save, post_delete], sender=Sell)
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
    
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Staff, Staff_payment, Staff_work

@receiver([post_save, post_delete], sender=Staff_work)
@receiver([post_save, post_delete], sender=Staff_payment)
def staff_balance_signal(sender, instance, **kwargs):

    staff = Staff.objects.get(id=instance.staff.id)
    staff_payments = Staff_payment.objects.filter(staff=staff, is_deleted=False)
    staff_works = Staff_work.objects.filter(staff=staff, is_deleted=False)

    staff_payments_total = sum(payment.price for payment in staff_payments)
    staff_works_total = sum(work.price for work in staff_works)

    staff_balance = staff_works_total - staff_payments_total
    staff.balance = staff_balance
    staff.save()
