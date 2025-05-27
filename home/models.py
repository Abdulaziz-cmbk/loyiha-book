from django.db import models

# Create your models here.

class References(models.Model):
    TYPE_CHOICES = [
        ('kitob_turi', 'kitob_turi'),
        ('jinsi', 'jinsi'),
        ('chiqim_turi', 'chiqim_turi'),
    ]

    type = models.CharField(max_length=255,choices=TYPE_CHOICES, verbose_name="Malumotnoma turi")
    value = models.CharField(max_length=255,verbose_name="Ma'lumotnoma qiymati")
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'References'

    def __str__(self):
        return self.value


class Author(models.Model):
    full_name = models.CharField(max_length=255)
    birth_date = models.DateField()
    country = models.CharField(max_length=255)
    is_deleted = models.BooleanField(default=False)


    class Meta:
        db_table = 'Author'

    def __str__(self):
        return self.full_name   
    



class Book(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media')
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE)
    category = models.ForeignKey(to=References, on_delete=models.CASCADE, related_name="book_category_references")
    description = models.TextField()
    created_at = models.DateField()
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "Book"

    def __str__(self):
        return self.name


class Expence(models.Model):
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE, related_name="expence_book_book")
    price = models.FloatField()
    quantity = models.IntegerField()
    total_price = models.FloatField()
    description = models.TextField()
    created_at = models.DateField()
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = "Expence"

    def __str__(self):
        return self.price


class Sell(models.Model):
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE, related_name="sell_book_book")
    price = models.FloatField(verbose_name="narxini kiriting")
    quantity = models.IntegerField(verbose_name="nechtaligini kiriting")
    total_price = models.FloatField()
    description = models.TextField()
    created_at = models.DateField()
    is_deleted = models.BooleanField(default=False)


    class Meta:
        db_table = "Sell"

    def __str__(self):
        return self.quantity


class Staff(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.CharField(max_length=2255)
    birthdate = models.DateField()
    gender  = models.ForeignKey(to=References, on_delete=models.CASCADE, related_name="Staff_gender_references")
    created_at = models.DateField()
    balance = models.FloatField(verbose_name="balansni kiriting")
    is_deleted = models.BooleanField(default=False)


    class Meta:
        db_table = "Staff"

    def __str__(self):
        return self.full_name


class Staff_work(models.Model):
    staff = models.ForeignKey(to=Staff, on_delete=models.CASCADE,  related_name="staffwork_staff_staff")
    price = models.FloatField(verbose_name="narxi")
    decription = models.TextField(verbose_name="tavsif")
    created_at = models.DateField()
    is_deleted = models.BooleanField(default=False)


    class Meta:
        db_table = "Staff_work"

    def __str__(self):
        return self.price


class Staff_payment(models.Model):
     staff = models.ForeignKey(to=Staff, on_delete=models.CASCADE, related_name="staffpayment_staff_staff")
     price = models.FloatField(verbose_name="narxi")
     created_at = models.DateField()
     is_deleted = models.BooleanField(default=False)


class output(models.Model):
    type = models.ForeignKey(to=References, on_delete=models.CASCADE, related_name="output_type_References")
    price = models.FloatField(verbose_name="narxi")
    decription = models.TextField(verbose_name="tavsif")
    created_at = models.DateField()
    is_deleted = models.BooleanField(default=False)