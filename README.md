# bookrestplus


APIs - Requests and Responses

Request Method : GET (Search Fields - Author Name)
Url - http://127.0.0.1:5000/booklist (Complete List of Books)
Url - http://127.0.0.1:5000/book/<id> (Particular Book)
For search:
Url - http://127.0.0.1:5000/booklist/<searchkeyword>
Response - status 200 ok

Request Method : POST
Url - http://127.0.0.1:5000/addbook
Body - {
    “bookname”:”Harry Potter”,
    “author”:”J K Rowling”
    }
Response - status 200 book added successfully ok



Request Method : PUT
Url - http://127.0.0.1:5000/update/<id>
Body - {
    “bookname”:”Harry Potter”,
    “author”:”J K Rowling”
    }
Response - status 200 Updated successfully



Request Method : DELETE
Url -http://127.0.0.1:5000/delete/<id>
Response - status 200 deleted successfully
