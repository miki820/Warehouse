import functionality
import sqlite3

# Establish connection to the SQLite database
con = sqlite3.connect('warehouse.db')
con.row_factory = sqlite3.Row
cur = con.cursor()

while True:
    # User Interface
    print("Menu")
    print("1. Add product")
    print("2. Find product")
    print("3. Update product")
    print("4. Delete product")
    print("5. Generate raport")
    print("6. Exit")

    number = input("Choose an option: ")

    if number == "1":
        try:
            print()
            name = input("Enter the product name: ")
            description = input("Enter the product description: ")
            price = float(input("Enter the product price: "))
            amount = int(input("Enter the available quantity: "))
        except ValueError:
            print("\nInvalid input type!\n")
        else:
            functionality.add_product(name, description, price, amount)
    elif number == "2":
        product_id = input("\nEnter the product name or ID: ")
        functionality.find_product(product_id)
    elif number == "3":
        product_id = input("\nEnter the product ID you want to update: ")
        functionality.edit_product(product_id)
    elif number == "4":
        product_id = input("\nEnter the product ID you want to delete: ")
        functionality.delete_product(product_id)
    elif number == "5":
        functionality.generate_report()
    elif number == "6":
        con.close()
        break
    else:
        print("\nInvalid option! Please Try Again\n")
