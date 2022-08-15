from flask import Flask, request, jsonify

app = Flask(__name__)

contacts = [
    {
        "contact": 6589565478,
        "name": "Aarshi",
        "done": False,
        "id": 1
    },
    {
        "contact": 9854758484,
        "name": "Fiza",
        "done": False,
        "id": 2
    }
]
@app.route("/add-data", methods = ["POST"])

def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "please provide the data"
        }, 400)
    contact = {
        "contact": request.json.get('Contact', ""),
        "name": request.json["name"],
        "id": contacts[-1]["id"] +1,
        "done": False
    }
    contacts.append(contact)
    return jsonify({
        "status": "success",
        "message": "contact added successfully"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data": contacts,
    })
if (__name__=="__main__"):
    app.run(debug = True)