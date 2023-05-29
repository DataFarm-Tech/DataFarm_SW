import pymysql
# Establish the connection to the MySQL server
connection = pymysql.connect(
    host="172.105.191.35",
    user="your_username",
    password="your_password",
    database="datafarm"
)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Prepare the SQL statement to insert data into the table
sql = "INSERT INTO persons (name, age, phone) VALUES (%s, %s, %s)"

# Prompt the user to enter person's details
name = input("Enter name: ")
age = int(input("Enter age: "))
phone = input("Enter phone number: ")

# Execute the SQL statement with the provided values
cursor.execute(sql, (name, age, phone))

# Commit the changes to the database
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
