"""Creates sample data for the adoption database"""

from models import Pet, db
from app import app

db.drop_all()
db.create_all()

# options to run file:
# ipython: %run seed.py
# python3 seed.py

p1 = Pet(name='Canelo', species='dog', age='2', photo_url='https://chico.ca.us/sites/main/files/imagecache/lightbox/main-images/dog_license.jpg')
p2 = Pet(name='Snap', species='cat', age='7', photo_url='https://images.pexels.com/photos/617278/pexels-photo-617278.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2')
p3 = Pet(name='Carrot', species='porcupine', age='1')

db.session.add_all([p1, p2, p3])
db.session.commit()
