from flask import Flask, render_template,jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title' : 'Software Engineering',
    'location' : 'Nairobi, Kenya',
    'salary' : '120,000ksh'
  },

  {
    'id': 2,
    'title' : 'Accountant',
    'location' : 'Nairobi, Kenya',
    'salary' : '80,000ksh'
  },

  {
    'id': 3,
    'title' : 'Project Mananger',
    'location' : 'Nakuru, Kenya',
    'salary' : '70,000ksh'
  },

  {
    'id': 4,
    'title' : 'Web Designer',
    'location' : 'Mombasa, Kenya',
  
  },

]

@app.route("/")
def hello_world():
    return render_template("home.html",jobs = JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  
if __name__== "__main__":
  app.run(host='0.0.0.0' , debug=True)
  