import json
from csv import DictReader

with open('../files/users.json', 'r') as j:
    json_load = json.load(j)
    number_of_users = len(json_load)

users = [{"name": user['name'], "gender": user['gender'], "address": user['address'], "age": user['age'], "books": []}
         for user in json_load]

with open('../files/books.csv') as c:
    reader = DictReader(c)
    books = [{"title": row['Title'], "author": row['Author'], "pages": row['Pages'], "genre": row['Genre']} for row in
             reader]

curr_usr = 0
for book in books:
    users[curr_usr]["books"].append(book)
    curr_usr = curr_usr + 1
    if curr_usr >= number_of_users:
        curr_usr = 0

with open('../files/result.json', 'w') as r:
    json.dump(users, r, indent=4)
