import random
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb://test:sparta@ac-3zlcrwk-shard-00-00.v9nxihz.mongodb.net:27017,ac-3zlcrwk-shard-00-01.v9nxihz.mongodb.net:27017,ac-3zlcrwk-shard-00-02.v9nxihz.mongodb.net:27017/?ssl=true&replicaSet=atlas-106koo-shard-0&authSource=admin&retryWrites=true&w=majority', tlsCAFile=ca)
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/rsp", methods=["POST"])
def bucket_post():
    bucket_receive = request.form['bucket_give']
    # 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
    bucket_list = list(db.bucket.find({}, {'_id': False}))
    count = len(bucket_list)+1

    doc = {'num': count,'bucket': bucket_receive, 'done': 0}
    db.bucket.insert_one(doc)
    return jsonify({'msg': '등록 완료!'})

@app.route("/bucket/done", methods=["POST"])
def bucket_done():
    num_receive = request.form['num_give'] #문자열로 바뀌어서, 밑에 숫자로 바꿈
    db.bucket.update_one({'num': int(num_receive)}, {'$set': {'done': 1}})
    return jsonify({'msg': '버킷 완료!'})

@app.route("/bucket/undone", methods=["POST"])
def bucket_undone():
    num_receive = request.form['num_give'] #문자열로 바뀌어서, 밑에 숫자로 바꿈
    db.bucket.update_one({'num': int(num_receive)}, {'$set': {'done': 0}})
    return jsonify({'msg': '실행 취소!'})


@app.route("/rsp", methods=["GET"])
def rsp_get():
    rsp_list = list(db.rsp_user.find({}, {'_id': False}))

    return jsonify({'rsp': rsp_list})

@app.route("/rsp/random", methods=["GET"])
def rsp_get_rand():
    rsp_list = list(db.rsp_com.find({}, {'_id': False}))
    rsp_ran_list = random.choice(rsp_list)
    return jsonify({'rsp_rand': rsp_ran_list})

@app.route("/bucket/delete", methods=["POST"])
def bucket_delete():
    num_receive = request.form['num_give']
    db.bucket.delete_one({'num': int(num_receive)})
    return jsonify({'msg': "삭제 완료"})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
