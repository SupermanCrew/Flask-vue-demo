# 实例化对象
from flask import  Flask,render_template,request,jsonify
from flask_migrate import Migrate as migrate
from settings import SECRET_KEY
from flask_cors import CORS
# 导入子路由的蓝图
from api.publishers import publishers_bp
from api.authors import authors_bp
from api.books import books_bp
from models import *
import datetime
import jwt
import os

from models import db

app=Flask(__name__,static_folder='upimg')

CORS(app, resources={r"/*": {"origins": "*"}})


class Config(object):
    """配置参数"""
    # sqlalchemy的配置参数
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@127.0.0.1:3306/fkbook"
    # 设置每次请求结束后会自动提交数据库中的改动，一般都设置手动保存
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False
    # 设置sqlalchemy自动更新跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True


# 连接数据库
app.config.from_object(Config)

db.init_app(app)
grate = migrate(app, db)

# 是子路由
app.register_blueprint(books_bp, url_prefix='/ts')
app.register_blueprint(publishers_bp, url_prefix='/cbs')
app.register_blueprint(authors_bp, url_prefix='/zz')


# 前台返回格式
ret = {
    "data": {},
    "meta": {
        "status": 200,
        "message": "注册成功"
    }
}


@app.route('/')
def index():
    return 'Hello B站程序员科科!'


# 上传图片
@app.route("/img_upload/", methods=['POST'])
def img_upload():
    response = {}
    file = request.files.get('file')
    print(file,file.filename)
    # try:
    # 构造图片保存路径 路径为<USER_AVATAR_ROOT + 文件名>
    # USER_AVATAR_ROOT刚刚在settings.py中规定过，需要导入进来
    file_path = os.path.join('./upimg', file.filename)
    with open(file_path, 'wb+') as f:
        f.write(file.read())
        f.close()
    response['file'] = file.filename  # 返回新的文件名
    response['code'] = 0
    response['msg'] = "图片上传成功！"
    return {'code': 200, 'message': '上传成功', 'data': response}


# 注册
@app.route("/register/", methods=['POST'])
def register():
    username = request.json.get("username")
    password = request.json.get("password")
    value = request.json.get("value")
    if value == '1':
        pass
    elif value == '2':
        # print(username, password,"商家")
        # user = Chushou.query.filter(Chushou.username==username, Chushou.password==password).first()
        user = Chushou.query.filter_by(username=username, password=password).first()
        if user:
            ret["meta"]["status"] = 500
            ret["meta"]["message"] = "该用户已注册"
        else:
            chushou = Chushou(username=username, password=password)
            ret["meta"]["status"] = 200
            ret["meta"]["message"] = "注册成功"
            db.session.add(chushou)
            db.session.commit()
        return jsonify(ret)
    else:
        print(username, password, "用户")
        # user = Goumai.query.filter(Goumai.username==username, Goumai.password==password).first()
        user = Goumai.query.filter_by(username=username, password=password).first()
        if user:
            ret["meta"]["status"] = 500
            ret["meta"]["message"] = "该用户已注册"
        else:
            goumai = Goumai(username=username, password=password)
            ret["meta"]["status"] = 200
            ret["meta"]["message"] = "注册成功"
            db.session.add(goumai)
            db.session.commit()
        return jsonify(ret)


# 登录
@app.route("/login/", methods=['POST'])
def login():
    ret = {
        "data": {},
        "meta": {
            "status": 200,
            "message": ""
        }
    }
    try:
        username = request.json["username"]
        password = request.json["password"]
        value = int(request.json["value"])

        if value == 1:
            user = Guanli.query.filter_by(username=username, password=password)
            print(user.first())
            if not user:
                ret["meta"]["status"] = 500
                ret["meta"]["message"] = "用户不存在或密码错误"
                return jsonify(ret)
            elif user and user.first().password:
                dict = {
                    "exp": datetime.datetime.now() + datetime.timedelta(days=1),  # 过期时间
                    "iat": datetime.datetime.now(),  # 开始时间
                    "id": user.first().id,
                    "username": user.first().username,
                }
                token = jwt.encode(dict, SECRET_KEY, algorithm="HS256")
                ret["data"]["token"] = token
                ret["data"]["username"] = user.first().username
                ret["data"]["user_id"] = user.first().id
                # 这里需要根据数据库判断是不是管理员
                ret["data"]["isAdmin"] = 1
                ret["meta"]["status"] = 200
                ret["meta"]["message"] = "登录成功"
                print(ret,type(ret))
                return jsonify(ret)
            else:
                ret["meta"]["status"] = 500
                ret["meta"]["message"] = "用户不存在或密码错误"
                return jsonify(ret)
        elif value ==2:
            user = Chushou.query.filter_by(username=username, password=password)
            if not user:
                ret["meta"]["status"] = 500
                ret["meta"]["message"] = "用户不存在或密码错误"
                return jsonify(ret)
            elif user and user.first().password:
                dict = {
                    "exp": datetime.datetime.now() + datetime.timedelta(days=1),  # 过期时间
                    "iat": datetime.datetime.now(),  # 开始时间
                    "id": user.first().id,
                    "username": user.first().username,
                }
                token = jwt.encode(dict, SECRET_KEY, algorithm="HS256")
                ret["data"]["token"] = token
                ret["data"]["username"] = user.first().username
                ret["data"]["user_id"] = user.first().id
                # 这里需要根据数据库判断是不是管理员
                ret["data"]["isAdmin"] = 2
                ret["meta"]["status"] = 200
                ret["meta"]["message"] = "登录成功"
                print(ret, type(ret))
                return jsonify(ret)
            else:
                ret["meta"]["status"] = 500
                ret["meta"]["message"] = "用户不存在或密码错误"
                return jsonify(ret)
        else:
            user = Goumai.query.filter_by(username=username, password=password)
            # print(user)
            if not user:
                ret["meta"]["status"] = 500
                ret["meta"]["message"] = "用户不存在或密码错误"
                return jsonify(ret)
            elif user and user.first().password:
                dict = {
                    "exp": datetime.datetime.now() + datetime.timedelta(days=1),  # 过期时间
                    "iat": datetime.datetime.now(),  # 开始时间
                    "id": user.first().id,
                    "username": user.first().username,
                }
                token = jwt.encode(dict, SECRET_KEY, algorithm="HS256")
                ret["data"]["token"] = token
                ret["data"]["username"] = user.first().username
                ret["data"]["jianjie"] = user.first().jianjie
                ret["data"]["img_url"] = user.first().img_url
                ret["data"]["user_id"] = user.first().id
                # 这里需要根据数据库判断是不是管理员
                ret["data"]["isAdmin"] = 3
                ret["meta"]["status"] = 200
                ret["meta"]["message"] = "登录成功"
                print(ret, type(ret))
                return jsonify(ret)
            else:
                ret["meta"]["status"] = 500
                ret["meta"]["message"] = "用户不存在或密码错误"
                return jsonify(ret)
    except Exception as error:
        print(error)
        ret["meta"]["status"] = 500
        ret["meta"]["message"] = "用户不存在或密码错误"
        return jsonify(ret)


if __name__=="__main__":
    app.run(host='127.0.0.1', port=8000, debug=False)
