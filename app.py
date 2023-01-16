from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.2qwfec3.mongodb.net/Cluster0?retryWrites=true&w=majority')
# client = MongoClient("mongodb+srv://HANGHAE99_CHAPTER1_9TEAM:sparta@cluster0.\
# fc6zoao.mongodb.net/?retryWrites=true&w=majority")
db = client.sparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/rsp", methods=["POST"])
def rsp():
    # 이게 버튼 눌렀을 때 일어나야 되는 일

    # 유저가 낸 것 user_give로 받아오기
    user_receive = request.form['user_give']

    # 컴퓨터가 낸 것 com_give로 받아오기
    com_receive = request.form['com_give']

    # 결과 result_give로 받아오기
    result_receive = request.form['result_give']


    # 히스토리 조회부분
    history_list = list(db.rsptest.find({}, {'_id': False}))
    count = len(history_list) + 1

    doc = {
        # 몇회차인지
        'num': count,

        # 유저가 낸 것
        'user': user_receive,

        # 컴퓨터가 낸 것
        'com': com_receive,

        # 결과
        'result': result_receive
    }

    # 데이터를 rsptest db에 삽입
    db.rsptest.insert_one(doc)





    return jsonify({'msg':'처음 조회'})


@app.route("/rsp/history", methods=["GET"])
def history():
    history_list = list(db.rsptest.find({}, {'_id': False}))
    return jsonify({'history': history_list})





if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)
