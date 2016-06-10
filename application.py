from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
## import CRUD Operations
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, CategoryItem

app = Flask(__name__)

#Create session and connect to DB
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

#Making an API Endpoint (GET Request)
@app.route('/categories/<int:category_id>/menu/JSON')
def restaurantMenuJSON(restaurant_id):
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    return jsonify(MenuItems=[i.serialize for i in items])

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON/')
def restaurantMenuItemJSON(restaurant_id, menu_id):
    singleMenuItem = session.query(MenuItem).filter_by(id=menu_id).one()
    return jsonify(singleMenuItem=singleMenuItem.serialize)

#Landing Page
#Show all categories

@app.route('/')
def categories():
    categories = session.query(Category).all()
    items = session.query(CategoryItem).order_by('id desc').limit(10).all()
    return render_template('categories.html', category=categories, items = items)

#Create new category

@app.route('/new/', methods=['GET','POST'])
def newCategory():
    if request.method == 'POST':
        newCategory = Category(name = request.form['name'])
        session.add(newCategory)
        session.commit()
        flash("new category created!")
        return redirect(url_for('categories'))
    else:
        return render_template('newcategory.html')

#Edit Category

@app.route('/<category_name>/edit/', methods=['GET','POST'])
def editCategory(category_name):
    category = session.query(Category).filter_by(name=category_name).one()
    if request.method == 'POST':
        if request.form['name']:
            category.name = request.form['name']
        session.add(category)
        session.commit()
        flash("category name changed!")
        return redirect(url_for('categories'))
    else:
        return render_template('editcategory.html', category_name = category_name)


#Delete category

@app.route('/<category_name>/delete/', methods=['GET','POST'])
def deleteCategory(category_name):
    category = session.query(Category).filter_by(name=category_name).one()
    if request.method == 'POST':
	items = session.query(CategoryItem).filter_by(category_id = category.id).all()
	for i in items:
		session.delete(i)
        session.delete(category)
        session.commit()
        flash("category deleted!")
        return redirect(url_for('categories'))
    else:
        return render_template('deletecategory.html', category_name = category_name)

#Individual category page

@app.route('/<category_name>')
def categoryItems(category_name):
    categories = session.query(Category).all()
    category = session.query(Category).filter_by(name=category_name).one()
    items = session.query(CategoryItem).filter_by(category_id=category.id).all()
    return render_template('categoryitems.html',categories = categories, category = category, items = items)

#Individual item page

@app.route('/<category_name>/<int:item_id>/')
def singleItem(category_name, item_id):
    categories = session.query(Category).all()
    category = session.query(Category).filter_by(name=category_name).one()
    items = session.query(CategoryItem).filter_by(category_id=category.id).all()
    singleItem = session.query(CategoryItem).filter_by(id=item_id).one()
    return render_template('singleitem.html', category_name = category_name, item_id = item_id, i = singleItem, categories = categories, category = category, items = items)

# Task 1: Create route for new Item function here
@app.route('/newitem/', methods=['GET','POST'])
def newCategoryItem():
    if request.method == 'POST':
    	category = session.query(Category).filter_by(name=request.form['categoryname']).one()
        newItem = CategoryItem(name = request.form['name'], category_id = category.id)
	if request.form['description']:
		newItem.description = request.form['description']
	else:
		newItem.description = 'no description added yet'
        session.add(newItem)
        session.commit()
        flash("new item created!")
        return redirect(url_for('categories'))
    else:
    	categories = session.query(Category).all()
        return render_template('newitem.html', categories = categories)

# Task 2: Create route for editMenuItem function here

@app.route('/<category_name>/<int:item_id>/edit/', methods=['GET','POST'])
def editCategoryItem(category_name, item_id):
    editedItem = session.query(CategoryItem).filter_by(id=item_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['description']:
            editedItem.description = request.form['description']
        session.add(editedItem)
        session.commit()
        flash("item edited!")
        return redirect(url_for('categoryItems', category_name = category_name))
    else:
        return render_template('editcategoryitem.html', category_name = category_name, item_id = item_id, i = editedItem)

# Task 3: Create a route for deleteMenuItem function here

@app.route('/<category_name>/<int:item_id>/delete/', methods=['GET','POST'])
def deleteCategoryItem(category_name, item_id):
    itemToDelete = session.query(CategoryItem).filter_by(id=item_id).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        flash("item deleted!")
        return redirect(url_for('categoryItems', category_name = category_name))
    else:
        return render_template('deletecategoryitem.html', category_name = category_name, item_id = item_id, i = itemToDelete)

# Task 4: Create a new restaurant here


#Using flask to route site
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port = 8000)
