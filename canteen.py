import mysql.connector
import time

# Connect to MySQL
c = mysql.connector.connect(
    host="localhost",
    user="root",
    password="daksh@4321",
    database="canteen"
)
cursor = c.cursor()

while True:
    cursor.execute("SELECT * FROM Orders")
    orders = cursor.fetchall()

    print("\n Pending Orders \n")
    for order in orders:
        print(f"Order ID: {order[0]}, Student: {order[2]}, Room: {order[3]}, Food: {order[5]}, Total: ₹{order[6]}")

    # Option to delete completed orders
    delete_id = input("\nEnter Order ID to mark as completed (or press Enter to refresh): ")
    if delete_id:
        cursor.execute("DELETE FROM Orders WHERE id = %s", (delete_id,))
        c.commit()
        print("\n Order marked as completed!")

    print("\nRefreshing in 10 seconds...\n")
    time.sleep(10)  # Refresh every 10 seconds

