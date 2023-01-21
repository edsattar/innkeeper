from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.RoomType)
admin.site.register(models.Room)
admin.site.register(models.Guest)
admin.site.register(models.Reservation)
admin.site.register(models.RoomReservation)
admin.site.register(models.Booking)
admin.site.register(models.CheckIn)
admin.site.register(models.CheckOut)


admin.site.register(models.PaymentMethod)
admin.site.register(models.PaymentStatus)
admin.site.register(models.Payment)

admin.site.register(models.Department)


admin.site.register(models.Employee)
admin.site.register(models.EmployeePosition)
admin.site.register(models.EmployeeSalary)
# admin.site.register(models.EmployeeAttendance)
# admin.site.register(models.EmployeeLeave)
# admin.site.register(models.EmployeeLeaveType)
# admin.site.register(models.EmployeeLeaveRequestStatus)

admin.site.register(models.Expense)
admin.site.register(models.ExpenseCategory)
# admin.site.register(models.ExpenseStatus)

admin.site.register(models.Supplier)
# admin.site.register(models.SupplierType)

admin.site.register(models.PurchaseOrder)
admin.site.register(models.PurchaseOrderItem)


