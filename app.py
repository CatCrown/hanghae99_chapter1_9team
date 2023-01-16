import random
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb://test:sparta@ac-3zlcrwk-shard-00-00.v9nxihz.mongodb.net:27017,ac-3zlcrwk-shard-00-01.v9nxihz.mongodb.net:27017,ac-3zlcrwk-shard-00-02.v9nxihz.mongodb.net:27017/?ssl=true&replicaSet=atlas-106koo-shard-0&authSource=admin&retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

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

    return jsonify({'rsp': rsp_list})

#db(rsp_com)에서 image와 넘버 번호 리스트를 가져오고 랜덤으로 하나만 가져오기
@app.route("/rsp/random", methods=["GET"])
def rsp_get_rand():
    rsp_list = list(db.rsp_com.find({}, {'_id': False}))
    rsp_ran_list = random.choice(rsp_list)
    return jsonify({'rsp_rand': rsp_ran_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
