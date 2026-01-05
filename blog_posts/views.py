# blog_posts/views.py
from flask import render_template,url_for,flash,request,redirect,Blueprint,abort
from flask_login import current_user,login_required
from Carblog import db
from Carblog.models import BlogPost
from Carblog.blog_posts.forms import BlogPostForm 
from Carblog.blog_posts.picture_handler import add_post_pic 

blog_posts = Blueprint('blog_posts',__name__)

# CREATE

@blog_posts.route('/create',methods=['GET','POST'])
@login_required
def create_post():
    form = BlogPostForm()

    if form.validate_on_submit():
        if form.post_image.data:
            username = current_user.username
            pic_filename = add_post_pic(form.post_image.data, username)
        else: 
            pic_filename = 'default_post.png'

        blog_post = BlogPost(title=form.title.data,text=form.text.data,post_image=pic_filename, 
                             user_id=current_user.id)

        db.session.add(blog_post)
        db.session.commit()
        flash('Blog Post Created', 'success')
        return redirect(url_for('core.index'))
    
    return render_template('create_post.html',form=form)


# BLOG POST VIEW
@blog_posts.route('/<int:blog_post_id>')
def blog_post(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)
    return render_template('blog_post.html',title=blog_post.title,post_image=blog_post.post_image,date=blog_post.date,post=blog_post)


# UPDATE
@blog_posts.route('/<int:blog_post_id>/update',methods=['GET','POST'])
@login_required
def update(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)

    if blog_post.author != current_user:
        abort(403)

    form = BlogPostForm()


    if form.validate_on_submit():
        if form.post_image.data:
            username = current_user.username
            pic_filename = add_post_pic(form.post_image.data,username)  
            blog_post.post_image = pic_filename        

        blog_post.title = form.title.data
        blog_post.text = form.text.data
        blog_post.user_id = current_user.id

        db.session.commit()
        flash('Blog Post Updated', 'success')
        return redirect(url_for('blog_posts.blog_post',blog_post_id=blog_post_id))
    
    elif request.method == "GET":
        form.title.data = blog_post.title
        form.text.data = blog_post.text 

    post_image = url_for('static', filename='post_pics/' + blog_post.post_image)
    return render_template('create_post.html',title='Update',form=form, post_image=post_image)

    



# DELETE
@blog_posts.route('/<int:blog_post_id>/delete',methods=['GET','POST'])
@login_required
def delete_post(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)
    if blog_post.author != current_user:
        abort(403)

    db.session.delete(blog_post)
    db.session.commit()
    flash('Blog Post Deleted', 'success')
    return redirect(url_for('core.index'))

