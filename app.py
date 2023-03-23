from flask import Flask, render_template, jsonify
app = Flask(__name__)
JOBS = [{
  'id':1,
  'title':'Data Analyst',
  'location': 'Bombay,India',
  'salary': 'Rs 10,00,000'
},       
  {
  'id':2,
  'title':'Data Scientist',
  'location': 'Gujarat,India',
  'salary': 'Rs 8,00,000'
},
  {
  'id':3,
  'title':'Backend Developer',
  'location': 'Remote,India',
  'salary': 'Rs 9,00,000'
},
 {
'id':4,
'title':'Frontend Developer',
'location': 'Sydney,India',
}
       ]
@app.route("/")
def hello():
  return render_template('home.html',jobs=JOBS)

@app.route("/api/jobs")
def jsonData():
  return jsonify(JOBS)

if __name__=='__main__':
  app.run(host = '0.0.0.0',debug=True)