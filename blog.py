import string
import uuid
import datetime
from post import Post
from src.common.database import Database

class Blog(object):
    def __init__(self,author,title,author_id,description,_id=None):
        self.author=author
        self.title=title
        self.description=description
        self._id=uuid.uuid4().hex if _id is None else _id
        self.author_id=author_id

    def new_post(self,title,content,date=datetime.datetime.utcnow()):#Should be called by a blog object(Hence,no need to specify the ID)
        post=Post( blog_id=self._id,
                   created_date=date
                   ,title=title,content=content,author=self.author)
        post.save_to_mongo()

    def get_posts(self):
        return Post.from_blog(self._id)

    def save_to_mongo(self):
        Database.insert(collection="blogs",data=self.json())

    def json(self):
        return {
            'author':self.author,
            'title': self.title,
            'description':self.description,
            'author_id':self.author_id,
            '_id':self._id

        }
    @classmethod
    def from_mongo(cls,id):                            #Finds information about a specific blog with an ID
        blog_data=Database.find_one(collection="blogs",query={'_id':id})
        return cls(**blog_data)


    @classmethod
    def find_by_author_id(cls,author_id):                  #Finds information about all the blogs with the corresponding author_id
        blogs=Database.find("blogs",{'author_id':author_id})
        return [cls(**blog) for blog in blogs]




