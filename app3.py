### Integrate HTML with Flask
## HTTP Verb GET And POST

from flask import Flask,request,redirect,url_for,render_template


app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="Pass"
    else:
        res="Fail"
    return render_template('results.html',result=res)

@app.route('/fail/<int:score>')
def fail(score):
    return f"The person has failed the exam with an average score of {score}"

@app.route('/results')
def results():
    # Retrieve marks for each subject from the form
    subject1 = int(request.args.get('subject1'))
    subject2 = int(request.args.get('subject2'))
    subject3 = int(request.args.get('subject3'))
    subject4 = int(request.args.get('subject4'))

    # Calculate total marks and average
    total_marks = subject1 + subject2 + subject3 + subject4
    average_marks = total_marks / 4

    # Determine pass or fail based on average marks
    if average_marks < 50:
        result = 'fail'
    else:
        result = 'success'
    
    return redirect(url_for(result, score=average_marks))



if __name__ == '__main__':
    app.run(debug=True)  