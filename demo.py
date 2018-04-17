from flask import Flask,request,render_template
import pymysql
db = pymysql.connect("localhost", "root", "123456", "nongda", charset='utf8' )

app=Flask(__name__)

@app.route("/",methods=["GET"])
def index():
    cursor = db.cursor()
    cursor.execute("select * from stus")
    results = cursor.fetchall()
    print(results);
    return render_template("index.html",results=results)
@app.route("/add",methods=["GET"])
def add():
    return render_template("add.html")
@app.route("/addcon",methods=["GET"])
def addcon():
    name=(request.args.get("name"))
    age=(request.args.get("age"))
    sex=(request.args.get("sex"))
    cursor = db.cursor()
    sql="insert into stus (name,age,sex) values ('"+name+"','"+age+"','"+sex+"')"
    cursor.execute(sql)
    db.commit()
    return render_template("notice.html")
@app.route("/del",methods=["GET"])
def del1():
    id=request.args.get("id")
    cursor = db.cursor()
    cursor.execute("delete from stus where id="+id)
    db.commit()
    return render_template("notice.html")
app.run()






