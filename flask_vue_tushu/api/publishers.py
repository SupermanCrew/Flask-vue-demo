from models import *
from flask import Blueprint,jsonify,request,render_template

publishers_bp = Blueprint('publishers', __name__)

def paginate_list(data, page, per_page):
    start = (page - 1) * per_page
    end = start + per_page
    paginated_data = data[start:end]
    return paginated_data


@publishers_bp.route('/', methods=['GET'])
def get_all_publishers():
    # 处理获取图书的逻辑
    page_obj_zs = Publisher.query.count()
    book_list = Publisher.query.all()
    # 获取搜索关键字
    per_page = request.args.get('pageSize', default=10, type=int)
    page = request.args.get('pageNum', default=1, type=int)
    search_query = request.args.get('name')
    # 查询图书数据并进行过滤
    if search_query:
        book_list = Publisher.query.filter(Publisher.name.ilike(f'%{search_query}%')).all()
        page_obj_zs = Publisher.query.filter(Publisher.name.ilike(f'%{search_query}%')).count()
    # 通过函数对 List 过滤
    books = paginate_list(book_list, page, per_page)

    result = [{'id': author.id, 'name': author.name} for author in books]
    data = {'code': 200, 'zs': page_obj_zs, 'data': result}
    return jsonify(data)

@publishers_bp.route('/', methods=['POST'])
def add_publishers():
    # 处理添加出版社的逻辑
    data = request.json
    author = Publisher(name=data['name'])
    db.session.add(author)
    db.session.commit()
    return jsonify({'code': 200, 'data': '增加成功'})

@publishers_bp.route('/<publish_id>/', methods=['GET'])
def get_publishers(publish_id):
    # 处理获取出版社的逻辑
    author = Publisher.query.get(publish_id)
    result = {'id': author.id, 'name': author.name}
    data = {'code': 200, 'data': result}
    return jsonify(data)

@publishers_bp.route('/<publish_id>/', methods=['PUT'])
def update_publishers(publish_id):
    # 处理更新出版社的逻辑
    author = Publisher.query.get(publish_id)
    if not author:
        return 'Publisher not found', 404

    data = request.json
    author.name = data['name']
    db.session.commit()
    return jsonify({'code': 200, 'data': '更新成功'})

@publishers_bp.route('/<publish_id>/', methods=['DELETE'])
def delete_publishers(publish_id):
    # 处理删除出版社的逻辑
    author = Publisher.query.get(publish_id)
    if not author:
        return 'Publisher not found', 404

    db.session.delete(author)
    db.session.commit()
    return jsonify({'code': 200, 'data': '删除成功'})