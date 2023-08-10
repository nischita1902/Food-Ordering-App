import sys
from admin import *
from user import *

admin = Admin_Panel()
user = User_Panel()

while True:
    print("Press 1 for Admin Login")
    print("Press 2 for User Login")
    print("Press 3 for Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        username = input("Enter Admin Username: ")
        password = input("Enter Admin Password: ")
        
        if admin.admin_login(username, password):
            print("Successfully Loged In")
            while True:
                print("Press 1 for Add Food Items: ")
                print("Press 2 for Edit Food Items: ")
                print("Press 3 for Read Food Items: ")
                print("Press 4 for Remove Food Items: ")
                print("Press 5 for Logout: ")

                admin_choice = int(input("Enter Your Choice: "))

                if admin_choice == 1:
                    print(admin.add_food_items())
                    print(".......Food Item Added Successfully.....")
                
                elif admin_choice == 2:
                    print(admin.edit_food_items())
                    print(".......Food Item Updated Successfully.....")
                
                elif admin_choice == 3:
                    admin.read_food_items()
                
                elif admin_choice == 4:
                    print(admin.remove_food_items())
                    print("........Food Item Removed Successfully.....")
                
                elif admin_choice == 5:
                    print("......Logged out...")
                    break
                
                else:
                    print("Please enter a valid choice")
        
        else:
            print("Invalid Credentials")

    elif choice == 2:
        username = input("Enter User Username: ")
        password = input("Enter User Password: ")
        
        if user.user_login(username, password):
            print(" Successfully Logged In")
            while True:
                print("Press 1 for Place Order")
                print("Press 2 for Order History")
                print("Press 3 for Update User Profile")
                print("Press 4 for Logout")
                user_choice = int(input("Enter Your Choice: "))

                if user_choice == 1:
                    user.place_order()
                
                elif user_choice == 2:
                    print(user.order_history())
                
                elif user_choice == 3:
                    print(user.update_user())
                    print("User Profile Updated Successfully")
                
                elif user_choice == 4:
                    print("Logged out")
                    break
                
                else:
                    print("Please enter a valid choice")
        else:
            print('Invalid Credentials')
    
    if choice == 3:
        print("Thank You for using our application")
        sys.exit()
