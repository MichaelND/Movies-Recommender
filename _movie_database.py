class _movie_database():

  def __init__(self):
    self.movies = {}
    self.users = {}
    self.ratings = {}
    self.images = {}
    self.mid = 0
    self.uid = 0

  def load_movies(self, movie_file):
    self.movies = {}
    for m in open(movie_file):
      mid = int(m.split("::")[0])

      #update mid
      if mid > self.mid:
        self.mid = mid

      values = m.split("::")[1:]
      values[-1] = values[-1].strip('\n')

      movie = {}
      movie['title']    = values[0]
      movie['genres']   = values[1]
      self.movies[mid]  = movie

  def get_movie(self, mid):
    return self.movies.get(mid)

  def get_movies(self):
    midlist = []
    for m in self.movies:
      midlist.append(m)
    return midlist

  def set_movie(self, mid, data):
    mid = int(mid)
    if self.movies.get(mid) is None:
      self.movies[mid] = {}

    self.movies[mid]['title'] = data['title']
    self.movies[mid]['genres'] = data['genres']

  def delete_movie(self, mid):
    self.movies.pop(mid, None)

  def load_users(self, users_file):
    self.users = {}
    for u in open(users_file): 
      uid = int(u.split("::")[0])

      #update uid
      if uid > self.uid:
        self.uid = uid

      values = u.split("::")[1:]
      values[-1] = values[-1].strip('\n')

      user = {}
      user['gender']     = values[0]
      user['age']        = int(values[1])
      user['occupation'] = int(values[2])
      user['zipcode']    = values[3]
      self.users[uid] = user

  def get_user(self, uid):
    return self.users.get(uid)

  def get_users(self):
    userlist = []
    for m in self.users:
      userlist.append(m)
    return userlist

  def set_user(self, uid, data):
    uid = int(uid)
    if self.users.get(uid) is None:
      self.users[uid] = {}

    self.users[uid]['gender']     = data['gender']
    self.users[uid]['age']        = data['age']
    self.users[uid]['occupation'] = data['occupation']
    self.users[uid]['zipcode']    = data['zipcode']

  def delete_user(self, uid):
    self.users.pop(uid, None)

  def load_ratings(self, ratings_file):
    ratings_collection = open(ratings_file)
    for r in ratings_collection:
      uid     =int(r.split("::")[0])
      mid     = int(r.split("::")[1])
      rating  = int(r.split("::")[2])
      if mid not in self.ratings:
        self.ratings[mid] = {}
      self.ratings[mid][uid] = rating

  def get_rating(self, mid):
    if mid not in self.ratings:
      return 0

    average = 0
    for rating in self.ratings[mid]:
      average = average + self.ratings[mid][rating]

    average = average / float(len(self.ratings[mid]))

    return average

  def get_highest_rated_movie(self):
    highest = {}
    for mid in self.movies.keys():
      r = self.get_rating(mid)
      highest[mid] = r
    maxrating = max(highest, key=highest.get)
    return maxrating

  def set_user_movie_rating(self, uid, mid, rating):
    if self.get_movie(mid) == None or self.get_user(uid) == None:
      return

    if mid not in self.ratings:
      self.ratings[mid] = {}
    self.ratings[mid][uid] = rating

  def get_highest_rated_unvoted_movie(self, uid):
    highest = {}

    for mid in self.ratings.keys():
      if uid not in self.ratings[mid]:
        r = self.get_rating(mid)
        highest[mid] = r
    maxrating = max(highest.values())
    maxmid = [k for k, v in highest.items() if v == maxrating]
    maxmid = sorted(maxmid)
    return maxmid[0]

  def get_user_movie_rating(self, uid, mid):
    if mid not in self.ratings or uid not in self.ratings[mid]:
      return None
    return self.ratings[mid][uid]

  def delete_all_ratings(self):
    self.ratings = {}

  def get_id(self, value):
    if value == "mid":
      self.mid += 1
      return self.mid
    elif value == "uid":
      self.uid += 1
      return self.uid

  def load_images(self, images_file):
    self.images = {}
    for images in open(images_file):
      mid = int(images.split("::")[0])
      self.images[mid] = images.split("::")[2].strip('\n')

  def get_image(self, mid):
    return self.images.get(mid)

if __name__ == "__main__":
 mdb = _movie_database()

 #### MOVIES ########
 mdb.load_users('ml-1m/users.dat')
 mdb.load_movies('ml-1m/movies.dat')
 mdb.load_ratings('ml-1m/ratings.dat')
 mdb.load_images('ml-1m/images.dat')

