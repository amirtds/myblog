from flask import Blueprint, render_template
import os
import markdown

bp = Blueprint('main', __name__)

def load_posts():
    posts = []
    posts_dir = os.path.join(os.path.dirname(__file__), '..', 'posts')
    for filename in os.listdir(posts_dir):
        if filename.endswith('.md'):
            with open(os.path.join(posts_dir, filename), 'r') as f:
                content = f.read()
                html_content = markdown.markdown(content)
                title_line = content.split('\n', 1)[0]
                title = title_line.replace('# ', '').strip()
                post = {
                    'title': title,
                    'content': html_content,
                    'url': filename.replace('.md', '')
                }
                posts.append(post)
    return posts

@bp.route('/')
def index():
    posts = load_posts()
    return render_template('index.html', posts=posts)

@bp.route('/post/<post_url>')
def post(post_url):
    posts = load_posts()
    post = next((post for post in posts if post['url'] == post_url), None)
    if post:
        return render_template('post.html', post=post)
    else:
        return "Post not found", 404
