from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

# Learning route
@app.route('/learn/<int:lesson_number>')
def learn(lesson_number):
    # You can handle the lesson number here, fetch data from a database or JSON file, and render the appropriate template
    return f"Learning lesson {lesson_number}"

# Quiz route
@app.route('/quiz/<int:question_number>')
def quiz(question_number):
    # Similar to the learning route, handle the question number and render the appropriate template
    return f"Quiz question {question_number}"

# Quiz result page route
@app.route('/quiz/result')
def quiz_result():
    # You can handle the quiz result here, calculate the score, and render the result template
    return "Quiz result page"

if __name__ == "__main__":
    app.run(debug=True)
