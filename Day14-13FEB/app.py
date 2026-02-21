from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def validate_input(name, email, age):
    if not name or not email or not age:
        return False, "All fields are required"

    if "@" not in email:
        return False, "Invalid email format"

    try:
        age = int(age)
        if age < 18:
            return False, "Age must be 18 or above"
    except ValueError:
        return False, "Age must be a number"

    return True, "Registration successful"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        age = request.form.get("age")

        valid, message = validate_input(name, email, age)

        if valid:
            return render_template("index.html", success=message)
        else:
            return render_template("index.html", error=message)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)