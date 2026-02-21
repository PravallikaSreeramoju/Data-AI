from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from werkzeug.utils import secure_filename
import os

from models import Item
from database import users_db, items_db, cart_db, orders_db

app = Flask(__name__)
app.secret_key = "secret123"

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# -------------------------
# Authentication
# -------------------------

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        data = request.form

        if data["username"] in users_db:
            return "User exists"

        users_db[data["username"]] = {
            "password": data["password"]
        }

        return redirect("/login")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.form

        user = users_db.get(data["username"])

        if not user or user["password"] != data["password"]:
            return "Invalid credentials"

        session["user"] = data["username"]
        return redirect("/")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


# -------------------------
# Home Page
# -------------------------

@app.route("/")
def home():
    return render_template(
        "home.html",
        items=items_db.values()
    )



# -------------------------
# Upload Form
# -------------------------
@app.route("/upload", methods=["GET", "POST"])
def upload():

    if request.method == "POST":

        name = request.form["name"]
        price = request.form["price"]
        description = request.form["description"]
        file = request.files["image"]

        if not name or not price:
            return "Name and price required"

        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

        # Auto ID
        item_id = len(items_db) + 1

        items_db[item_id] = {
            "id": item_id,
            "name": name,
            "price": float(price),
            "description": description,
            "image": filename
        }

        return redirect("/")

    return render_template("upload.html")


# -------------------------
# REST API — ITEMS
# -------------------------

@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items_db)


@app.route("/items", methods=["POST"])
def create_item():
    try:
        data = Item(**request.json)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

    if data.id in items_db:
        return jsonify({"error": "Duplicate ID"}), 400

    items_db[data.id] = data.dict()
    return jsonify(data.dict()), 201


@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    if item_id not in items_db:
        return jsonify({"error": "Item not found"}), 404

    items_db[item_id].update(request.json)
    return jsonify(items_db[item_id])


@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    if item_id not in items_db:
        return jsonify({"error": "Item not found"}), 404

    del items_db[item_id]
    return jsonify({"message": "Deleted"})


# -------------------------
# CART
# -------------------------

@app.route("/cart/add/<int:item_id>")
def add_to_cart(item_id):
    # Check login
    if "user" not in session:
        return redirect("/login")
    user = session["user"]
    cart = cart_db.setdefault(user, [])
    cart.append(item_id)
    return redirect("/cart")



@app.route("/cart")
def view_cart():
    if "user" not in session:
        return redirect("/login")
    user = session["user"]
    cart_items = [
        items_db[i]
        for i in cart_db.get(user, [])
    ]
    return render_template("cart.html", items=cart_items)



@app.route("/cart/remove/<int:item_id>")
def remove_from_cart(item_id):
    user = session.get("user")

    cart_db[user].remove(item_id)
    return redirect("/cart")


# -------------------------
# CHECKOUT
# -------------------------

@app.route("/checkout")
def checkout():
    user = session.get("user")

    cart_items = [items_db[i] for i in cart_db.get(user, [])]
    total = sum(item["price"] for item in cart_items)

    return render_template("checkout.html", items=cart_items, total=total)


# -------------------------
# PAYMENT (Mock)
# -------------------------

@app.route("/payment", methods=["POST"])
def payment():
    user = session.get("user")

    orders_db[user] = cart_db.get(user, [])
    cart_db[user] = []

    return "Payment Successful ✅ Order Placed"


# -------------------------

if __name__ == "__main__":
    app.run(debug=True)
