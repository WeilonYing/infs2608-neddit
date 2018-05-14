from datetime import datetime
from .models import Comment, Post, Subneddit


def create_post(
    subneddit, title, author, content="", file=None, isTextPost=True, submitDate=datetime.now()):
    """
    Create and save a post to database

    @param subneddit: string, subneddit code
    @param title: string, post title
    @param author: User model object
    @param content: string, optional, post contents
    @param file: File, optional
    @param isTextPost: bool, optional
    @param submitDate: datetime, optional
    @return: whether post creation was successful
    @rtype: bool
    """
    try:
        subneddit_fkey = Subneddit.objects.get(id=subneddit)
        p = Post(
            subneddit=subneddit_fkey,
            title=title,
            content=content,
            author=author,
            notefile=file,
            isTextPost=isTextPost,
            submitDate=submitDate)
        p.save()
        return True
    except Exception as e:
        print(e)
        return False

def recursive_get_child_comments(parentcomment):
    comment_tree = []
    for c in Comment.objects.filter(parentComment=parentcomment):
        comment_tree.append({
            'comment': c,
            'children': recursive_get_child_comments(c)
        })

    return comment_tree

def get_comments(post):
    # first, get top level comments, then recursively get its children
    comment_tree = []
    for c in Comment.objects.filter(parentComment=None, post=post):
        comment_tree.append({
            'comment': c,
            'children': recursive_get_child_comments(c)
        })

    return comment_tree
