from app.blueprints.main import bp

from flask import render_template
from sqlalchemy import func

from app.models.finance import Project, Attachment, Payment, Item
from app.db_size import getsize

@bp.route("/")
def index():
    project_count = Project.query.count()

    attachment_count = Attachment.query.count()
    attachment_total_file_size = Attachment.query.with_entities(func.sum(Attachment.file_size).label("fs_total")).first()[0]

    item_count = Item.query.count()
    item_total_cost = format(
        round(
            Item.query.with_entities(func.sum(Item.cost).label("cost_total")).first()[0],
            2),
        ","
    )

    payment_count = Payment.query.count()
    payment_total_value = format(
        round(
            Payment.query.with_entities(func.sum(Payment.value).label("value_total")).first()[0],
            2),
        ","
    )

    db_size = getsize()

    return render_template("main/index.html",
                project_count = project_count,
                attachment_count = attachment_count,
                attachment_total_file_size = attachment_total_file_size,
                item_count = item_count,
                item_total_cost = item_total_cost,
                payment_count = payment_count,
                payment_total_value = payment_total_value,
                db_size = db_size
    )