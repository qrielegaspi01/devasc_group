from flask import Flask, jsonify, request

app = Flask(__name__)

glucose = [
    {
        "glucose_id" : "100",
        "date" : ["11-04-22"],
        "glucose_rate" : [ "110"]
    },
    {
        "glucose_id" : "102",
        "date" : ["11-05-22"],
        "glucose_rate" : [ "95"]
    }
]
@app.route ('/glucose', methods=['GET'])
def getGlucose():
    return jsonify(glucose)
@app.route('/glucose', methods=['POST'])
def addGlucose():
    glucose = request.get_json()
    glucose.append(glucose)
    return {'id': len(glucose)},200

@app.route('/glucose/<int:index>', methods=['DELETE'])
def deleteGlucose(index):
    glucose.pop(index)
    return 'glucose id was deleted' , 200

if __name__ ==  '__main__':
    app.run()