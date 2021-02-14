from flask import Flask
from flask_sqlalchemy import SQLAlchemy, Model, BaseQuery


class Singleton(type):
    _instances = dict()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            new_instance = super(Singleton, cls).__call__(*args, **kwargs)
            cls._instances[cls] = new_instance
        return cls._instances[cls]


class SingletonSQLAlchemy(SQLAlchemy, metaclass=Singleton):
    def __init__(
            self, app=None, use_native_unicode=True, session_options=None, metadata=None, query_class=BaseQuery,
            model_class=Model, engine_options=None):
        super().__init__(app=app, use_native_unicode=use_native_unicode, session_options=session_options,
                         metadata=metadata, query_class=query_class, model_class=model_class, engine_options=engine_options)


def config_db(app: Flask, db: SQLAlchemy = SingletonSQLAlchemy()):
    db.init_app(app)
    app.db = db
