from app.blueprints.projects import bp

from flask import render_template, request, url_for, redirect
from sqlalchemy.sql import func

from app.models.models import db, Project, Item, Payment

@bp.route("/projects/list")
def list():
    projects = Project.query.all()
    return render_template("projects/list.html", projects=projects)

@bp.route("/projects/<int:project_id>/detail", methods=["GET"])
def detail(project_id):
    #project_id = request.args.get("project_id")
    # Check if the project_id is in the url args
    if project_id:
        project = Project.query.filter_by(id=project_id).first()
        # check if the project exists
        if project:
            # query project's items
            items = Item.query.filter_by(project_id=project_id).all()
            # query item's sum cost
            items_sum_cost = Item.query.with_entities(func.sum(Item.cost).label("items_sum_cost")).filter_by(project_id=project_id).order_by(Item.id).first()
            items_sum_cost = items_sum_cost[0]
            # query item's paid value
            items_paid_value = Item.query.with_entities(func.sum(Item.paid).label("items_paid_value")).filter_by(project_id=project_id).order_by(Item.id).first()
            items_paid_value = items_paid_value[0]
            return render_template("projects/detail.html",
                        project = project,
                        items = items,
                        items_count = len(items),
                        items_sum_cost = items_sum_cost,
                        items_paid_value = items_paid_value
            )
    
    return str(project_id)

@bp.route("/projects/new", methods=["GET", "POST"])
def new():
    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")

        # Check if there is project with the same name
        if not Project.query.filter_by(name=name).first():
            new_project = Project(
                name = name,
                description = description
            )
            # commit new project to the database
            db.session.add(new_project)
            db.session.commit()

            return redirect(
                url_for("projects.detail", project_id=new_project.id)
            )

@bp.route("/projects/<int:project_id>/delete")
def delete(project_id):
    project = Project.query.filter_by(id = project_id).first()
    # check if the project exists
    if project:
        db.session.delete(project)
        db.session.commit()

        return redirect(
            url_for("projects.list")
        )