import os 

from flask import Flask, redirect, render_template, jsonify#, Blueprint
# from flask_restful import Api
from flask_restplus import Api
from flask_jwt import JWT

# from security import authenticate, identity
# from resources.user import UserRegister
from resources.topic import Topic, Class, Title, PageNotFound
from db import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'Nitinkumar'

app.__author__ = "Nitinkumar Patel"
app.__copyright__ = "Copyright 2018, The Nitin_must Project"
app.__credits__ = ["Nitin Patel"]
app.__license__ = "Must"
app.__version__ = "1.0.1"
app.__maintainer__ = "Nitin Patel"
app.__email__ = "er.nitinpatel914@gmail.com"
app.__status__ = "Production"

#@ Nitinkumar
#In the README.txt, this project includes the artifacts for the 2 tasks: 
# blueprint = Blueprint('api',__name__, url_prefix='/eb')
# api = Api(blueprint) #,doc=False
api = Api(app) #,doc=False
PREFIX = "/eb"
ENV = "QA"

# app.register_blueprint(blueprint)


# @app.before_first_request
# def create_tables():
#     db.create_all()

# jwt = JWT(app, authenticate, identity)  # /auth

@app.route(PREFIX+'/all/topics')
def topics():
    return redirect(PREFIX+'/class/topic', code=302)

@app.route(PREFIX+'/contact_author')
def author():
    return jsonify({"Author":app.__author__, "E-Mail":app.__email__}), 200
# @app.errorhandler(404)
# def page_not_found(e):
#     # note that we set the 404 status explicitly
#     return render_template('404.html'), 404

api.add_resource(Class, PREFIX+'/class/<string:name>')
api.add_resource(Topic, PREFIX+'/topic/<int:_id>')
api.add_resource(Title, PREFIX+'/title/<string:title>') # extra api /eb/title/<urltitle>
api.add_resource(PageNotFound, PREFIX+'/<path:path>')



if __name__ == '__main__':
    from db import db
    db.init_app(app)
    print (app.__author__)
    app.run(port=5000, debug=True if ENV=="QA" else False)
