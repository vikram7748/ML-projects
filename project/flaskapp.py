from flask import *
import pymysql as pm
app = Flask(__name__)
db= pm.connect(
    host= "localhost",
    user="root",
    password="",
    database="prnka_car")

cursor = db.cursor()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/showroom")
def showroom():
    return render_template("showroom.html")

@app.route("/buy")
def buy():
    cursor.execute("select * from buy")
    data = cursor.fetchall()
    return render_template("buy.html",userdata = data)

@app.route("/create",methods=["POST"])
def create():
    uname = request.form.get('uname')
    cars = request.form.get('cars')
    contacts = request.form.get('contacts')
    insq = "insert into buy(name,car,contact_no)values('{}','{}','{}')".format(uname,cars,contacts)
    try:
        cursor.execute(insq)
        db.commit()
        return redirect(url_for('buy'))
    except:
        db.rollback()
        return "error in query"
@app.route("/sell")
def sell():
    cursor.execute("select * from sell")
    dat = cursor.fetchall()
    return render_template("sell.html",userdat = dat)
    
@app.route("/creat",methods=["POST"])
def creat():
    uname = request.form.get('uname')
    cars = request.form.get('cars')
    contacts = request.form.get('contacts')
    insq = "insert into sell(name,car,contact_no)values('{}','{}','{}')".format(uname,cars,contacts)
    try:
        cursor.execute(insq)
        db.commit()
        return redirect(url_for('sell'))
    except:
        db.rollback()
        return "error in query"
if __name__=="__main__":
    app.run()