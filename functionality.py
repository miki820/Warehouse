import sqlite3

con = sqlite3.connect('warehouse.db')
con.row_factory = sqlite3.Row
cur = con.cursor()


# Function to add product to database
def add_product(name, description, price, amount):
    cur.execute("INSERT INTO Product (name, description, price, amount) VALUES (?, ?, ?, ?)",
                (name, description, price, amount))

    con.commit()
    print("\nProduct has been successfully added to the warehouse.\n")


# Function to find product by ID or name
def find_product(id_or_name):
    if id_or_name.isnumeric():
        cur.execute("SELECT * FROM Product WHERE id = ?", (id_or_name,))
    elif not id_or_name.isnumeric():
        cur.execute("SELECT * FROM Product WHERE name LIKE ?", (id_or_name,))
    else:
        print("\nInvalid name!\n")
        return

    products = cur.fetchall()

    print()
    if len(products) > 0:
        for product in products:
            print_product_details(product)
    else:
        print("No products found!\n")


# Function to edit product details
def edit_product(id_product):
    if not id_product.isnumeric():
        print("\nInvalid ID!\n")
        return

    cur.execute("SELECT * FROM Product WHERE id = ?", (id_product,))
    products = cur.fetchall()
    if len(products) == 0:
        print("\nProduct not found!\n")
        return

    print("\nDo you want to change all values of the product or just the single one?")
    print("1. All values")
    print("2. Single value")
    choice = input()

    if choice == "1":
        edit_product_all(id_product)
    elif choice == "2":
        edit_product_single(id_product)
    else:
        print("\nInvalid option! Please try again.\n")


# Function to edit a single product detail
def edit_product_single(id_product):
    print()
    print("Choose what you want to change:")
    print("1. Name")
    print("2. Description")
    print("3. Price")
    print("4. Quantity")
    to_change = input()

    if to_change == "1":
        name = input("\nEnter the new product name: ")
        cur.execute("UPDATE Product SET name = ? WHERE id == ?", (name, id_product))
        con.commit()
        print("\nThe product name has been changed.\n")
    elif to_change == "2":
        description = input("\nEnter the new product description: ")
        cur.execute("UPDATE Product SET description = ? WHERE id == ?", (description, id_product))
        con.commit()
        print("\nThe product description has been changed.\n")
    elif to_change == "3":
        try:
            price = float(input("\nEnter the new product price: "))
        except ValueError:
            print("\nInvalid input type! Please enter a valid number.\n")
        else:
            cur.execute("UPDATE Product SET price = ? WHERE id == ?", (price, id_product))
            con.commit()
            print("\nThe product price has been changed.\n")
    elif to_change == "4":
        try:
            amount = int(input("\nEnter the new quantity of product: "))
        except ValueError:
            print("\nInvalid input type! Please enter a valid number.\n")
        else:
            cur.execute("UPDATE Product SET amount = ? WHERE id == ?", (amount, id_product))
            con.commit()
            print("\nThe product quantity has been changed.\n")
    else:
        print("\nInvalid option! Please try again.\n")


# Function to edit all details of a product
def edit_product_all(id_product):
    print()
    try:
        name = input("Enter the new product name: ")
        description = input("Enter the new product description: ")
        price = float(input("Enter the new product price: "))
        amount = int(input("Enter the new quantity of product: "))
    except ValueError:
        print("\nInvalid input type! Please enter valid values.\n")
    else:
        cur.execute("UPDATE Product SET name = ?, description = ?, price = ?, amount = ? WHERE id == ?",
                    (name, description, price, amount, id_product))
        con.commit()
        print("\nThe product details have been updated.\n")


# Function to delete a product
def delete_product(id_product):
    if not id_product.isnumeric():
        print("\nError: Invalid ID!\n")
        return

    cur.execute("SELECT * FROM Product WHERE id = ?", (id_product,))
    products = cur.fetchall()
    if len(products) == 0:
        print("\nProduct not found!\n")
        return

    cur.execute("DELETE FROM Product WHERE id == ?", (id_product,))
    con.commit()
    print("\nThe product has been successfully deleted!\n")


# Function to generate a report
def generate_report():
    print("\nChoose the parameter to sort the report by:")
    print("1. ID")
    print("2. Name")
    print("3. Description")
    print("4. Price")
    print("5. Quantity")

    if sort(input()) == "Error":
        return


# Function to sort the report
def sort(choice):
    cur.execute("SELECT * FROM Product")
    products = cur.fetchall()
    if choice == "1":
        print("\nSorting by ID...")
        sorted_products = sorted(products, key=lambda x: x[0])
    elif choice == "2":
        print("\nSorting by name...")
        sorted_products = sorted(products, key=lambda x: x[1])
    elif choice == "3":
        print("\nSorting by description...")
        sorted_products = sorted(products, key=lambda x: x[2])
    elif choice == "4":
        print("\nSorting by price...")
        sorted_products = sorted(products, key=lambda x: x[3])
    elif choice == "5":
        print("\nSorting by quantity...")
        sorted_products = sorted(products, key=lambda x: x[4])
    else:
        print("\nInvalid parameter, sorting not possible!\n")
        return "Error"

    print("Generating a report of all products in the warehouse...\n")

    print("=== Start of report ===\n")
    for product in sorted_products:
        print_product_details(product)
    print("=== End of report ===\n")

    print("Do you want to save the report to a file?")
    print("1. Yes")
    print("2. No")
    to_file = input()
    if to_file == "1":
        write_to_file(sorted_products)
        print("\nThe report has been saved to a file.\n")
    elif to_file == "2":
        print()
        return
    else:
        print("\nInvalid option, report not saved to a file!\n")


# Function to write product details to a file
def write_to_file(sorted_products):
    with open("report.txt", "w") as file:
        for product in sorted_products:
            file.write("Id: " + str(product['id']) + "\n")
            file.write("Name: " + str(product['name']) + "\n")
            file.write("Description: " + str(product['description']) + "\n")
            file.write("Price: " + str(product['price']) + "\n")
            file.write("Amount: " + str(product['amount']) + "\n")
            file.write("\n")


# Function to print product details
def print_product_details(product):
    print("Id:", product['id'])
    print("Name:", product['name'])
    print("Description:", product['description'])
    print("Price:", product['price'])
    print("Amount:", product['amount'])
    print()
