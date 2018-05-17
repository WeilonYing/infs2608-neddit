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
    @return: Post, if creation successful
    @rtype: Post
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
        return p
    except Exception as e:
        print(e)
        return None


def create_comment(
    post, parentComment, content, author, submitDate=datetime.now()):
    """
    Create and save a comment to database.

    @param post: Post model object
    @param parentComment: Comment model object, the comment's parent if exists. Nullable.
    @param content: string, contents of comment
    @param author: User model object, the user who wrote the comment
    @param submitDate: datetime, optional
    @return: Comment, if creation successful
    @rtype: Comment
    """
    try:
        c = Comment(
            post=post,
            parentComment=parentComment,
            content=content,
            submitDate=submitDate,
            author=author)
        c.save()
        print(c)
        return c
    except Exception as e:
        print(e)
        return None


def recursive_get_child_comments(parentcomment):
    """Recursively get the children of a given comment"""
    comment_tree = []
    for c in Comment.objects.filter(parentComment=parentcomment):
        comment_tree.append({
            'comment': c,
            'children': recursive_get_child_comments(c)
        })

    return comment_tree


def get_comments(post):
    """Get a list of comments of a given post"""
    # first, get top level comments, then recursively get its children
    comment_tree = []
    for c in Comment.objects.filter(parentComment=None, post=post):
        comment_tree.append({
            'comment': c,
            'children': recursive_get_child_comments(c)
        })

    return comment_tree
