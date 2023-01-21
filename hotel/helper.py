import datetime
from .models import Room, CheckIn

def check_availability(room_number, check_in_date, check_out_date):
    # getting room object
    room = Room.objects.get(room_number=room_number)
    # converting string to datetime object
    check_in_date = datetime.datetime.strptime(check_in_date, '%Y-%m-%d')
    check_out_date = datetime.datetime.strptime(check_out_date, '%Y-%m-%d')
    # checking if there are existing check in or check out in between the requested check in and check out date
    check_in = CheckIn.objects.filter(room=room, check_in_date__lte=check_in_date, check_out_date__gte=check_in_date)
    check_out = CheckIn.objects.filter(room=room, check_in_date__lte=check_out_date, check_out_date__gte=check_out_date)
    
    if check_in or check_out:
        # if exists then room is not available
        return False
    else:
        # if not exists then room is available
        return True