from flask import Blueprint,render_template,jsonify
from exts import mail,db
from flask_mail import Message
from flask import request
import string
import random
from models import EmailCaptchaModel
bp = Blueprint("auth",__name__,url_prefix="/auth")

@bp.route("/login")
def login():
    return "login"
@bp.route("/register")
def register():
    return "register"
    # return render_template("regist.html")

@bp.route("/captcha/email")
def get_email_captcha():
    email = request.args.get("email")
    source = string.digits*4
    captcha = random.sample(source,4)
    captcha = "".join(captcha)
    message = Message(subject="知了传课注册验证码", recipients=[email], body=f"您的验证码是:{captcha}")
    mail.send(message)
    email_captcha = EmailCaptchaModel(email=email,captcha=captcha)
    db.session.add(email_captcha)
    db.session.commit()
    return jsonify({"code": 200, "message": "", "data": None})

@bp.route("/mail/test")
def mail_test():
    message = Message(subject="邮箱测试",recipients=["977374881@qq.com"], body="这是一条测试邮件")
    mail.send(message)
    return "邮件发送成功!"
