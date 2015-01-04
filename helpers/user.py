from mongo import *
from bson import ObjectId
import bcrypt, datetime

class User(object):
  def __init__(self, userid=None, username=None):
    if userid:
      self.user = users.find_one({'_id': ObjectId(userid)})
    elif username:
      self.user = users.find_one({'username': username.lower()})

  def get(self, key, default=''):
    return self.user.get(key, default)

  def add(self, key, value):
    self.raw_update({'$addToSet': {key: value}})

  def set(self, key, value):
    self.update({key: value})

  def update(self, d):
    self.raw_update({'$set': d})

  def raw_update(self, d):
    users.update({'_id': self.user['_id']}, d)
    self.user = users.find_one({'_id': self.get('_id')})

  def check(self):
    try:
      return self.user is not None
    except:
      return False

  def login(self, password):
    return bcrypt.hashpw(str(password), str(self.user['password'])) == str(self.user['password'])

  @classmethod
  def create(klass, username, password):
    user = {'username': username}
    salt = bcrypt.gensalt()
    user['password'] = bcrypt.hashpw(str(password), salt)
    user['created_at'] = datetime.datetime.utcnow()
    _id = users.insert(user)
    return User(userid=_id)

  def get_id(self):
    return str(self.user['_id'])

  def is_admin(self):
    return self.get('admin', False)
