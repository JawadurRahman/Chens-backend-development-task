from pymongo import MongoClient

# Connect to Local MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Create (or connect to) the database
db = client.names_db

# Create (or connect to) the collection
names_collection = db.names

# List of first names to add to the database
first_names = [
    "Alice", "Bob", "Charlie", "David", "Eve", 
    "Frank", "Grace", "Heidi", "Ivan", "Judy"
]

# Insert names into the collection
for name in first_names:
    if not names_collection.find_one({"first_name": name}):
        names_collection.insert_one({"first_name": name})

print("Database initialized with first names.")
