"""Flask demo app for test purposes"""
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/")
def hello():
  print(request.accept_mimetypes)
  message = "Hello World!"

  response = jsonify({"message": message})
  return response



if __name__ == "__main__":
    app.run()