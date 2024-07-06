from flask import Flask, request, jsonify
from pymongo import MongoClient, ASCENDING, DESCENDING

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client.names_db
names_collection = db.names

# Get all the names in alphabetical order
@app.route('/get_names', methods=['GET'])
def get_names():
    sort_order = request.args.get('sort', 'asc')
    sort_criteria = ASCENDING if sort_order == 'asc' else DESCENDING
    names_cursor = names_collection.find().sort("first_name", sort_criteria)
    names = [{"first_name": name["first_name"]} for name in names_cursor]
    return jsonify(names)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
