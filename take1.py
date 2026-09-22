"""
Upahara Darshini - a simple restaurant ordering system.

Features:
- Chef/owner adds menu items with price and stock
- Customer creates an account / logs in
- Customer can order multiple items in one visit (cart), stopping when they choose
- Stock is checked and reduced as orders are placed
- Basic exception handling so a bad input doesn't crash the whole session
"""

# Menu is shared across the whole program: {item_name: {"price": int, "stock": int}}
Menu = {}


class Order:
    """A single line-item order (one menu item + quantity)."""

    order_count = 0

    def __init__(self, order, quantity):
        if order not in Menu:
            raise ValueError(f"Sorry, '{order}' is not on the menu.")
        if quantity <= 0:
            raise ValueError("Quantity must be a positive number.")
        if Menu[order]["stock"] < quantity:
            raise ValueError(
                f"Sorry, only {Menu[order]['stock']} of '{order}' left in stock."
            )

        self.orderid = Order.order_count
        Order.order_count += 1
        self.order = order
        self.quantity = quantity
        self.amount = Menu[order]["price"] * quantity

        # reduce stock immediately once the order is confirmed valid
        Menu[order]["stock"] -= quantity

    def print_order_details(self):
        print(
            f"\norder id: {self.orderid} | item: {self.order} "
            f"| qty: {self.quantity} | amount: {self.amount}"
        )

    @staticmethod
    def take_out():
        print("\nyour order will be ready in 5 minutes, please collect it and enjoy!!!")
        print("thank you for choosing UD")
        print("see you again for a fantastic meal!!!")


class Account:
    """Handles user signup/login and viewing the menu."""

    users = {}

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.orders = []
        if self.username not in Account.users:
            Account.users[self.username] = self.password

    def login(self):
        print("login successful!!")
        return self

    def create_account(self):
        Account.users[self.username] = self.password
        print(f"Account with username {self.username} created successfully.")
        print("you can start ordering from now...\n")

    def print_menu(self):
        print("Here is your menu: ")
        print("_" * 40)
        for name, details in Menu.items():
            status = "SOLD OUT" if details["stock"] == 0 else f"stock: {details['stock']}"
            print(f"{name} ------> {details['price']}  ({status})")


class Owner:
    """Handles adding items (with price and stock) to the shared Menu."""

    def add_item(self):
        while True:
            try:
                n = int(input("enter how many items you want to add: "))
            except ValueError:
                print("please enter a whole number.")
                continue

            tem_dic = {}
            for i in range(1, n + 1):
                name = input(f"Enter item {i}: ").strip()
                try:
                    price = int(input("Enter item price: "))
                    stock = int(input("Enter item stock: "))
                except ValueError:
                    print("price and stock must be numbers. skipping this item.")
                    continue
                tem_dic[name] = {"price": price, "stock": stock}

            print(tem_dic)
            confirm = input("is this good? (y/n): ").strip().lower()

            if confirm == "y":
                Menu.update(tem_dic)
                print(f"{len(tem_dic)} items added successfully to the menu!!")
                print("Here is your updated menu: ")
                print("_" * 40)
                for name, details in Menu.items():
                    print(f"{name} ------> {details['price']}  (stock: {details['stock']})")
                break
            else:
                print("ok, let's re-enter the items.\n")
                # loop again without saving tem_dic


def create_acclogin():
    """Handles account creation/login, then shows the menu."""
    username = input("Enter your username: ")
    password = input("Enter password: ")
    account = Account(username, password)
    account.login()
    account.print_menu()
    return account


def take_order():
    """Takes a single item order from the customer. Returns an Order, or None if it failed."""
    order_name = input("Enter your order name: ").strip()
    try:
        quantity = int(input("enter order quantity: "))
    except ValueError:
        print("quantity must be a number. that item wasn't added.")
        return None

    try:
        order = Order(order_name, quantity)
        order.print_order_details()
        return order
    except ValueError as e:
        print(e)
        return None


def print_receipt(cart):
    print("\n----- Your Receipt -----")
    if not cart:
        print("(no items ordered)")
        return
    total = 0
    for o in cart:
        print(f"{o.order} x{o.quantity} = {o.amount}")
        total += o.amount
    print(f"Total: {total}")


def place_order():
    """Loops, taking multiple orders into a cart, until the customer says they're done."""
    cart = []
    while True:
        order = take_order()
        if order is not None:
            cart.append(order)

        more = input("Do you want to order anything else? (y/n): ").strip().lower()
        if more != "y":
            break

    print_receipt(cart)
    if cart:
        Order.take_out()
    return cart


def main():
    print("welcome to upahara darshini!!!")
    print("dear chef, please add to the menu...")
    chef = Owner()
    chef.add_item()

    create_acclogin()
    place_order()


if __name__ == "__main__":
    main()
