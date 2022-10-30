from flask import Blueprint, jsonify
books_bp = Blueprint("hello_world", __name__)

# @hello_world_bp.route("/hello-world", methods=["GET"])
# def say_hello_world():
#     my_beautiful_response_body = "Hello, World!"
#     return my_beautiful_response_body

# @hello_world_bp.route("/hello/JSON", methods=["GET"])
# def say_hello_json():
#     return {
#         "name": "Ada Lovelace",
#         "message": "Hello!",
#         "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
#     }

# @hello_world_bp.route("/broken-endpoint-with-broken-server-code")
# def broken_endpoint():
#     response_body = {
#         "name": "Ada Lovelace",
#         "message": "Hello!",
#         "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
#     }
#     new_hobby = "Surfing"
    
#     response_body["hobbies"].append(new_hobby)
    
#     return response_body

class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description 

books = [ 
    Book(1, "Harry Potter 1", "Harry Potter part 1"),
    Book(2, "Harry Potter 2", "Harry Potter part 2"),
    Book(3, "Harry Potter 3", "Harry Potter part 3")

    ]


@books_bp.route("/books/<book_id>", methods = ["GET"])
def get_all_books(book_id):
    book_id = int(book_id)
    books_response = []
    for book in books:
        if book.id == book_id:
            books_response.append({
                "id": book.id,
                "title": book.title,
                "description": book.description
            })
    
    return jsonify(books_response)


    

