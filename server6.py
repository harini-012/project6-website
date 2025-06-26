from flask import Flask,request,render_template
app=Flask(__name__)
@app.route("/",methods=['GET','POST'])
def form():
    if request.method =='POST':
        data={"name":request.form.get('name'),
        "email":request.form.get('email'),
        "contact":request.form.get('contact'),
        "gender":request.form.get('gender'),
        "type":request.form.get('type'),
        "state":request.form.get('state'),
        "file":request.files.get('file').filename if request.files.get('file') else "No file uploaded"
        }
        return render_template("14.03hwresult.html",data=data)
    return render_template("14.03.html")
if __name__=='__main__':
    app.run(debug=True)