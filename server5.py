from flask import Flask,request,render_template
app=Flask(__name__)
@app.route("/")
def form():
    return render_template("12.03.html")
@app.route("/submit",methods=["POST"])
def submit():
    name=request.form.get("name")
    age=request.form.get("age")
    dob=request.form.get("dob")
    month=request.form.get("month")
    time=request.form.get("time")
    date_time=request.form.get("date-time")
    return f"<b>The updated form is</b> <br><br> Name:{name}<br>Age:{age} <br> DOB:{dob} <br>month:{month}<br> date-time:{date_time}"
if __name__=="__main__":
    app.run(debug=True)    