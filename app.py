import os 

from flask import Flask, redirect, render_template #, Blueprint
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

#@ Nitinkumar
#In the README.txt, this project includes the artifacts for the 2 tasks: 
# blueprint = Blueprint('api',__name__, url_prefix='/eb')
# api = Api(blueprint) #,doc=False
api = Api(app) #,doc=False
PREFIX = "/eb"

# app.register_blueprint(blueprint)


# @app.before_first_request
# def create_tables():
#     db.create_all()

# jwt = JWT(app, authenticate, identity)  # /auth

@app.route(PREFIX+'/all/topics')
def topics():
    return redirect(PREFIX+'/class/topic', code=302)

# @app.errorhandler(404)
# def page_not_found(e):
#     # note that we set the 404 status explicitly
#     return render_template('404.html'), 404

api.add_resource(Class, PREFIX+'/class/<string:name>')
api.add_resource(Topic, PREFIX+'/topic/<int:_id>')
api.add_resource(Title, PREFIX+'/title/<string:title>')
api.add_resource(PageNotFound, PREFIX+'/<path:path>')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
