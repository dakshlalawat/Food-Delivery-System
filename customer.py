import mysql.connector  # Import MySQL module

# Connect to MySQL
c = mysql.connector.connect(
    host="localhost",
    user="root",
    password="daksh@4321", 
    database="canteen"
)
cursor = c.cursor()  # Creates a cursor to execute SQL commands


menu = {
    1: ("Vada Pav", 40),
    2: ("Lime Water", 40),
    3: ("Oreo Shake", 70),
    4: ("Paneer Prantha", 75),
    5: ("Cold Coffee", 70)
}


# Show menu
print("\n Canteen Menu ")
for key, value in menu.items():
     print(f"{key}. {value[0]} - ₹{value[1]}")


student_id = input("\nEnter Student ID: ")
name = input("Enter Name: ")
room_no = input("Enter Room No: ")
mobile_no = input("Enter Mobile No: ")



# Initialize variables
order_items = []
total_price = 0

# Take multiple food orders
while True:
    choice = int(input("\nEnter food item number (0 to finish): "))  
    if choice == 0:  
        break  
    if choice in menu:
        food_item, price = menu[choice]
        order_items.append(food_item)
        total_price += price
    else:
        print("Invalid choice! Try again.")

# Ensure 'ordered_food' is always defined (even if no item is ordered)
ordered_food = ", ".join(order_items) if order_items else "No items ordered"

# Insert into database
cursor.execute("INSERT INTO Orders (student_id, name, room_no, mobile_no, food_item, total_price) VALUES (%s, %s, %s, %s, %s, %s)",
               (student_id, name, room_no, mobile_no, ordered_food, total_price))
c.commit()

print(f"\n✅ Order placed successfully! Total Bill: ₹{total_price}")

cursor.close()
c.close()

input("\nPress Enter to exit...")



