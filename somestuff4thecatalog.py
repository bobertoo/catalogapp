from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, CategoryItem

engine = create_engine('sqlite:///catalog.db')
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

# adding categories
newCategory1 = Category(name="Skateboarding")
session.add(newCategory1)
session.commit()

newCategory2 = Category(name="Rollerblading")
session.add(newCategory2)
session.commit()


# adding category items
categoryItem1 = CategoryItem(name="Skate Deck", description="This is the actual board",
                     category=newCategory1)

session.add(categoryItem1)
session.commit()

categoryItem2 = CategoryItem(name="blades", description="These are the bladez",
                     category=newCategory2)

session.add(categoryItem2)
session.commit()

print "added new categories"
