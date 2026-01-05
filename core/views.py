#core/views.py
from flask import render_template,url_for,flash,redirect,Blueprint
from Carblog import db
from Carblog.models import User,BlogPost
from flask import render_template,request,Blueprint

core = Blueprint('core',__name__)

@core.route('/')
def index():
    page = request.args.get('page',1,type=int)
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page,per_page=5)
    return render_template('index.html',blog_posts=blog_posts)


@core.route('/info')
def info():
    return render_template('info.html')

