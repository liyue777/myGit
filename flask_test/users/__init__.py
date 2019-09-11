# 作者：李跃
from flask import Blueprint

users_blue = Blueprint("users", __name__)
from users import views
