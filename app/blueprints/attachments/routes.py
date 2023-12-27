from app.blueprints.attachments import bp

from flask import request, redirect, render_template, send_file

from app.models.finance import db, Attachment

@bp.route("/attachments/<int:attachment_id>/download")
def download(attachment_id):
    attachment = Attachment.query.filter_by(id = attachment_id).first()
    if attachment:
        UPLOAD_PATH = "static/attachments/"
        return send_file(UPLOAD_PATH + attachment.file_name, as_attachment=True, download_name = attachment.common_name)

@bp.route("/attachments/<int:attachment_id>/delete")
def delete(attachment_id):
    attachment = Attachment.query.filter_by(id = attachment_id).first()
    if attachment:
        from os import remove
        remove(attachment.file_path)
        db.session.delete(attachment)
        db.session.commit()

        return redirect(request.args.get("back_path"))

@bp.route("/attachments/<int:attachment_id>/view")
def view(attachment_id):
    attachment = Attachment.query.filter_by(id = attachment_id).first()
    if attachment:
        return render_template("attachments/view.html",
                               attachment = attachment,
                               back_path = request.args.get("back_path"))

@bp.route("/attachments/new/payment/<int:payment_id>", methods = ["POST"])
@bp.route("/attachments/new/item/<int:item_id>", methods = ["POST"])
@bp.route("/attachments/new/project/<int:project_id>", methods = ["POST"])
def new(payment_id = None, item_id = None, project_id = None):
    UPLOAD_PATH = "app/static/attachments/"

    common_file_name = request.form.get("file_name")
    file = request.files["file"]
    file_extension = file.filename.rsplit('.', 1)[1].lower()

    # set common file name
    if not common_file_name:
        common_file_name = file.filename
    else:
        common_file_name = common_file_name + "." + file_extension

    # generate unique file name
    from time import time
    from hashlib import md5
    file_name = md5(
        str(time()).encode()
    ).hexdigest() + "." + file_extension
    # set the file path
    file_path = UPLOAD_PATH + file_name

    # save file
    file.save(file_path)

    # get the file size
    from os import stat
    file_size = stat(file_path).st_size

    # save file to the database
    # save attachment to the database
    if payment_id:
        new_attachment = Attachment(
            file_path = file_path,
            file_extension = file_extension,
            file_name = file_name,
            common_name = common_file_name,
            file_size = file_size,
            payment_id = payment_id
        )
    elif item_id:
        new_attachment = Attachment(
            file_path = file_path,
            file_extension = file_extension,
            file_name = file_name,
            common_name = common_file_name,
            file_size = file_size,
            item_id = item_id
        )
    elif project_id:
        new_attachment = Attachment(
            file_path = file_path,
            file_extension = file_extension,
            file_name = file_name,
            common_name = common_file_name,
            file_size = file_size,
            project_id = project_id
        )
    db.session.add(new_attachment)
    db.session.commit()

    # redirect to the previous page
    return redirect(request.args.get("back_path"))