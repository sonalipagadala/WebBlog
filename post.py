import uuid

from src.common.database import Database
import datetime

class Post(object):
    def __init__(self,title,content,author,blog_id,created_date=datetime.datetime.utcnow(),_id=None):  #Constructor
        self.title=title
        self.content=content
        self.author=author
        self.created_date=created_date
        self.blog_id=blog_id
        self._id=uuid.uuid4().hex if _id is None else _id
    def save_to_mongo(self):
        Database.insert(collection="posts",data=self.json())


    def json(self):
        return {
            '_id':self._id,
        'title':self.title,
        'content':self.content,
        'author':self.author,
        'blog_id':self.blog_id,
        'created_date':self.created_date
        }


    @staticmethod
    def from_blog(id):
            return [post for post in Database.find(collection='posts',query={'blog_id':id})]

    @classmethod
    def from_mongo(cls,id):
        post_data=Database.find_one(collection="posts",query={'_id':id})
        return cls(**post_data)
