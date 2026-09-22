#just like how you took student name and marks and displayed it
#take orders and display it

orders={}
#2 ways to take order:
#1. do you have a menu, or do you want to first take their order and then check if it is there or not?
#i think for beginner display menu..make it easy...
'''
name=input("Enter your name: ")
order=input("give your order: ")

print("please wait in the waiting area, your order will be served soon..")
orders[name]=order
'''
class Order:
    order_count=0
    def __init__(self, order, quantity):
        self.orderid=Order.order_count
        Order.order_count+=1
        self.order=order
        self.quantity=quantity
        payable=Menu[self.order]*self.quantity
        self.amount=payable
     
        

    def print_order_details(self):
        print(f'\n\nyour order id: {self.orderid} \nyour order:{self.order} \nquantity: {self.quantity}\n amount: {self.amount}\n')

    def take_out():
        print("your order will be ready in 5 minutes, please collect it and enjoy!!!")
        print("thank you for choosing UD")
        print("see you again for a fantastic meal!!!")
       

#let us not make this a class method, and use this function to create ojects inside it
#can a function call a class and create object? -we can inside the function definition




while False:
    name=input("Enter your name: ")
    order=input("give your order: ")
    quantity=input('Enter quantity: ')
    order1=Order(order, quantity)
    order1.print_order_details()

#features:
#1. view menu
#2. create account
#3. make order
#4. simulate payment
#5. give feedback

#how to implement create account feature

class Account :
    users={}
    def __init__(self, username, password):
        self.username=username
        self.password=password
        self.orders=[]
        if self.username not in Account.users.keys():
            Account.users[self.username]=self.password
    def login(self):
        print('login succesful!!')
        return self

        
    def create_account(self):
        Account.users[self.username]=self.password
        print(f"Account with username {self.username} created succesfully.. ")
        print(" you can start ordering from now...\n")

    def print_menu(self):
        print("Here is your menu: ")
        print("_"*40)
        for key, value in Menu.items():
         print(key, '------>', value)


'''
class Menu:
    def __init__(self, order_name, order_cost):
        pass'''
#do i need a class for this? or is a dictionary enough?
Menu={}
class Owner:
    
    def add_item(self):
     while True:
        n=int(input("enter how many items you want to add: "))
        tem_dic={}
        for i in range(1,n+1):
        
            name=input(f"Enter item {i}: ")
            price=int(input("Enter item price: "))
            tem_dic[name]=price
        print(tem_dic)
        retry=input("is this good or do you want to retry?(y/n): ")
        if retry=='y':
              break
        else:
             Menu.update(tem_dic)

        print(f"{len(tem_dic)} items added successfully to the menu!!")
        #print(Menu)
        print("Here is your updated menu: ")
        print("_"*40)
        for key, value in Menu.items():
            print(key, '------>', value)
        print()
        print()
        print()
        break

#main block:
print('welcome to upahara darshini!!!')
print("dear chef, please add to the menu...")
chef=Owner()
chef.add_item()

def create_acclogin():
    def view_menu():
           l1.print_menu()
    username=input("Enter your username: ")
    password=input("Enter password: ")
    l1=Account(username, password)
    l1.login()
    view_menu()
    


create_acclogin()



#now we have code for adding items to the menu and displaying price
#we can put this in chef/owner class and provide it as a method

def place_ord():
    order=input("Enter your order name: ")
    quantity=int(input("enter order quantity: "))
    o1=Order(order,quantity)
    o1.print_order_details()
    Order.take_out()
place_ord()

"""
welcome to upahara darshini!!!
dear chef, please add to the menu...
enter how many items you want to add: 7
Enter item 1: cofee
Enter item price: 5
Enter item 2: tea
Enter item price: 10
Enter item 3: badam milk
Enter item price: 15
Enter item 4: idli
Enter item price: 15
Enter item 5: dosa
Enter item price: 20
Enter item 6: chapathi
Enter item price: 25
Enter item 7: poori
Enter item price: 30
{'cofee': 5, 'tea': 10, 'badam milk': 15, 'idli': 15, 'dosa': 20, 'chapathi': 25, 'poori': 30}
is this good or do you want to retry?(y/n): n
7 items added successfully to the menu!!
Here is your updated menu: 
________________________________________
cofee ------> 5
tea ------> 10
badam milk ------> 15
idli ------> 15
dosa ------> 20
chapathi ------> 25
poori ------> 30



Enter your username: rachana
Enter password: 123456
login succesful!!
Here is your menu: 
________________________________________
cofee ------> 5
tea ------> 10
badam milk ------> 15
idli ------> 15
dosa ------> 20
chapathi ------> 25
poori ------> 30
Enter your order name: idli
enter order quantity: 5


your order id: 0 
your order:idli 
quantity: 5
 amount: 75

your order will be ready in 5 minutes, please collect it and enjoy!!!
thank you for choosing UD
see you again for a fantastic meal!!!
"""

#now this is working fine!!
#we need to add multiple item order taking feature to this..
#it will be ossum...
