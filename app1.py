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

## redirect takes a URL or endpoint as its argument and sends a response that tells the browser to navigate to that URL.
## url_for generates a URL for the endpoint named result, which will be either 'success' or 'fail', and includes any parameters (in this case, score=marks) that are needed to build the URL.

if __name__ == '__main__':
    app1.run(debug=True)   