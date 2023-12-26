from app.blueprints.payments import bp

from flask import request, redirect, url_for, render_template

from app.models.models import db, Payment, Item, Person, Paymentmethod, Attachment

@bp.route("/payments/list/page/<int:page>")
def list(page = 1):
    # query payments
    payments = Payment.query.paginate(page = 1, per_page = 10)
    # query persons
    persons = Person.query.all()
    # query items
    items = Item.query.all()

    return render_template("payments/list.html",
                            payments = payments,
                            persons = persons,
                            items = items
    )

@bp.route("/payments/<int:payment_id>/detail")
def detail(payment_id):
    # check if the payment exists
    payment = Payment.query.filter_by(id = payment_id).first()
    if payment:
        # query person
        person = Person.query.filter_by(id = payment.person_id).first()
        # query payment method
        payment_method = Paymentmethod.query.filter_by(id = payment.payment_method_id).first()
        # query attachments
        attachments = Attachment.query.filter_by(payment_id = payment.id).all()
        return render_template("payments/detail.html",
                               payment = payment,
                               person = person,
                               payment_method = payment_method,
                               attachments = attachments
#                               request = request
        )

@bp.route("/payments/new", methods = ["POST"])
def new():
    # check if the url request method is POST
    if request.method == "POST":
        # load arguments
        value = float(request.form.get("value")) # load as the float
        payment_method = request.form.get("payment_method")
        person = request.form.get("person")
        item_id = request.form.get("item_id")

        # create new payment
        new_payment = Payment(
            value = round(value, 2), # round value to 2nd decimal place
            payment_method_id = payment_method,
            item_id = item_id,
            person_id = person
        )

        # update item's paid value according to the new payment
        item = Item.query.filter_by(id = item_id).first()
        item.paid += float(value)

        # commit new payment to the database
        db.session.add(new_payment)
        db.session.commit()

        # redirect back to the item's page
        return redirect(
            url_for("items.detail", item_id = item_id)
        )

@bp.route("/payments/<int:payment_id>/delete")
def delete(payment_id):
    # check if the payment exists
    payment = Payment.query.filter_by(id = payment_id).first()
    if payment:
        # load item
        item = Item.query.filter_by(id = payment.item_id).first()
        # update item's paid value according to payment deletion
        item.paid -= round(float(payment.value), 2)
        # delete payment from the database
        db.session.delete(payment)
        db.session.commit()

        # redirect back to the item's page
        return redirect(
            url_for("items.detail", item_id = item.id)
        )