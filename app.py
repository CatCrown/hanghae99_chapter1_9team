from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient("mongodb+srv://HANGHAE99_CHAPTER1_9TEAM:sparta@cluster0.fc6zoao.mongodb.net/?retryWrites=true&w=majority")
db = client.sparta

@app.route('/')
def home():
   return render_template('index.html')

<<<<<<< HEAD
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
    # 기록 조회 부분
    history_list = list(db.rsptest.find({}, {'_id': False}))
    return jsonify({'history': history_list})


@app.route("/rsp/delete", methods=["GET"])
def delete():
    # 기록 조회 부분
    history_list = list(db.rsptest.find({}, {'_id': False}))

    # db.rsptest.deleteMany({})
    db.rsptest.drop()

    return jsonify({'history': history_list})
=======
# log값 받기 (win_give는 이긴 횟수, result_give는 승,무,패 구별하는 변수
# result_give가 1은 비긴 것 2는 이긴 것 3은 진 것
@app.route("/rsp_log", methods=["POST"])
def result_post():
    win_receive = request.form['win_give']
    result_receive = request.form['result_give']
    msg=''
    if result_receive == 1:
                            msg = '비겼다'


   else if result_receive == 2:
                              msg = '이겼다'

        else if result_reveive == 3:
            msg = '졌다'
    doc = {'win': win_receive,'msg': msg}
    db.winner.insert_one(doc)
    return jsonify({'msg': '등록 완료!'})

#db(rsp_user)에서 image와 넘버 번호 리스트를 가져온다
@app.route("/rsp", methods=["GET"])
def rsp_get():
    rsp_list = list(db.rsp_user.find({}, {'_id': False}))
>>>>>>> 9ae6eeaf061cb425cd707a507601f4ad1bc80349


<<<<<<< HEAD


=======
#db(rsp_com)에서 image와 넘버 번호 리스트를 가져오고 랜덤으로 하나만 가져오기
@app.route("/rsp/random", methods=["GET"])
def rsp_get_rand():
    rsp_list = list(db.rsp_com.find({}, {'_id': False}))
    rsp_ran_list = random.choice(rsp_list)
    return jsonify({'rsp_rand': rsp_ran_list})

>>>>>>> 9ae6eeaf061cb425cd707a507601f4ad1bc80349

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)
