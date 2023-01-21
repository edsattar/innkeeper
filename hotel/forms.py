from django import forms
from django.db import models
from .models import RoomType, Guest, Reservation, RoomReservation, CheckIn

# class BookingForm(forms.ModelForm):
#     class Meta:
#         model = Booking
#         fields = ['guest_name', 'room', 'check_in_date', 'check_out_date', 'number_of_guests','notes']
#         widgets = {
#             'check_in_date': forms.DateInput(attrs={'type': 'date'}),
#             'check_out_date': forms.DateInput(attrs={'type': 'date'}),
#         }

#     def __init__(self, *args, **kwargs):
#         super(BookingForm, self).__init__(*args, **kwargs)
#         self.fields['room'].queryset = Room.objects.filter(status='available')

class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        fields = ['first_name', 'last_name', 'email', 'phone_number', 
                  'address', 'city', 'state', 'zip_code', 'country']


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['reference_number', 'guest_name', 'guest_phone_number']

class RoomReservationForm(forms.ModelForm):
    class Meta:
        model = RoomReservation
        fields = ['reservation','room_type', 'check_in_date', 'check_out_date', 
                  'number_of_adults','number_of_children', 'selling_price']
        widgets = {
            'check_in_date': forms.DateInput(attrs={'type': 'date'}),
            'check_out_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        room_type = cleaned_data.get("room_type")
        check_in_date = cleaned_data.get("check_in_date")
        check_out_date = cleaned_data.get("check_out_date")
        available_rooms = Room.objects.filter(room_type=room_type, available=True).count()

        if check_in_date and check_out_date:
            if check_out_date <= check_in_date:
                raise forms.ValidationError("Check-out date should be after check-in date.")
            # check if there are any reservations or bookings that overlap with the selected dates
            overlapped_reservations = RoomReservation.objects.filter(room_type=room_type, 
                                                                check_in_date__lte=check_out_date, 
                                                                check_out_date__gte=check_in_date)
            
            if available_rooms <= overlapped_reservations:
                raise forms.ValidationError("There is no available room for the selected dates.")


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    zip_code = forms.CharField(max_length=100)
    country = forms.CharField(max_length=100)
    room_type = forms.ModelChoiceField(queryset=RoomType.objects.all())
    check_in_date = forms.DateField()
    check_out_date = forms.DateField()