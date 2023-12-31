import wtforms
from wtforms.validators import Email,Length,EqualTo
from models import UserModel,EmailCaptchaModel
from exts import db
class RegisterForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="邮箱格式错误！")])
    captcha = wtforms.StringField(validators=[Length(min=4,max=4,message="验证码格式错误")])
    username = wtforms.StringField(validators=[Length(min=3,max=20,message="用户名格式错误")])
    password = wtforms.StringField(validators=[Length(min=6,max=20,message="密码格式错误")])
    password_confirm = wtforms.StringField(validators=[EqualTo("password")])

    # 自定义验证
    # 1、验证邮箱是否注册过
    def validata_email(self,field):
        email = field.data
        user = UserModel.querry.filter_by(email=email).first()
        if user:
            raise wtforms.ValidationError(message="该邮箱已被注册")

    # 2、验证码是否正确
    def validata_captcha(self,field):
        captcha = field.data
        email = self.email.data
        captcha_model = EmailCaptchaModel.query.filter_by(email=email,captcha=captcha).first()
        if not captcha_model:
            raise wtforms.ValidationError(message="邮箱或者验证码错误！")
        else:
            db.session.delete(captcha_model)
            db.session.commit()








