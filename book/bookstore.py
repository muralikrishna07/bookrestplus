from flask import Flask,Blueprint
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify,request
from .extentions import mongo
# from werkzeug.security import generate_password_hash,check_password_hash


# app.secret_key="keykey"
# app.config['MONGO_URI'] = "mongodb://localhost:27017/bookstore"
# mongo = PyMongo(app)

bk = Blueprint('bk',__name__)

@bk.route("/addbook",methods=["POST"])
def add_book():
    _json = request.json
    _bookname = _json['bookname']
    _author = _json['author']

    if _bookname and _author and request.method == 'POST':
        mongo.db.booktable.insert({'bookname':_bookname,'author':_author})
        resp = jsonify("book added successfully"),200
        return resp
    else:
        return not_found()

@bk.route('/booklist',methods=['GET'])
def booklist():
    bookname = request.args.get('bookname')
    author = request.args.get('author')
    if author or bookname:
        output = []
        for q in mongo.db.booktable.find({"$or":[{'bookname':bookname},{'author':author}]}):   
            output.append({'bookname' : q['bookname'], 'author' : q['author']})
        if len(output)!=0 :
            return jsonify({'result' : output})
        else:
            return jsonify({'result' : 'No Results Found'})

    else:
        book = mongo.db.booktable.find()
        resp = dumps(book)
        return resp


@bk.route('/book/<id>',methods=['GET'])
def find_book(id):
    book = mongo.db.booktable.find_one({'_id':ObjectId(id)})
    resp = dumps(book)
    return resp


@bk.route('/update/<id>',methods=['PUT'])
def update(id):
    _id=id
    _json = request.json
    _bookname = _json['bookname']
    _author = _json['author']

    if _bookname and _author and request.method == 'PUT':
        mongo.db.booktable.update_one({'_id': ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)},
                         {'$set': {'bookname': _bookname, 'author': _author}}) 

        resp = jsonify("Updated successfully"),200
        return resp
    else:
        return not_found()

@bk.route('/delete/<id>',methods=['DELETE'])
def delete(id):
    mongo.db.booktable.delete_one({'_id':ObjectId(id)})
    resp = jsonify("deleted successfully"),200
    return resp

@bk.errorhandler(404)
def not_found(error=None):
    message = {
        'status':404,
        'message':'not fount'+request.url
    }
    resp=jsonify(message)
    resp.status_code=200
    return resp

