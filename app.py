from flask import Flask, render_template, jsonify
from database import load_job_from_db

app = Flask(__name__)
jobs=load_job_from_db()
@app.route("/")
def hello():
  return render_template('home.html', jobs=jobs)


@app.route("/api/jobs")
def jsonData():
  return jsonify(jobs)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
