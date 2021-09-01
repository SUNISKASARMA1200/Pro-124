from flask import Flask,jsonify,request
app = Flask(__name__)

tasks = [
    {
        "id":1 ,
        "name":u'Sukanya Sarma ',
        "contact":u"9365298700",
        "done":False,
    },
    {
        "id":2 ,
        "name":u'Susibrat Sarma',
        "contact":u"9435709116",
        "done":False,
    }
]

@app.route("/add-data",
methods = ["POST"])

def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data"
        },400)

    task = {
        "id":tasks[-1]["id"]+1,
        "name":request.json['name'],
        "contact":request.json.get('contact'),
        'done':False
    }

    tasks.append(task)

    return jsonify({
        "status":"success",
        "message":"task added successfully",
    })

@app.route('/get-data')

def get_task():
    return jsonify({
        "data":tasks
    })


if(__name__ == "__main__"):
    app.run(debug=True)
