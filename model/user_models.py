import json
from flask import make_response
import mysql.connector

class user_model:
    def __init__(self):
        # connection establishment
        try:
            self.con = mysql.connector.connect(
                host="localhost", user="root", password="", database="flask_tutorial"
            )
            # after insert queery we need to commit every time so
            self.con.autocommit = True
            # cursor will seed data inside database and allow to perform DML operation
            self.cur = self.con.cursor(
                dictionary=True
            )  # get data from database in dictionary format

            print("connection Successfully Established!")
        except:
            print("Connection Error")

    def user_getall_model(self):
        # Query execution code
        self.cur.execute("SELECT * FROM users")
        result = self.cur.fetchall()
        if len(result) > 0:
            # return json.dumps(result)
            # res = make_response({"payload":result}, 200)
            # #to allow cross server side request header is required
            # res.header['Access-Control-Allow-Origin'] = "*"
            # return res
            return make_response({"payload": result}, 200)
        else:
            return make_response("No Data Inside Database!", 204)

    def user_addone_model(self, data):
        # Query execution code
        self.cur.execute(
            f"INSERT INTO users(name, email, phone, role, password) VALUES('{data['name']}', '{data['email']}', '{data['phone']}', '{data['role']}', '{data['password']}')"
        )
        return make_response({"message": "User Created Successfully"}, 201)

    def user_update_model(self, data):
        # Query execution code
        # self.cur.execute(f"UPDATE users SET name = '{data['name']}', email = '{data['email']}', phone = '{data['phone']}, role = '{data['role']}', password = '{data['password']}' WHERE id = {data['id']} ")
        self.cur.execute(
            f"UPDATE users SET name='{data['name']}', email='{data['email']}', phone='{data['phone']}' WHERE id={data['id']}"
        )
        if self.cur.rowcount > 0:
            return make_response({"message": "User Update Successfully"}, 201)
        else:
            return make_response({"message": "User has nothing to update"}, 202)

    def user_delete_model(self, id):
        # Query execution code
        self.cur.execute(f"DELETE FROM users WHERE id={id}")

        if self.cur.rowcount > 0:
            return make_response({"message": "User Deleted Successfully"}, 200)
        else:
            return make_response({"message": "Nothing to Delete"}, 202)

    def user_patch_model(self, id, data):
        qry = "UPDATE users SET "
        for key in data:
            qry += f"{key}='{data[key]}',"
        qry = qry[:-1] + f" WHERE id = {id}"
        self.cur.execute(qry)
        if self.cur.rowcount > 0:
            return make_response({"message": "UPDATED_SUCCESSFULLY"}, 201)
        else:
            return make_response({"message": "NOTHING_TO_UPDATE"}, 204)

    def user_pagination_model(self, limit, page):
        limit = int(limit)
        page = int(page)
        start = (page * limit) - limit
        qry = f"SELECT * FROM users LIMIT {start}, {limit}"
        self.cur.execute(qry)
        result = self.cur.fetchall()
        if len(result) > 0:
            res = make_response(
                {"payload": result, "page_no": page, "limit": limit}, 200
            )
            return make_response({"payload": result}, 200)
        else:
            return make_response("No Data Inside Database!", 204)

    def user_profileImage_model(self, uid, filepath):
        self.cur.execute(
            f"UPDATE users SET profile_avatar='{filepath}' WHERE id = {uid}"
        )
        if self.cur.rowcount > 0:
            return make_response({"message": "User Profile Update Successfully"}, 201)
        else:
            return make_response(
                {"message": "User has not uploaded profile image"}, 202
            )
