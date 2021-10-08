# Squidcatman - Michelle Lo & Hellokitty, Angela Zhang & Inky, Deven Maheshwari & Batman
# SoftDev
# K13 - //
# October 8 2021

from flask import Flask, render_template 
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "No hablo queso!"

coll = [0,1,1,2,3,5,8]

@app.route("/occupyflaskst") 
def test_tmplt():
    return render_template( 'model_tmplt.html', foo="fooooo", collection=coll)

if __name__ == "__main__":
    app.debug = True
    app.run()
