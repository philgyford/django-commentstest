from customcomments.models import CommentWithTitle
from customcomments.forms import CommentFormWithTitle

def get_model():
    return CommentWithTitle

def get_form():
    return CommentFormWithTitle