# 数据库配置信息
HOSTNAME = "127.0.0.1"
PORT = 3306
USERNAME =  "root"
PASSWORD = "123456"
DATABASE = "zhiliaooa"
DB_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"
SQLALCHEMY_DATABASE_URI = DB_URI

#qspyegmaonwhbceh
# 邮箱配置
MAIL_SERVER = "smtp.qq.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "976631565@qq.com"
MAIL_PASSWORD = "qspyegmaonwhbceh"
MAIL_DEFAULT_SENDER = "976631565@qq.com"
