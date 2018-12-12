from flask_restplus import Resource  # , reqparse
# from flask_restful import Resource #, reqparse
from flask import jsonify
# from flask_jwt import jwt_required
from models.topic import TopicModel


class Topic(Resource):
    '''
    parser = reqparse.RequestParser()
    parser.add_argument('urlclass',
                        type=str,
                        required=True,
                        help="urlclass"
                        )
    parser.add_argument('urltitle',
                        type=str,
                        required=True,
                        help="urltitle"
                        )
    '''
    # @jwt_required()

    def get(self, _id):
        topics = TopicModel.find_by_topicid(_id)
        ret_response = []
        if topics:
            for topic in topics:
                ret_response.append(TopicModel.get_json(topic))
        else:
            ret_response = [{
                "Topic_id": _id,
                "error": "URL Not Found",
                "cause": "topic {} not in database".format(_id)
            }]

        return jsonify(ret_response)

    '''
    def post(self, _id):
        if TopicModel.find_by_topicid(_id):
            return {'message': "An topic with topicid :{} already exists.".format(_id)}, 400

        data = Topic.parser.parse_args()

        topic = TopicModel(topicid=_id, **data)
        # topic = TopicModel(urlclass=data['urlclass'], topicid=_id, urltitle=data['urltitle'])

        try:
            topic.save_to_db()
        except:
            return {"message": "An error occurred inserting the topic."}, 500

        return topic.json(), 201

    def delete(self, _id):
        topic = TopicModel.find_by_topicid(_id)
        if topic:
            topic.delete_from_db()

        return {'message': 'topic deleted'}

    def put(self, _id):
        data = Topic.parser.parse_args()

        topic = TopicModel.find_by_topicid(_id)

        if topic:
            topic.topicid = data['topicid']
            topic.urltitle = data['urltitle']
        else:
            topic = TopicModel(topicid=_id, **data)
            # topic = TopicModel(urlclass=data['urlclass'], topicid=_id, urltitle=data['urltitle'])

        topic.save_to_db()

        return topic.json()
    '''


class Class(Resource):

    def get(self, name):
        topics = TopicModel.find_by_urlclass(name)
        ret_response = []
        if topics:
            for topic in topics:
                ret_response.append(TopicModel.get_json(topic))
        else:
            ret_response = [{
                "URL_class": name,
                "error": "URL Not Found",
                "cause": "URL_class {} not in database".format(name)
            }]

        return jsonify({"url-publish": ret_response})


class Title(Resource):

    def get(self, title):
        topics = TopicModel.find_by_urltitle(title)
        ret_response = []
        if topics:
            for topic in topics:
                ret_response.append(TopicModel.get_json(topic))
        else:
            ret_response = [{
                "Url_title": title,
                "error": "URL Not Found",
                "cause": "Url_title {} not in database".format(title)
            }]

        return jsonify(ret_response)


class PageNotFound(Resource):

    def get(self, path):
        return {"err_message": "Not recognizable Path: '{}', Please, check it!".format(path)}, 404


'''
class TopicList(Resource):

    # @jwt_required()
    def get(self):
        # retrive data from database table
        return {'topics': list(map(lambda x: x.json(), TopicModel.query.all()))}
'''
