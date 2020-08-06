import lpldata
from flask import Flask,render_template

app = Flask(__name__)
LPL = lpldata.Lpl_Data()

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/wingsvd',methods=['GET','POST'])
def wings_vd():
    return LPL.get_wings_vd()

@app.route('/memberdata',methods=['GET','POST'])
def memberdata():
    return LPL.get_member_top12()

@app.route('/wingstop5',methods=['GET','POST'])
def wings_top5():
    return LPL.get_wings_top5()

@app.route('/heropick',methods=['GET','POST'])
def hero_pick():
    return LPL.get_hero_top60()

@app.route('/homeround',methods=['GET','POST'])
def home_round():
    return LPL.get_home_data()
if __name__ == '__main__':
    app.run(debug=True)