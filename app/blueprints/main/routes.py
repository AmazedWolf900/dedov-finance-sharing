from app.blueprints.main import bp

from flask import render_template
from sqlalchemy import func

from app.models.models import Project, Attachment

@bp.route("/")
def index():
    project_count = Project.query.count()

    attachment_count = Attachment.query.count()
    attachment_total_file_size = Attachment.query.with_entities(func.sum(Attachment.file_size).label("fs_total")).first()[0]

    return render_template("main/index.html",
                project_count = project_count,
                attachment_count = attachment_count,
                attachment_total_file_size = attachment_total_file_size
    )