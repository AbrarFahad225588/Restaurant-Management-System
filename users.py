from abc import ABC
from orders import Orders
class Users(ABC):
    def __init__(self, name, phone, email, adress):
        self.name=name 
        self.phone=phone
        self.email=email
        self.adress=adress
class Customers(Users):
    def  __init__(self, name, phone, email, adress):
        super().__init__(name, phone, email, adress) 
        self.cart=Orders()
    def view_menu(self,restaurent) :
        restaurent.menu.show_menu() 
    def add_to_cart(self,restaurent,item_name,quantity):
        item=restaurent.menu.find_item(item_name) 
        if item:
            if quantity > item.quantity:
                print("Sorry we don't have enough quantity of this item")
            else:
                    
                item.quantity=quantity
                self.cart.add_item(item)
                print("Item Added")
        else:
            print("item not found")
    def view_cart(self):
        print('***View Cart***')     
        print('Name\tPrice\tQuantity') 
        for item,quantity in  self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{ quantity}")
        print(f'total price : {self.cart.total_price}') 
    def pay_bill(self):
        print(f'pay bill {self.cart.total_price} tk \n paid successfully !!')
        self.cart.clear()
             
class Employ(Users):
    def __init__(self, name, phone, email, adress,age,designation,salary):
        self.age=age
        self.designation=designation
        self.salary=salary
        super().__init__(name, phone, email, adress) 
              
class Admin(Users):
    def __init__(self, name, phone, email, adress):
        super().__init__(name, phone, email, adress)
    def add_employee(self,restaurent, employee) :
        restaurent.add_employee(employee)
    def view_employ(self,restaurent):
        restaurent.view_employ()
    def add_menu_item(self,restaurent,item):
        restaurent.menu.add_menu_item(item)
    def remove_item(self,restaurent,item):
        restaurent.menu.remove_item(item)  
    def view_menu(self,restaurent):
        restaurent.menu.show_menu()               

        
 
        

    



        
        
        
# mama_retaurent=restaurent("mama_Restaurent")
# admin=Admin('fahad',123123,'dhfgd@gmail.com','dhaka')        
# mn=Menu()  
# item=FoodItem('pizza',50,10)
# item1=FoodItem('Burger',20,20)
# item2=FoodItem('noodles',30,15)
# admin.add_menu_item(mama_retaurent,item)   
# admin.add_menu_item(mama_retaurent,item1)   
# admin.add_menu_item(mama_retaurent,item2)   
 
# customer=Customers('lamim',123123,'rere@gmail.com','dhaka')  

# customer.view_menu(mama_retaurent) 
# item_name=input('Enter item name: ')
# item_quantity=int(input('Enter item quantity: '))
# customer.add_to_cart(mama_retaurent,item_name,item_quantity)
# customer.view_cart()
                
            
     