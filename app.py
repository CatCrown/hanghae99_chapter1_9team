from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
import random
import certifi
ca = certifi.where()


@app.route('/')
def index():
  return render_template('index.html')


from pymongo import MongoClient
client = MongoClient(
    'mongodb+srv://HANGHAE99_CHAPTER1_9TEAM:sparta@cluster0.fc6zoao.mongodb.net/?retryWrites=true&w=majority')

db = client.sparta



#이미지(주소)와 이미지 고유넘버를 한묶음으로 저장
# d = {}
# d['https://ifh.cc/g/mtGs0O.png'] = 1
# d['https://ifh.cc/g/1Y0LPy.png'] = 2
# d['https://ifh.cc/g/Qqw7Qa.png'] = 3
# keys = list(d.keys())
# count = 0;
# for i in range(3):
#   doc = {'num_com': count + 1, 'img_list_com': keys[count]}
#   count = count + 1
#   db.rsp_com.insert_one(doc)
#
#   doc = {'num_user': count + 1, 'img_list_user': keys[count]}
#   count = count + 1
#   db.rsp_user.insert_one(doc)







# log값 받기 (win_give는 이긴 횟수, result_give는 승,무,패 구별하는 변수
# result_give가 1은 비긴 것 2는 이긴 것 3은 진 것
#@app.route("/rsp_log", methods=["POST"])
# def result_post():
#     win_receive = request.form['win_give']
#     result_receive = request.form['result_give']
#     msg = ''
#     if result_receive == 1:
#         msg = '비겼다'
#
#     elif result_receive == 2:
#         msg = '이겼다'
#
#     elif result_receive == 3:
#         msg = '졌다'
#
#     doc = {'win': win_receive, 'msg': msg}
#     db.winner.insert_one(doc)
#     return jsonify({'msg': '등록 완료!'})


# db(rsp_user)에서 image와 넘버 번호 리스트를 가져온다
@app.route("/rsp", methods=["GET"])
def rsp_get():
    rsp_list = list(db.rsp_user.find({}, {'_id': False}))
    return jsonify({'rsp': rsp_list})

# db(rsp_com)에서 image와 넘버 번호 리스트를 가져오고 랜덤으로 하나만 가져오기
@app.route("/rsp/random", methods=["GET"])
def rsp_get_rand():
    rsp_list = list(db.rsp_com.find({}, {'_id': False}))
    rsp_ran_list = random.choice(rsp_list)
    return jsonify({'rsp_rand': rsp_ran_list})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

