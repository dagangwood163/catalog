# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import City, Base, Attraction, User

from datetime import datetime


engine = create_engine('sqlite:///attractionscatalog')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create a dummy user based on Udacity's lecture code example
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com")
session.add(User1)
session.commit()

# Add four major cites in Texas
austin = City(name="Austin")
session.add(austin)
session.commit()

dallas = City(name="Dallas")
session.add(dallas)
session.commit()

houston = City(name="Houston")
session.add(houston)
session.commit()

sanantonio = City(name="San Antonio")
session.add(sanantonio)
session.commit()

# Add an attraction for each city
attractionItem1 = Attraction(user_id=1, name="State Capitol", description="This is a beautiful building that shows off many of the natural resources are so prevalent in Texas",
                             city=austin,
                             created_at=datetime(2017, 8, 5, 0, 0, 0))
session.add(attractionItem1)
session.commit()

attractionItem2 = Attraction(user_id=1, name="Dallas Arboretum & Botanical Gardens", description="A nationally acclaimed 66 acre display garden features breathtaking floral displays all year long",
                             city=dallas,
                             created_at=datetime(2017, 8, 5, 10, 00, 00))
session.add(attractionItem2)
session.commit()

attractionItem3 = Attraction(user_id=1, name="NASA's Space Center", description="The official visitor center for NASA's Johnson Space Center",
                             city=houston,
                             created_at=datetime(2017, 8, 5, 03, 00, 00))
session.add(attractionItem3)
session.commit()

attractionItem4 = Attraction(user_id=1, name="River Walk", description="You can shop, dine,and simply stroll along and let the strumming mariachi soothe your spirit",
                             city=sanantonio,
                             created_at=datetime(2017, 8, 5, 05, 00, 00))
session.add(attractionItem4)
session.commit()

#
print "all items added!"
