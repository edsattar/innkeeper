from django.db import models
import uuid
from datetime import datetime as dt
from time import time

# Create your models here.

class RoomType(models.Model):
    room_type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(null=True)

    def __str__(self):
        return self.room_type

class Room(models.Model):
    room_number = models.IntegerField()
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    description = models.TextField(null=True)

    def __str__(self):
        return f'{str(self.room_number)} - {self.room_type}'

class Guest(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, null=True)
    country = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Reservation(models.Model):

    def get_ref_number():
        return ''.join(str(e) for e in 
        [['JA','FB','MA','AP','MY','JU','JL','AU','SP','OC','NV','DC'][dt.now().month - 1], 
        dt.now().year%10, 
        dt.now().day, 
        int(time()/40)%1000])

    reference_number = models.CharField(max_length=10, unique=True, default=get_ref_number())
    guest_name = models.CharField(max_length=50)
    guest_phone_number = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):   
        return self.guest.first_name + " " + self.guest.last_name + " " + str(self.room.room_number)

class RoomReservation(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    selling_price = models.DecimalField(max_digits=6, decimal_places=2)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    number_of_adults = models.IntegerField(default=1)
    number_of_children = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.reservation.guest.first_name + " " + self.reservation.guest.last_name + " " + str(self.room.room_number)
class Booking(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.guest.first_name + " " + self.guest.last_name + " " + str(self.room.room_number)
class CheckIn(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    check_in_time = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.reservation.guest.first_name + " " + self.reservation.guest.last_name + " " + str(self.room.room_number)

class CheckOut(models.Model):
    check_in = models.ForeignKey(CheckIn, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.check_in.reservation.guest.first_name + " " + self.check_in.reservation.guest.last_name + " " + str(self.check_in.room.room_number)

class PaymentMethod(models.Model):
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return self.payment_method

class PaymentStatus(models.Model):
    payment_status = models.CharField(max_length=50)

    def __str__(self):
        return self.payment_status

class Payment(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=30, null=True)
    payment_status = models.ForeignKey(PaymentStatus, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.reservation.guest.first_name + " " + self.reservation.guest.last_name + " " + str(self.amount)


class Department(models.Model):
    department_name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.department_name

class EmployeePosition(models.Model):
    position_name = models.CharField(max_length=50)
    department_name = models.ForeignKey(Department, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.position_name

class Employee(models.Model):
    name = models.CharField(max_length=50)
    position = models.ForeignKey(EmployeePosition, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class EmployeeSalary(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.employee.name + " " + str(self.amount)

class ExpenseCategory(models.Model):
    category_name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.category_name

class Expense(models.Model):
    expense_category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.expense_category.category_name + " " + str(self.amount)

class Supplier(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class PurchaseOrder(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.supplier.name + " " + str(self.order_date)

class PurchaseOrderItem(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.purchase_order.supplier.name + " " + self.item_name + " " + str(self.total_price)



