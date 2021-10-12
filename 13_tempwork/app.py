# Squidcatman - Michelle Lo & Hellokitty, Angela Zhang & Inky, Deven Maheshwari & Batman
# SoftDev
# K13 - Template for Success/Using Flask/Creating flask app using the occupation python data 
# October 13 2021

from flask import Flask, render_template 
import csv
import random

app = Flask(__name__)



@app.route("/")
def hello_world():
    return "No hablo queso!"

@app.route("/occupyflaskst") 
def test_tmplt():
    jobp = {}
    with open('data/occupations.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            job = row["Job Class"]
            percentage = float(row["Percentage"])
            jobp[job] = str(percentage)
        del jobp['Total']
    return render_template( 'tablified.html', foo = "K13", random = chooseRandom(jobp), response = jobp)

def chooseRandom(jobdict):     #
    randVal = random.uniform(0, 100) # randomly chooses a number from 0 to total percentage
    for k, v in jobdict.items():
        randVal -= float(v)
        if randVal <= 0:    # first cumulative percentage >= random value is the job chosen
            return k

if __name__ == "__main__":
    app.debug = True
    app.run()
