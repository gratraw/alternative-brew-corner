from flask import render_template, request, redirect
from app import app, db
from backend.data_validator import validate_recieved_data
from backend.models import RecipeModel


# The route for the default webpage - index
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        recipe = request.form
        correct_data = validate_recieved_data(recipe)
        print(correct_data)
        new_recipe = RecipeModel(
            name=correct_data["name"],
            time=correct_data["time"],
            coffee=correct_data["coffee"],
            water=correct_data["water"],
            description=correct_data["description"],
        )
        try:
            db.session.add(new_recipe)
            db.session.commit()
            return redirect("/")
        except:
            return "There was an error creating the recipe"
    else:
        recipes = RecipeModel.query.order_by(RecipeModel.id).all()
        return render_template("index.html", recipes=recipes)


@app.route("/delete/<int:id>")
def delete_recipe(id):
    recipe_to_delete = RecipeModel.query.get_or_404(id)
    try:
        db.session.delete(recipe_to_delete)
        db.session.commit()
        return redirect("/")
    except:
        return "There was an error deleting the recipe"


@app.route("/update/<int:id>", methods=["GET", "POST"])
def update_recipe(id):
    recipe_to_update = RecipeModel.query.get_or_404(id)
    if request.method == "POST":
        recipe = request.form
        correct_data = validate_recieved_data(recipe)
        print(correct_data)
        try:
            recipe_to_update.name = correct_data["name"]
            recipe_to_update.time = correct_data["time"]
            recipe_to_update.coffee = correct_data["coffee"]
            recipe_to_update.water = correct_data["water"]
            recipe_to_update.description = correct_data["description"]
            db.session.commit()
            return redirect("/")
        except:
            return "There was an error updating the recipe"
    else:
        return {
            "name": recipe_to_update.name,
            "time": recipe_to_update.time,
            "coffee": recipe_to_update.coffee,
            "water": recipe_to_update.water,
            "description": recipe_to_update.description,
        }
