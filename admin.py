#Admin Functionalities
import json
class Admin_Panel:
    def __init__(self):
        self.count=0
        self.main_food_dict={}
        self.updated_food={}

    def admin_login(self,username,password):
        if username=='Nischita' and password=='Sweety':
            return True
        return False

    def add_food_items(self):
        self.count+=1
        Food_name=input(f'Enter name of food: ')
        Quantity=input(f"Enter number of Qunatity: ")
        Stock=input(f'Enter the Stock Quantity of food: ')
        Price=float(input(f"Enter price per item of food: "))
        Discount=(Price*25)/100
        food_dict={'FoodName':Food_name,'Quantity':Quantity,'Stock':Stock,'Price':Price,'Discount':Discount}
        self.main_food_dict[self.count]=food_dict
        with open('Food_add.json','w') as f:
            json.dump(self.main_food_dict,f,indent=4)
        return self.main_food_dict
    
    def edit_food_items(self):
      
        with open('Food_add.json','r') as f:
            data=json.load(f)
        for k,v in data.items():
            print(f'FoodID: {k} || Food_Details: {v}')

        food_id=input('Enter the FoodID you want to update: ')
        Field=input('Enter the field you want to update: ')
        updated_value=input('Enter the updated value: ')
        data[food_id][Field]=updated_value
        with open('Updated_Food.json','w') as f:
            json.dump(data,f,indent=4)
        return data
    
    def read_food_items(self):
        with open('Updated_Food.json','r') as f:
            data=json.load(f)
        for k,v in data.items():
            print(f'FoodID: {k} || Food_Details: {v}')

    def remove_food_items(self):
        with open('Updated_Food.json','r') as f:
            Data=json.load(f)
        for k,v in Data.items():
            print(f'FoodID: {k} || Food_Details: {v}')
        remove_food=input('Enter FoodID which you want to delete: ')
        del Data[remove_food]
        return Data
