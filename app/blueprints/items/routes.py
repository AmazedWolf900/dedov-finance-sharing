from app.blueprints.items import bp

from flask import render_template, request, redirect, url_for

from app.models.models import db, Item, Paymentmethod, Person, Payment, Attachment

@bp.route("/items/<int:item_id>/delete")
def delete(item_id):
    item = Item.query.filter_by(id = item_id).first()
    # check if the item exists
    if item:
        project_id = item.project_id
        db.session.delete(item)
        db.session.commit()

        return redirect(
            url_for('projects.detail', project_id = project_id)
        )

@bp.route("/items/new", methods = ["GET", "POST"])
def new():
    # check if the url request is POST method
    if request.method == "POST":
        # load arguments
        name = request.form.get("name")
        description = request.form.get("description")
        cost = request.form.get("cost")
        project_id = request.args.get("project_id")

        # create new item
        new_item = Item(
            name = name,
            description = description,
            cost = cost,
            paid = 0,
            project_id = project_id
        )

        # commit new item to the database
        db.session.add(new_item)
        db.session.commit()
        
        # redirect back to the project's page
        return redirect(
                url_for("projects.detail", project_id = project_id)
            )

@bp.route("/items/<int:item_id>/detail")
def detail(item_id):
    # query item from the database
    item = Item.query.filter_by(id = item_id).first()
    # check if the item exists
    if item:
        # query payment methods
        payment_methods = Paymentmethod.query.all()
        # query persons
        persons = Person.query.all()

        return render_template(
            "items/detail.html",
            item = item,
            payment_methods = payment_methods,
            persons = persons,
            request = request
        )