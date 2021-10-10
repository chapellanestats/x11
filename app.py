from flask import Flask, render_template
from numpy import nan
from pandas.io.formats import style
import requests
import json
import pandas as pd
app = Flask(__name__)

#df.to_html("C:\\Python\TestApp\\templates\\test.html", na_rep=0)

@app.route('/', methods=("GET", "POST"))
def menus():
    return render_template('index.html')

@app.route('/Overperformers.html', methods=("GET", "POST")) 
def Overperformers():
    df = pd.set_option('colheader_justify', 'left')
    df = pd.read_excel("C:\\Users\\andre\\Documents\\X11_DB.xlsx", sheet_name="Overperformers")
    df.index = df.index + 1
    return render_template('Overperformers.html', tables=[df.to_html(classes='data', na_rep="0", index=True, bold_rows=False, columns=["Team Name", "Player Name", "Position", "Age", "Skill", "Games", "Goals", "Assists", "Avg. Over Performance"])])

@app.route('/Goals.html', methods=("GET", "POST")) 
def Goals():
    df = pd.set_option('colheader_justify', 'left')
    df = pd.read_excel("C:\\Users\\andre\\Documents\\X11_DB.xlsx", sheet_name="Goals")
    df.index = df.index + 1
    return render_template('Goals.html', tables=[df.to_html(classes='data', na_rep="0", index=True, bold_rows=False, columns=["Team Name", "Player Name", "Position", "Age", "Skill", "Games", "Goals", "Avg. Rating"])])

@app.route('/Assists.html', methods=("GET", "POST")) 
def Assists():
    df = pd.set_option('colheader_justify', 'left')
    df = pd.read_excel("C:\\Users\\andre\\Documents\\X11_DB.xlsx", sheet_name="Assists")
    df.index = df.index + 1
    return render_template('Assists.html', tables=[df.to_html(classes='data', na_rep="0", index=True, bold_rows=False, columns=["Team Name", "Player Name", "Position", "Age", "Skill", "Games", "Assists", "Avg. Rating"])])

@app.route('/Best Rated.html', methods=("GET", "POST")) 
def Best_Rated():
    df = pd.set_option('colheader_justify', 'left')
    df = pd.read_excel("C:\\Users\\andre\\Documents\\X11_DB.xlsx", sheet_name="Best Rated")
    df.index = df.index + 1
    return render_template('Best Rated.html', tables=[df.to_html(classes='data', na_rep="0", index=True, bold_rows=False, columns=["Position", "Player Name", "Team Name", "Age", "Skill", "Best Rating"])])
    
if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', debug=True)
