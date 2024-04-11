from flask import Flask, render_template, session
import datetime

app = Flask(__name__)
app.secret_key = 'COMS4170'

lessons = {
    1: {
        "name": "Coco Loco",
        "ingredients": ["Arak", "Grapefruit", "Mint Leaves", "Ice"],
        "preparation_steps": [
            "Fill a quarter of a glass with ice.",
            "Pour in Arak till it fills ⅓ of the glass.",
            "Fill the rest with grapefruit.",
            "Throw a bunch of mint leaves in.",
            "Stir.",
            "Drink!"
        ]
    },
    2: {
        "name": "Lose Control",
        "ingredients": ["Vodka", "Redbull", "Ice"],
        "preparation_steps": [
            "Fill the glass with ice.",
            "Pour in two shots vodka.",
            "Fill the rest with redbull.",
            "Salute!"
        ]
    },
    3: {
        "name": "House Blend",
        "ingredients": ["Campari", "Orange Juice", "Orange", "Ice"],
        "preparation_steps": [
            "Put 3-4 ice cubes in a glass.",
            "Pour in 3 shots of campari.",
            "Fill with orange juice till ¾ of the glass is filled.",
            "Cut a slice of orange and lay it down inside the glass.",
            "Call your friends!"
        ]
    },
    4: {
        "name": "Warm Drinks for Cold Days",
        "ingredients": ["Red Wine", "Apple Juice", "Cinnamon Sticks", "Peaches"],
        "preparation_steps": [
            "Pour in a bottle of Wine into a pot.",
            "Pour 4 cups of apple juice.",
            "Throw in a bunch of cinnamon sticks.",
            "Throw in sliced tiny pieces of peaches.",
            "Heat until boiling",
            "Enjoy! Relax on the couch"
        ]
    },
    5: {
        "name": "Relax on the couch",
        "ingredients": ["Champagne/Sparkling Wine", "Orange Juice"],
        "preparation_steps": [
            "Fill a half glass with champagne/sparkling wine.",
            "Fill the rest with orange juice.",
            "Lay down and relax."
        ]
    }
}

@app.route('/')
def home():
    return render_template('home.html')

# Learning route
@app.route('/learn/<int:lesson_number>', methods=['GET', 'POST'])
def learn(lesson_number):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    session['lesson_number'] = lesson_number
    session['enter_time'] = current_time
    lesson = lessons.get(lesson_number)

    previous_lesson = lesson_number - 1 if lesson_number > 1 else None
    next_lesson = lesson_number + 1 if lesson_number < len(lessons) else None
    quiz = lesson_number

    if lesson:
        print("Session:", session)
        return render_template('learn.html', data=lesson, previous_lesson=previous_lesson, next_lesson=next_lesson,quiz=quiz)
    else:
        return "Lesson not found"


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
