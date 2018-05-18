class BaseConfig(object):
    """ 配置基类 """
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '\xd6+@+\xc6\x03\xaa\r>o>c\xb3\x1f2z\x9c;\x8f\xbaXoo\xc9'
    INDEX_PER_PAGE = 9
    ADMIN_PER_PAGE = 15


class DevelopmentConfig(BaseConfig):
    """ 开发环境配置 """
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root@localhost:3306/jobplus?charset=utf8'
    HOSTNAME = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'jobplus'
    USERNAME = 'root'
    PASSWORD = ' '

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8mb4".format(username=USERNAME,
                                                                                               password=PASSWORD,
                                                                                               host=HOSTNAME, port=PORT,
                                                                                               db=DATABASE)


class ProductionConfig(BaseConfig):
    """ 生产环境配置 """
    pass


class TestingConfig(BaseConfig):
    """ 测试环境配置 """
    pass


configs = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}