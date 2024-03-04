from flask import request, send_file
from app import app
from model.user_models import user_model
from datetime import datetime

obj = user_model()

@app.route("/user/getall")
def user_get_all():
    return obj.user_getall_model()


@app.route("/user/addone", methods=["POST"])
def user_addone():
    return obj.user_addone_model(request.form)


@app.route("/user/update", methods=["PUT"])
def user_update():
    return obj.user_update_model(request.form)


@app.route("/user/delete/<int:id>", methods=["DELETE"])
def user_delete(id):
    return obj.user_delete_model(id)


@app.route("/user/patch/<int:id>", methods=["PATCH"])
def user_patch(id):
    return obj.user_patch_model(id, request.form)


@app.route("/user/getall/limit/<int:limit>/page/<int:page>", methods=["GET"])
def user_pagination(limit, page):
    return obj.user_pagination_model(limit, page)


@app.route("/user/<uid>/upload/image", methods=["PUT"])
def user_avatar(uid):
    file = request.files["avatar"]
    date = str(datetime.now().timestamp())  # for unique name
    fileName_split = file.filename.split(".")
    # ext = fileName_split[len(fileName_split) - 1]
    ext = fileName_split[-1]
    name = fileName_split[0]
    new_name = f"{name}_{date}.{ext}"
    filepath = f"uploads/{new_name}"
    file.save(filepath)
    return obj.user_profileImage_model(uid, filepath)


@app.route("/uploads/<filename>")
def user_getImage(filename):
    return send_file(f"uploads/{filename}")
