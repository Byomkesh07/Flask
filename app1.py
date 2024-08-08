# Building url dynamically

from flask import Flask,redirect,url_for


app1 = Flask(__name__)

@app1.route('/success/<int:score>')
def success(score):
    return "The person has passed the exam with marks " + str(score)

@app1.route('/fail/<int:score>')
def fail(score):
    return "The person has failed the exam with marks " + str(score)

#Result checker
@app1.route('/results/<int:marks>')
def results(marks):
    result = ""
    if marks<50 :
        result = 'fail'
    else:
        result = 'success'
    return redirect(url_for(result,score=marks))


if __name__ == '__main__':
    app1.run(debug=True)   