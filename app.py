from flask import Flask, render_template,redirect,url_for

app = Flask(__name__)

@app.route('/')
def apex_legends():
    # kills = input("kills:" )
    return "You are now playing apex legends."

@app.route('/gigachad/<int:kills>')
def gigachad(kills):
    return f"You have {kills} kills, you are a gigachad."

@app.route('/soychamp/<int:kills>')
def soychamp(kills):
    return f"You are a soychamp, go uninstall the game right now, you have only {kills} kills."


### this block of code redirects user to the new page instead of keeping them on the same page ..
@app.route("/handsup/<int:deaths>")
def handsup(deaths):
    if deaths>=20:
        return redirect(url_for("gigachad", kills=deaths))
    return redirect(url_for("soychamp", kills=deaths))


### This block will keep the user on the same page rather than redirecting them to the new page for that specific condition.
# @app.route('/handsup/<int:kills>')
# def handsup(kills):
#     if kills>=20:
#         return gigachad(kills)
#     return soychamp(kills)


if __name__=='__main__':
    app.run(port=5000, debug=True)
    
    