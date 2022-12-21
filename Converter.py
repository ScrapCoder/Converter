from flask import Flask, render_template,request
app=Flask(__name__)

@app.route("/",methods=['POST',"GET"])
def home():
    if request.method=="POST":
        n1=eval(request.form["conum"])
        menu=request.form["Setting"]

        if menu=="C-->F":
            ans=(n1*9/5) +32

        if menu=="F-->C":
            ans=(n1-32)*5/9
        return render_template("Converted.html",**{"answer":ans})
    return render_template("home_page.html")

if __name__=="__main__":
    app.run(debug=True)