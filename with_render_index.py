from flask import Flask, render_template,redirect,url_for, request

app = Flask(__name__)

@app.route('/')
def apex_legends():
    return render_template('index.html')

@app.route('/gigachad/<int:kills>')
def gigachad(kills):
    return f"You have {kills} kills, you are a gigachad."

@app.route('/soychamp/<int:kills>')
def soychamp(kills):
    return f"You are a soychamp, go uninstall the game right now, you have only {kills} kills."

@app.route("/handsup/<int:deaths>")
def handsup(deaths):
    if deaths>=20:
        return redirect(url_for("gigachad", kills=deaths))
    return redirect(url_for("soychamp", kills=deaths))

@app.route('/yeet', methods=['POST','GET'])
def yeet():
    total_kills = 0
    if request.method == 'POST':
        total_kills = float(request.form['kills'])
    return redirect(url_for("num_kills", eliminations=total_kills))

@app.route('/num_kills/<int:eliminations>')
def num_kills(eliminations):
    if eliminations>=20:
        return render_template('result.html', status="GIGACHAD")
    return render_template('result.html', status='SOYCHAMP')

if __name__=='__main__':
    app.run(port=5000, debug=True)
    
## this is a new comment

    