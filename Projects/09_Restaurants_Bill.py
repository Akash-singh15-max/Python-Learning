# Restaurants Bill System
import json
import os
import datetime

# File to store invoice
FILE_NAME = "Restaurantbill.json"

# Function to generate bill header
def generate_bill_header(customer,date):
    print("\n\n")
    print("\t       AKU RESTAURANT")
    print("\t    ====================")
    print(f"Date : {date}")
    print(f"Invoice to : {customer}")
    print("\n-------------------------------------------")
    print("Items\t\tQty\t\tTotal")
    print("-------------------------------------------\n")

# Function to generate bill body
def generate_bill_body(item, qty, price):
    print(f"{item.ljust(15)}\t{str(qty).ljust(8)}\t{price*qty:.2f}")

# Function to generate bill footer
def generate_bill_footer(total):
    discount = 0.1 * total
    net_total = total - discount
    cgst = 0.09 * net_total
    grand_total = net_total + (2 * cgst)    # sgst

    print("\n-------------------------------------------")
    print(f"Sub Total\t\t\t{total:.2f}")
    print(f"Discount @10%\t\t\t{discount:.2f}")
    print("-------------------------------------------")
    print(f"Net Total\t\t\t{net_total:.2f}")
    print(f"CGST @9%  \t\t\t{cgst:.2f}")
    print(f"SGST @9%  \t\t\t{cgst:.2f}")
    print("-------------------------------------------")
    print(f"Grand Total\t\t\t{grand_total:.2f}")
    print("-------------------------------------------")

# Function to save invoice
def save_invoice(order):
    try:
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME,"w") as file:
                orders = json.load(file)
        else:
            orders = []
        
        orders.append(order)
        with open(FILE_NAME,"w") as file:
            json.dump(orders,file,indent=4)

        print("\nInvoice saved successfully!")
    except Exception as e:
        print(f"Error saving invoice: {e}")
    
# function to load invoice from file
def load_invoices():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME,"r") as file:
            return json.load(file)
    return []

# Function to generate a new invoice
def generate_invoice():
    os.system("cls")
    customer = input("Enter customer name : ").strip()
    date = datetime.date.today().strftime("%d %B, %Y")
    try:
        num_items = int(input("\nEnter number of items: "))
        items = []
        total = 0
        for i in range(num_items):
            print(f"\nEnter details for item {i+1}: ")
            item_name = input("\nItem Name : ").strip()
            qty = int(input("Quantity : "))
            price = float(input("Unit Price : "))
            items.append({"item" : item_name, "qty" : qty, "price" : price})
            total += qty*price

        # Display the bill
        generate_bill_header(customer,date)
        for item in items:
            generate_bill_body(item["item"], item["qty"], item["price"])
        generate_bill_footer(total)

        # Save invoice option
        save_option = input("\nSave Invoice? (y/n): ").strip().lower()
        if save_option == 'y':
            save_invoice({"customer" : customer, "date" : date, "items" : items})
    except ValueError:
        print("Invalid input. Please enter valid numbers for quantity and price.")

# Function to show all invoices
def show_all_invoices():
    os.system("cls")
    invoices = load_invoices()
    if not invoices:
        print("\nNo previous invoices found!\n")
        return
    print("\n***** Previous Invoices *****\n")
    for order in invoices:
        total = sum(item["qty"] * item["prices"] for item in order["items"])
        generate_bill_header(order["customer"],order["date"])
        for item in order["items"]:
            generate_bill_body(item["item"], item["qty"], item["price"])
        generate_bill_footer(total)

# Function to search for an invoice by customer name
def search_invoice():
    os.system("cls")
    name = input("Enter Customer name : ").strip()
    invoices = load_invoices()
    found = False
    for order in invoices:
        if order["Customer"].lower()==name.lower():
            total = sum(item["qty"] * item["price"] for item in order["items"])
            generate_bill_header(order["customer"],order["date"])
            for item in order["items"]:
                generate_bill_body(item["item"], item["qty"], item["price"])
            generate_bill_footer(total)
            found = True

    if not found:
        print(f"\nNo invoice found for {name}\n")

# Main menu function
def main():
    while True:
        os.system("cls")
        print("\t========== AKU RESTAURANTS ==========")
        print("\n1. Generate Invoice")
        print("2. Show all Invoices")
        print("3. Search Invoice")
        print("4. Exit")
        choice = input("\nEnter your choice: ").strip()

        if choice == '1':
            generate_invoice()
        elif choice == '2':
            show_all_invoices()
        elif choice == '3':
            search_invoice()
        elif choice == '4':
            print("\nThank you for using the system. Goodbye! :)\n")
            break
        else:
            print("\nInvalid choice, please try again.\n")

        input("\nPress enter to continue....")

# Run the main function
if __name__=="__main__":
    main()