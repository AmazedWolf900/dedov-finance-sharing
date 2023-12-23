from app.blueprints.main import bp

from flask import render_template

from app.models.models import Project

@bp.route("/")
def index():
    project_count = Project.query.count()
    return render_template("main/index.html",
                project_count=project_count
    )