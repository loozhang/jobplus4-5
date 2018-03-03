#coding:utf-8
from jobplus.models import db,User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError, TextAreaField, IntegerField,SelectField
from wtforms.validators import Length, Email, EqualTo, Required, URL, NumberRange,DataRequired
class LoginForm(FlaskForm):
    email = StringField("邮箱",validators=[Required(),Email()])
    password = PasswordField("密码",validators=[Required(),Length(6,24)])
    remember_me = BooleanField("记住我")
    submit = SubmitField("提交")
    def validata_email(self,field):
        if field.data and not User.query.filter_by(email=field.data).first():
            raise ValidationError('该邮箱未注册')
    def validate_password(self, field):
        user = User.query.filter_by(email=self.email.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('密码错误')



class RegisterForm(FlaskForm):
    username = StringField('用户名', validators=[Required(), Length(3, 24)])
    email = StringField('邮箱', validators=[Required(), Email()])
    password = PasswordField('密码', validators=[Required(), Length(6, 24)])
    repeat_password = PasswordField('重复密码', validators=[Required(), EqualTo('password')])
    submit = SubmitField('提交') 

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已经存在')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已经存在')


    def create_user(self):
        user = User(username=self.username.data,email=self.email.data,password=self.password.data)
        db.session.add(user)
        db.session.commit()
        return user
    def test(self):
        print("++++++++++")
class CompanyRegisterForm(RegisterForm):
    username = StringField('公司名', validators=[Required(), Length(3, 24)])
    def create_user(self):
        user = User(username=self.username.data,email=self.email.data,password=self.password.data)
        user.is_HR
        db.session.add(user)
        db.session.commit()
        return user

class VisterInfo(FlaskForm):
    username = StringField('姓名', validators=[DataRequired(message=""),Required(), Length(3, 24)])
    gender = SelectField('性别',choices=[('10','男'),('20','女')])
    phone = StringField('手机号码', validators=[DataRequired(),Length(11, 11, )])
    college = StringField('毕业院校', validators=[DataRequired(message='必须填写'),Length(2, 24,)])
    education = SelectField('学厉', choices=[
        ('1', '大专'),
        ('2', '本科'),
        ('3', '研究生'),
        ('4', '博士')
        ])
    major = StringField('专业', validators=[DataRequired(message=''),Length(3, 24, message='')])
    service_year = StringField('工作经验', validators=[DataRequired(),Length(1,256)])
    submit = SubmitField('点击更新')
