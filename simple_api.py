from flask import Flask, render_template, jsonify, request, session
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:Ahmed.Hashim02@localhost/friendsdb'
# creating DB connection for Postgress
db = SQLAlchemy(app)     # initialize SQL Alchemy
app.secret_key = 'secret_key'

class Friend(db.Model):
    name = db.Column(db.String(100), nullable = False)
    city = db.Column(db.String(100), nullable = False)
    contact = db.Column(db.String(100), unique = True, nullable = False, primary_key = True)

with app.app_context():
    db.create_all()

@app.route("/records")
def get_records():
    friends = Friend.query.all()
    friend_list = [{'name':friend.name, 'city':friend.city, 'contact':friend.contact} for friend in friends]
    return jsonify({'friends':friend_list})



data = [
    {'name':'Okasha','city':'Peshawar','contact':'+923069831221'},
    {'name':'Atif','city':'Peshawar','contact':'+923005986553'},
    {'name':'Kamran','city':'Peshawar','contact':'+923339301903'},
    {'name':'Aisha','city':'Wakefield','contact':'+447765658534'},
]

@app.route("/")
def home():
    return "<h1>We are making API-Home Page!</h1>"

@app.route("/api_response")
def response():
    return jsonify(data)

@app.route("/record", methods=['GET','POST'])
def add_record():
    # if request.method=="POST":       #for JSON response from Postman
    #     data_rcvd = request.get_json()
    #     record = {'name':data_rcvd['name'], 'city':data_rcvd['city'], 'contact':data_rcvd['contact']}
    #     data.append(record)
    #     return "Record Added Successfully"
    # else:
    #     pass

    if request.method == "POST":         # for receiving data from html form
        record={'name':request.form['name'],'city':request.form['city'],'contact':request.form['contact']}
        data.append(record)
        return "Record Added Successfully"
    else:
        return render_template('response.html')

@app.route("/db_record", methods=['GET','POST'])
def add_db_record():
    # if request.method=="POST":
    #     data = request.get_json()
    #     new_friend = Friend(name=data['name'], city=data['city'], contact = data['contact'])
    #     db.session.add(new_friend)
    #     db.session.commit()
    #     return jsonify({'msg':"Friend Added"})
    # else:
    #     return "Please add record via Postman in JSON Format"
    
    # if request.method=="POST":       #for JSON response from Postman
    #     data_rcvd = request.get_json()
    #     record = {'name':data_rcvd['name'], 'city':data_rcvd['city'], 'contact':data_rcvd['contact']}
    #     data.append(record)
    #     return "Record Added Successfully"
    # else:
    #     pass

    if request.method == "POST":         # for receiving data from html form
        record=Friend(name=request.form['name'],city=request.form['city'],contact=request.form['contact'])
        db.session.add(record)
        db.session.commit()
        return jsonify({'msg':"Friend Added"})
    else:
        return "Please add record via Postman in JSON Format"
    #     return "Record Added Successfully"
    # else:
    #     return render_template('response.html')
    
  



if __name__=="__main__":
    app.run(debug=True)