# DB 설정 관련
SQLALCHEMY_DATABASE_URI = 'postgresql://root:1234@3.36.154.16:5432/rulb'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# EMAIL 발송관련
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USERNAME = 'rulb.manager@gmail.com'
MAIL_PASSWORD = 'rulbrulb12'
MAIL_USE_TLS = False
MAIL_USE_SSL = True