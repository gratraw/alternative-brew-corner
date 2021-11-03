
from flask import render_template, request, redirect
from app import app, db
from backend.models import RecipeModel


#The route for the default webpage - index
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        recipe = request.form
        new_recipe = RecipeModel(name=recipe.get('name'), time=recipe.get('time'), coffee=recipe.get('coffee'), water=recipe.get('water'), description=recipe.get('description'))
        try:   
            db.session.add(new_recipe)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an error creating the recipe'
    else:
        recipes = RecipeModel.query.order_by(RecipeModel.id).all()
        return render_template('index.html', recipes=recipes)

@app.route('/delete/<int:id>')
def delete_recipe(id):
    recipe_to_delete = RecipeModel.query.get_or_404(id)
    try:
        db.session.delete(recipe_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an error deleting the recipe'

@app.route('/update/<int:id>', methods=['GET','POST'])
def update_recipe(id):
    recipe_to_update = RecipeModel.query.get_or_404(id)
    if request.method == 'POST':
        recipe = request.form
        try:
            recipe_to_update.name=recipe.get('name')
            recipe_to_update.time=recipe.get('time')
            recipe_to_update.coffee=recipe.get('coffee')
            recipe_to_update.water=recipe.get('water')
            recipe_to_update.description=recipe.get('description')
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an error updating the recipe'
    else:
        return render_template('form.html', recipe=recipe_to_update)
