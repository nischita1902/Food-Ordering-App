#User Functionalities
import json
class User_Panel:
    def __init__(self):
        self.count=0
        self.main_user_dict={}
        self.order_hist_dict={}

#User Registration

    def user_register(self):
        self.count+=1
        Full_name=input('Enter Full Name: ')
        Phone_number=int(input('Enter Phone Number: '))
        Email=input('Enter Your Email ID: ')
        Address=input('Enter Address: ')
        Password=input('Enter Password: ')
        user_dict={'FullName':Full_name,'PhoneNumber':Phone_number,'EmailID':Email,'Address':Address,'Password':Password}
        self.main_user_dict[self.count]=user_dict
        with open('User.json','w') as f:
            json.dump(self.main_user_dict,f,indent=4)
        return self.main_user_dict

#User Login

    def user_login(self,username,password):
        if username=='Nischita' and password=='Sweety':
            return True
        return False

#Place Order
    def place_order(self):
        order_dict={1:{'Name':'Tandoori Chicken','Quantity':'4 Pieces','Price':'INR 240'},2:{'Name':'Vegan Burger','Quantity':'1 Piece','Price':'INR 320'},3:{'Name':'Truffle Cake','Quantity':'500 Grams','Price':'INR 900'}}
        for k,v in order_dict.items():
            print(f"{k}. {v['Name']} ({v['Quantity']}) [{v['Price']}]")
        order_items=input('Enter the FoodID to be Ordered sperated by commas: ')
        order_list=[int(i.strip()) for i in order_items.split(',')]
        selected_items=[]
        for i in order_list:
            item=order_dict.get(i)
            if item:
                selected_items.append(item)
            else:
                return 'Wrong FoodID'
        if selected_items:
            for item in selected_items:
                print(f"{item['Name']} ({item['Quantity']}) [{item['Price']}]")
        confir=input('Enter (yes/no) for order placing: ')
        if confir.lower() == "yes":
            print('Order Placed... [Enjoy your Food......]')
            self.order_hist_dict['Order History']=selected_items
        else:
            print(' [Unfortunately] Your Order has been Cancelled')
        
# Order History
   
    def order_history(self):
        return self.order_hist_dict
# Update Profile
   
    def update_user(self):
        with open('User.json','r') as f:
            data = json.load(f)
        for k,v in data.items():
            print(f"User ID': {k} || User Details: {v}")
        update_id=input('Enter ID you want to update: ')
        field=input('Enter field you want to update: ')
        updated_value=input('Enter Updated value: ')
        data[update_id][field]=updated_value
        print('Your Profile Is Successfully Updated')
        with open("Updated_User.json","w")as f:
            json.dump(data,f,indent=4)
        return data
