reservations = {}
def is_room(room_number):
    if reservations[room_number] is None:
      return True
    else:
      return False

def make_reservation(room_number,name,check_in_date);
    if reservations[room_number] is None:
       reservations={
          'room_number': room_number,
          'name': name,
          'check_in_date': check_in_date
       }
       reservations[room_number]= reservations
       print ("Reservation successful")
    else:
       print("Room already taken")