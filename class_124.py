from flask import Flask,jsonify,request

app = Flask(__name__)

tasks = [
    {
        'id':1,
        'title':'Buy Groceries',
        'description':'milk,cheese,burger,fruits',
        'done':False
    },

    {
        'id':2,
        'title':'Learn Python',
        'description':'Need To Complete Pending work',
        'done':False
    }
    
]

@app.route("/")
def helloworld():
    return "Hello World"

@add.route("/add-data",methods = ["POST"])
def add_tasks():
    if not request.json:
        return jsonify({
            "Status":"Error",
            "Message":"Please Provide The Data"
        },400)
    task = {
        'id':tasks[-1]["id"]+1,
        'title':request.json["title"],
        'description':request.json.get("description",''),
        'done':False
    }
    tasks.append(task)
    return jsonify({
        "Status":"Success",
        "Message":"Tasks added Successfully"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })
        
if (__name__ == "__main__"):
    app.run()
