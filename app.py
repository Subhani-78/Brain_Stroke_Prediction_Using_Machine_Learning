from flask import Flask

app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    return "<i>Project Started</i>"


if __name__=="__main__":
    app.run()

# CI CD Pipeline =>