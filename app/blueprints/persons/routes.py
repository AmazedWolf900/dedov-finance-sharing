from app.blueprints.persons import bp

from flask import render_template, request, redirect, url_for
from sqlalchemy.sql import func

from app.models.models import db, Person, Payment

@bp.route("/persons/<int:person_id>/delete")
def delete(person_id):
    person = Person.query.filter_by(id = person_id).first()
    if person:
        db.session.delete(person)
        db.session.commit()

        return redirect(
            url_for("persons.list")
        )

@bp.route("/persons/new", methods = ["POST"])
def new():
    if request.method == "POST":
        name = request.form.get("name")
        address = request.form.get("address")

        new_person = Person(
            name = name,
            address = address
        )

        db.session.add(new_person)
        db.session.commit()

        return redirect(
            url_for("persons.detail", person_id = new_person.id)
        )

@bp.route("/persons/list/page/<int:page>")
def list(page = 1):
    persons = Person.query.paginate(page = page, per_page = 10)
    return render_template("persons/list.html", persons = persons)

@bp.route("/persons/<int:person_id>/detail")
def detail(person_id):
    # query person
    person = Person.query.filter_by(id = person_id).first()
    if person:
        payments_sum =  Payment.query.with_entities(func.sum(Payment.value)).filter_by(person_id = person_id).first()[0]
        return render_template(
            "persons/detail.html",
            person = person,
            payments_sum = payments_sum)