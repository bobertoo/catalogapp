from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, CategoryItem

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# adding categories
newCategory1 = Category(name="Skateboarding")
session.add(newCategory1)
session.commit()

newCategory2 = Category(name="Rollerblading")
session.add(newCategory2)
session.commit()

newCategory3 = Category(name="Pogoing")
session.add(newCategory3)
session.commit()

newCategory4 = Category(name="Surfing")
session.add(newCategory4)
session.commit()


# adding category items
categoryItem1 = CategoryItem(
    name="Skate Deck",
    description="This is the actual board",
    category=newCategory1)
session.add(categoryItem1)
session.commit()

categoryItem2 = CategoryItem(
    name="blades",
    description="These are the bladez",
    category=newCategory2)
session.add(categoryItem2)
session.commit()

categoryItem3 = CategoryItem(
    name="pogo stick",
    description="The stick with the springs",
    category=newCategory3)
session.add(categoryItem3)
session.commit()

categoryItem4 = CategoryItem(
    name="Surf Board",
    description="The thing you stand on",
    category=newCategory4)
session.add(categoryItem4)
session.commit()

categoryItem5 = CategoryItem(
    name="Helmet",
    description="Protect ur melon",
    category=newCategory1)
session.add(categoryItem5)
session.commit()

categoryItem6 = CategoryItem(
    name="Knee Pads",
    description="Keep those knees bruise free",
    category=newCategory2)
session.add(categoryItem6)
session.commit()

categoryItem7 = CategoryItem(
    name="Water Bottle",
    description="h2o to fuel the pogo",
    category=newCategory3)
session.add(categoryItem7)
session.commit()

categoryItem8 = CategoryItem(
    name="wax",
    description="Slick up the board to slice those waves",
    category=newCategory4)
session.add(categoryItem8)
session.commit()

categoryItem9 = CategoryItem(
    name="pepperoni pizza",
    description="gotta keep energy up",
    category=newCategory1)
session.add(categoryItem9)
session.commit()

categoryItem10 = CategoryItem(
    name="monster energy drink",
    description="FUEL THE BEAST",
    category=newCategory2)
session.add(categoryItem10)
session.commit()

print "added new categories"
