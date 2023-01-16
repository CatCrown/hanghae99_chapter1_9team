from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

from pymongo import MongoClient
<<<<<<< HEAD
client = MongoClient('mongodb+srv://test:sparta@cluster0.2qwfec3.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

=======
client = MongoClient('mongodb+srv://HANGHAE99_CHAPTER1_9TEAM:sparta@cluster0.fc6zoao.mongodb.net/?retryWrites=true&w=majority')
# client = MongoClient("mongodb+srv://HANGHAE99_CHAPTER1_9TEAM:sparta@cluster0.\
# fc6zoao.mongodb.net/?retryWrites=true&w=majority")
db = client.sparta
>>>>>>> fe60dd022fa0d4684fb95d5317c68292b6a44dd0

@app.route('/')
def home():
   return render_template('index.html')

<<<<<<< HEAD
=======
<<<<<<< HEAD
# log값 받기 (win_give는 이긴 횟수, result_give는 승,무,패 구별하는 변수
# result_give가 1은 비긴 것 2는 이긴 것 3은 진 것
@app.route("/rsp_log", methods=["POST"])
def result_post():
    win_receive = request.form['win_give']
    result_receive = request.form['result_give']
    msg=''
    if result_receive == 1:
          msg = '비겼다'


   elif result_receive == 2:
                              msg = '이겼다'

        elif result_reveive == 3:
            msg = '졌다'
    doc = {'win': win_receive,'msg': msg}
    db.winner.insert_one(doc)
    return jsonify({'msg': '등록 완료!'})

#db(rsp_user)에서 image와 넘버 번호 리스트를 가져온다
@app.route("/rsp", methods=["GET"])
def rsp_get():
    rsp_list = list(db.rsp_user.find({}, {'_id': False}))
=======
@app.route("/rsp", methods=["POST"])
def rsp():
    # 이게 버튼 눌렀을 때 일어나야 되는 일
>>>>>>> fe60dd022fa0d4684fb95d5317c68292b6a44dd0

@app.route("/show", methods=["GET"])
def result_show():

    history_list = list(db.history.find({}, {'_id': False}))
    print(history_list)
    return jsonify({'abc': history_list})


@app.route("/rsp/delete", methods=["GET"])
def delete():
    # 기록 조회 부분
    history_list = list(db.rsptest.find({}, {'_id': False}))

    # db.rsptest.deleteMany({})
    db.rsptest.drop()

    return jsonify({'history': history_list})
<<<<<<< HEAD


# log값 받기 (win_give는 이긴 횟수, result_give는 승,무,패 구별하는 변수
# result_give가 1은 비긴 것 2는 이긴 것 3은 진 것
@app.route("/rsp_log", methods=["POST"])
def result_post():
    win_receive = request.form['win_give']
    result_receive = request.form['result_give']
    msg=''

    if result_receive == 1:
        msg = '비겼다'

    elif result_receive == 2:
        msg = '이겼다'

    elif result_receive == 3:
        msg = '졌다'


    doc = {'win': win_receive,'msg': msg}
    db.winner.insert_one(doc)
    return jsonify({'msg': '등록 완료!'})


#db(rsp_user)에서 image와 넘버 번호 리스트를 가져온다
@app.route("/rsp", methods=["GET"])
def rsp_get():
    rsp_list = list(db.rsp_user.find({}, {'_id': False}))


=======
>>>>>>> a8139690e688017015221f8d02e8acd756be3a71


<<<<<<< HEAD
>>>>>>> fe60dd022fa0d4684fb95d5317c68292b6a44dd0
#db(rsp_com)에서 image와 넘버 번호 리스트를 가져오고 랜덤으로 하나만 가져오기
@app.route("/rsp/random", methods=["GET"])
def rsp_get_rand():
    rsp_list = list(db.rsp_com.find({}, {'_id': False}))
    rsp_ran_list = random.choice(rsp_list)
    return jsonify({'rsp_rand': rsp_ran_list})

<<<<<<< HEAD
=======
=======


>>>>>>> a8139690e688017015221f8d02e8acd756be3a71
>>>>>>> fe60dd022fa0d4684fb95d5317c68292b6a44dd0

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)