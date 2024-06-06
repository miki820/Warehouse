import sqlite3

con = sqlite3.connect('warehouse.db')
con.row_factory = sqlite3.Row
cur = con.cursor()

# Script to delete the Product table if it exists and create a new one
cur.executescript("""
DROP TABLE IF EXISTS Product;
CREATE TABLE IF NOT EXISTS Product (
id INTEGER PRIMARY KEY ASC,
name VARCHAR(50) NOT NULL,
description VARCHAR(100) NOT NULL,
price REAL NOT NULL,
amount INTEGER NOT NULL
)""")

# Data to be inserted into the table
products = (
    (None, 'TV', 'Telecommunication medium for transmitting moving images and sound.', 2664.80, 10),
    (None, 'Dishwasher', 'Machine that is used to clean dishware, cookware, and cutlery automatically.', 1399.00, 15),
    (None, 'Washing Machine', 'Home appliance used to wash laundry.', 2500.74, 20),
    (None, 'Computer', 'Electronic device for storing and processing data.', 3999.00, 25),
    (None, 'Camera', 'Device for recording visual images in the form of photographs or video signals.', 2199.00, 30)
)

# Insert multiple rows of data into the Product table
cur.executemany('INSERT INTO Product VALUES(?,?,?,?,?)', products)

con.commit()

con.close()
