#  diamond pattern


# n=5
# for i in range(n):
#     print(" "*(n-i-1),end="")
#     for j in range(2*i+1):
#        print("*",end="")
#     print()
# for i in range (n-2,-1,-1):
#        print(" "*(n-i-1),end="")
#        for j in range(2*i+1):
#          print("*",end="")
#        print()





# reversing of list 

# l=[10,20,30,40,50]
# l1=[]
# i=len(l)-1
# while(i>=0):
#     l1.append(l[i])
#     i-=1
# print(l1) 



# prime number


# num=int(input("Enter a number"))

# if num <=1:
#     print("Not a prime number")
# else:
#     for i in range(2,num):
#        if num %i ==0:
#             print("Not prime number")
#             break
#     else:
# #          print("Prime numer")


# machine test


# bookings = {}

# def book_room():
#     room = input("Enter Room Number: ")

#     if room in bookings:
#         print("Room Number is already booked.")
#     else:
#         name = input("Enter Guest Name: ")
#         rtype = input("Enter Room Type: ")
#         days = int(input("Enter Number of Days: "))
#         price = float(input("Enter Total Price: "))

#         if days > 0 and price > 0:
#             bookings[room] = {
#                 "Name": name,
#                 "Type": rtype,
#                 "Days": days,
#                 "Price": price
#             }
#             print("Room Booked Successfully.")
#         else:
#             print("Invalid Days or Price")

# def view_bookings():
#     if len(bookings) == 0:
#         print("No Booking Records Found.")
#     else:
#         for room, details in bookings.items():
#             print("Room Number:", room)
#             print("Guest Name:", details["Name"])
#             print("Room Type:", details["Type"])
#             print("Days:", details["Days"])
#             print("Price:", details["Price"])
#             print("--------------------")

# def search_booking():
#     room = input("Enter Room Number: ")
#     if room in bookings:
#         print(bookings[room])
#     else:
#         print("Booking Not Found.")

# def update_days():
#     room = input("Enter Room Number: ")
#     if room in bookings:
#         days = int(input("Enter New Number of Days: "))
#         if days > 0:
#             bookings[room]["Days"] = days
#             print("Booking Days Updated Successfully.")
#         else:
#             print("Invalid Days")
#     else:
#         print("Booking Not Found.")

# def cancel_booking():
#     room = input("Enter Room Number: ")
#     if room in bookings:
#         del bookings[room]
#         print("Booking Cancelled Successfully.")
#     else:
#         print("Booking Not Found.")

# while True:
#     print("\nHotel Room Booking System")
#     print("1. Book Room")
#     print("2. View All Bookings")
#     print("3. Search Booking")
#     print("4. Update Booking Days")
#     print("5. Cancel Booking")
#     print("6. Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         book_room()
#     elif choice == 2:
#         view_bookings()
#     elif choice == 3:
#         search_booking()
#     elif choice == 4:
#         update_days()
#     elif choice == 5:
#         cancel_booking()
#     elif choice == 6:
#         print("Thank You... Program cancelled.")
#         break
#     else:
#         print("Invalid Choice")


