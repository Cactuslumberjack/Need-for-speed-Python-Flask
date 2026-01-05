
from flask import Blueprint, request, jsonify, abort
from flask_login import current_user, login_required
from Carblog import db
from Carblog.models import BlogPost

blog_posts_api = Blueprint('blog_posts_api', __name__)

@blog_posts_api.route('/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    return jsonify({
        'id': post.id,
        'title': post.title,
        'post_image': post.post_image,
        'text': post.text,
        'date': post.date.isoformat(),
        'user_id': post.user_id})

@blog_posts_api.route('/<int:post_id>', methods=['PUT'])
@login_required
def update_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    data = request.get_json()
    post.title = data.get('title', post.title)
    post.post_image = data.get('post_image', post.post_image)
    post.text = data.get('text', post.text)
    db.session.commit()
    return jsonify({'message': 'Post updated successfully'})
