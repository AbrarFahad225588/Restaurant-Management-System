from users import Customers,Admin,Employ
from orders import Orders
from restaurent import restaurent
from menu import Menu
from food_item import FoodItem

mama_restaurent=restaurent('mamar restaurent')
def customer_menu():
    name=input('Enter Your name : ')
    email=input('Enter Your email : ')
    phone=input('Enter Your phone: ')
    adress=input('Enter Your adress : ')
    customer=Customers(name=name,email=email,phone=phone,adress=adress)
    while True:
        print(f"***Welcome {customer.name} to our mama_restaurent****")
        print("---------------------------------------------------------")
        print("1.View Menu")
        print("2.Add to Cart")
        print("3.View Cart")
        print("4.Pay Bill")
        print("5.Exit")
        op=int(input("Enter option : "))
        if op==1:
            customer.view_menu(mama_restaurent)
        elif op==2:
            item_name=input('Enter item name : ')
            item_quantity=int(input('Enter item quantity : '))  
            customer.add_to_cart(mama_restaurent,item_name,item_quantity) 
        elif op==3:
            customer.view_cart()
        elif op==4:
            customer.pay_bill()   
        elif op==5:
            print("Thank you for visiting mama_restaurent")
            break
        else:
            print("Invalid option")
            
            
            
def admin_menu():
    name=input('Enter Your name : ')
    email=input('Enter Your email : ')
    phone=input('Enter Your phone: ')
    adress=input('Enter Your adress : ')
    admin=Admin(name=name,email=email,phone=phone,adress=adress)
    while True:
        print(f"***Welcome {admin.name} to your mama_restaurent****")
        print("---------------------------------------------------------")
        print("1.Add New Item")
        print("2.Add New Employ")
        print("3.View Employees")
        print("4.View Items")
        print("5.Delete Item")
        print("6.Exit")
        op=int(input("Enter option : "))
        if op==1:
            item_name=input('Enter item name : ')
            item_price=int(input('Enter Item Price : '))
            item_quantity=int(input('Enter Item Quantity : '))
            item=FoodItem(item_name,item_price,item_quantity)
            admin.add_menu_item(mama_restaurent,item)
        elif op==2:
            name=input('Enter Employee name : ')
            age=input('Enter Employee age : ')
            phone=input('Enter Employee phone : ')
            designation=input('Enter Employee designation : ')
            adress=input('Enter Employee adress : ')
            salary=input('Enter Employee salary : ')
            email=input('Enter Employee email : ')
            employ=Employ(name, phone, email, adress,age,designation,salary)
            admin.add_employee(mama_restaurent,employ)  
        elif op==3:
            admin.view_employ(mama_restaurent)
        elif op==4:
            admin.view_menu(mama_restaurent)
        elif op==5:
            item_name=input('Enter Item Name : ')
            admin.remove_item(mama_restaurent,item_name)
        elif op==6:
            
            print('Successfully Exit your mama restaurent')
            break
            
        else:    
            print("Invalid option")            
            
            
            
            
            
            
while True:
    print('Welcome to our khwar duniya')
    print('1.Admin Interface')
    print('2.User Interface')
    print('3.Exit')
    op=int(input('Enter a option : '))
    if op==1:
        admin_menu()
    elif op==2:
        customer_menu()
    elif op==3:
        print('Successfully Exit your mama restaurent')
        break
    else:
        print("Invalid option")  
        
          
        
    