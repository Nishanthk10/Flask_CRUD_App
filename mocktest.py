from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import pytest
import app

class Users():
    _id = app.db.Column("id", app.db.Integer, primary_key=True)
    name = app.db.Column(app.db.String(100))
    email = app.db.Column(app.db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email

@pytest.fixture
def flask_app_mock():
    app_mock = Flask(__name__)
    db = SQLAlchemy(app_mock)
    db.init_app(app_mock)
    return app_mock

@pytest.fixture
def mock_users():
    users = Users('Nishanth', 'nishanthsentyar@gmail.com')
    return users

@pytest.fixture
def mock_get_sqlalchemy(mocker):
    mock = mocker.patch("flask_sqlalchemy._QueryProperty.__get__").return_value = mocker.Mock()
    return mock

data = Users.query.all()
print(data)
