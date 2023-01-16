from flask import jsonify, request
from db import db

def option_get():
   user_num = request.args.get('user_num')
   my_place_list = db.place.find({'user_num': int(user_num)}, {'_id': False})
    
def history_post():
  
