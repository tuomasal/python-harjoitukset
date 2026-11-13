import json
from flask import Flask, Response

app = Flask(__name__)
@app.route("/hello/<int:maara>")
def hello(maara):
    try:
        maara = int(maara)
        if maara < 1:
            raise ValueError
        response = {
            "message": ["Hello World!"] * maara,
            "status": 200
        }
        return response
    except ValueError:
        response = {
            "message": "Invalid number of repetitions",
            "status": 400
        }
        json_response = json.dumps(response)
        http_response = Response(response=json_response, status=400, mimetype="application/json")
        return http_response
    
    @app.errorhandler(404)
    def page_not_found(error_code):
        response = {
            "message": "Invalid endpoint",
            "status": 404
        }
        json_response = json.dumps(response)
        http_response = Response(
            response=json_response,
            status=404,
            mimetype="application/json"
        )
        return http_response

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000, use_reloader=True)