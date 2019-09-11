# 作者：李跃
from flask import render_template, request
import pymysql
from . import users_blue


@users_blue.route('/users')
def users():
    return 'users'


@users_blue.route('/sign_in', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        uname = request.form.get('uname')
        pwd = request.form.get('pwd')
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='shop', charset='utf8')
        cur = conn.cursor()
        cur.execute("select pwd from user where uname=%s", [uname])
        i = cur.fetchall()
        cur.close()
        conn.close()
        if len(i) != 0:
            if pwd == i[0][0]:
                return render_template('index.html', content={'uname': uname, 'pwd': pwd})
        return render_template('sign_in.html', content='账号密码错误', err='你好')
    return render_template('sign_in.html', err='你好')
