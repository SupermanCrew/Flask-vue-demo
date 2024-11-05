from models import *
from flask import Blueprint,jsonify,request,render_template

books_bp = Blueprint('book', __name__)


def paginate_list(data, page, per_page):
    start = (page - 1) * per_page
    end = start + per_page
    paginated_data = data[start:end]
    return paginated_data


@books_bp.route('/', methods=['GET'])
def get_all_books():
    # 处理获取图书的逻辑
    page_obj_zs = Book.query.count()
    book_list = Book.query.all()
    result = []
    # 获取搜索关键字
    per_page = request.args.get('pageSize', default=10, type=int)
    page = request.args.get('pageNum', default=1, type=int)
    search_query = request.args.get('title')

    # 查询图书数据并进行过滤
    if search_query:
        book_list = Book.query.filter(Book.title.ilike(f'%{search_query}%')).all()
        page_obj_zs = Book.query.filter(Book.title.ilike(f'%{search_query}%')).count()

    # 这种根据对象再进行过滤的方法 flask 不适合 django 和 fastapi 可以
    # # 计算起始索引和结束索引
    # start_index = (page - 1) * per_page
    # # 查询数据库获取分页数据
    # authors = Publisher.query.offset(start_index).limit(per_page).all()

    # 通过函数对 List 过滤
    books = paginate_list(book_list, page, per_page)

    for book in books:
        book_dict = {}
        authors = book.authors
        author_names = [author.name for author in authors]
        book_dict['id']=book.id
        book_dict['title']=book.title
        book_dict['img_url']=book.img_url
        book_dict['publisher']=book.publisher.name
        book_dict['authors']=author_names
        result.append(book_dict)
    data = {'code': 200, 'zs': page_obj_zs, 'data': result}
    return jsonify(data)


@books_bp.route('/', methods=['POST'])
def add_book():
    # 处理添加图书的逻辑
    data = request.json
    publisher_id = data['publishs_id']
    author_ids = data['authors_id']
    publisher = Publisher.query.get(publisher_id)
    authors = Author.query.filter(Author.id.in_(author_ids)).all()
    book = Book(title=data['title'],img_url=data['img_url'], publisher=publisher)
    book.authors = authors
    db.session.add(book)
    db.session.commit()
    return jsonify({'code': 200, 'data': '增加成功'})


@books_bp.route('/<book_id>/', methods=['GET'])
def get_books(book_id):
    # 处理获取图书的逻辑
    result = []
    books = Book.query.filter(Book.id == book_id)
    for book in books:
        book_dict = {}
        authors = book.authors
        author_names = [author.name for author in authors]
        book_dict['id']=book.id
        book_dict['title']=book.title
        book_dict['title']=book.img_url
        book_dict['publisher']=book.publisher.name
        book_dict['authors']=author_names
        result.append(book_dict)
    print(result)
    data = {'code': 200, 'data': result}
    return jsonify(data)


@books_bp.route('/<book_id>/', methods=['PUT'])
def update_book(book_id):
    # 处理更新图书的逻辑
    book = Book.query.get(book_id)
    data = request.json
    publisher_id = data['publishs_id']
    author_ids = data['authors_id']
    publisher = Publisher.query.get(publisher_id)
    authors = Author.query.filter(Author.id.in_(author_ids)).all()
    book.title = data['title']
    book.img_url = data['img_url']
    book.publisher = publisher
    book.authors = authors
    db.session.commit()
    return jsonify({'code': 200, 'data': '更新成功'})


@books_bp.route('/<book_id>/', methods=['DELETE'])
def delete_book(book_id):
    # 处理删除图书的逻辑
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({'code': 200, 'data': '删除成功'})