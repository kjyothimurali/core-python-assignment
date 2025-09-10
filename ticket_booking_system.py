#booking ticket if available
def booking(book_seat):
    if book_seat not in booked_seats:
        booked_seats.append(book_seat)
        print("ticket booked")
    else:
        print(f"{book_seat} is not available")
    
#cancelling ticket
def cancellation(seat):
    if seat in booked_seats:
        booked_seats.remove(seat)

#displaying available seats
def available_seats(n):
    available=[]
    for i in range(1,n+1):
        if i not in booked_seats:
            available.append(i)

    print("Available seats: ",available)
    


total_seats=int(input("enter total seats: "))
booked_seats=list(map(int,input("enter booked seats: ").split(",")))
book_seat=int(input("enter seat number to book: "))
booking(book_seat)
cancel_seat=int(input("enter seat number to cancel: "))
cancellation(cancel_seat)
available_seats(total_seats)
