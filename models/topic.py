from db import db
import sys
import traceback

import xml.etree.ElementTree as ET

try:
    tree = ET.parse("britannica_topics.xml")
    root = tree.getroot()
    data= root.findall('url-publish') # hardcoded according to given xml
    topicid_dict = {}
    urlclass_dict = {}
    urltitle_dict = {}
    for url_publish in data:
        for node in url_publish.getiterator():
            if node.tag=='topicid':
                topicid_dict[int(node.text)] = [url_publish]
            if node.tag == 'urlclass':
                if node.text in urlclass_dict:
                    urlclass_dict[node.text].append(url_publish)
                else:
                    urlclass_dict[node.text] = [url_publish]
            if node.tag == 'urltitle':
                if node.text in urltitle_dict:
                    urltitle_dict[node.text].append(url_publish)
                else:
                    urltitle_dict[node.text] = [url_publish]
except Exception as e:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    err_msg = "\n Exception - %s %s" % (e, traceback.format_exception(exc_type, exc_value, exc_traceback, limit=10))
    print (err_msg)
    sys.exit(0)

class TopicModel(db.Model):
    __tablename__ = 'topics'

    id = db.Column(db.Integer, primary_key=True)
    topicid = db.Column(db.Integer, primary_key=True)
    urltitle = db.Column(db.String(80))
    urlclass = db.Column(db.String(80))

    
    def __init__(self, topicid, urltitle, urlclass):
        self.topicid = topicid
        self.urltitle = urltitle
        self.urlclass = urlclass

    def json(self):
        return {'topicid': self.topicid, 'urltitle': self.urltitle, 'urlclass': self.urlclass}
    
    @classmethod
    def get_json(cls, topic):
        temp_dict = {i.tag:i.text for i in topic}
        topicid, urltitle, urlclass = int(temp_dict["topicid"]),temp_dict["urltitle"],temp_dict["urlclass"]
        topicObj = cls(topicid=topicid, urltitle=urltitle, urlclass=urlclass)
        return topicObj.json()

    @classmethod
    def find_by_topicid(cls, topicid):
        return topicid_dict[topicid] if topicid in topicid_dict else []
        # return cls.query.filter_by(topicid=topicid).first() #retrive data from db table
    
    @classmethod
    def find_by_urltitle(cls, urltitle):
        return urltitle_dict[urltitle] if urltitle in urltitle_dict else []
        # return cls.query.filter_by(urltitle=urltitle).first() #retrive data from db table
    
    @classmethod
    def find_by_urlclass(cls, urlclass):
        return urlclass_dict[urlclass] if urlclass in urlclass_dict else []
        # return cls.query.filter_by(urlclass=urlclass).first() #retrive data from db table
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    
