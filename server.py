from flask import Flask, render_template, request, jsonify, redirect, url_for
import datetime
from flask import session

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
        ],
        "image": "learn1.jpeg"
    },
    2: {
        "name": "Lose Control",
        "ingredients": ["Vodka", "Redbull", "Ice"],
        "preparation_steps": [
            "Fill the glass with ice.",
            "Pour in two shots vodka.",
            "Fill the rest with redbull.",
            "Salute!"
        ],
        "image": "learn2.jpeg"
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
        ],
        "image": "learn3.jpeg"
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
        ],
        "image": "learn4.jpeg"
    },
    5: {
        "name": "Relax on the couch",
        "ingredients": ["Champagne/Sparkling Wine", "Orange Juice"],
        "preparation_steps": [
            "Fill a half glass with champagne/sparkling wine.",
            "Fill the rest with orange juice.",
            "Lay down and relax."
        ],
        "image": "learn5.jpeg"
    }
}

quizzes = {
    1: {
        'questions': [
            {
                'text': 'What is the main ingredient in a Coco Loco?',
                'options': ['Vodka', 'Rum', 'Tequila', 'Whiskey'],
                'answer': 'Rum'
            },
            {
                'text': 'How much ice is typically used in a Coco Loco?',
                'options': ['None', 'Cubed', 'Crushed', 'As desired'],
                'answer': 'As desired'
            },
            {
                'text': 'Which fruit is used in a Coco Loco?',
                'options': ['Lemon', 'Orange', 'Grapefruit', 'Lime'],
                'answer': 'Grapefruit'
            }
        ]
    },
    2: {
        'questions': [
            {
                'text': 'What type of alcohol is mixed with Redbull in Lose Control?',
                'options': ['Vodka', 'Gin', 'Whiskey', 'Rum'],
                'answer': 'Vodka'
            },
            {
                'text': 'What is the final gesture suggested in the preparation of Lose Control?',
                'options': ['Cheers', 'Salute', 'Toast', 'Clap'],
                'answer': 'Salute'
            }
        ]
    },
    3: {
        'questions': [
            {
                'text': 'What is the primary alcoholic ingredient in House Blend?',
                'options': ['Vodka', 'Gin', 'Campari', 'Rum'],
                'answer': 'Campari'
            },
            {
                'text': 'What type of juice complements Campari in House Blend?',
                'options': ['Lemon Juice', 'Apple Juice', 'Orange Juice', 'Grapefruit Juice'],
                'answer': 'Orange Juice'
            },
            {
                'text': 'How many ice cubes are typically used in the House Blend?',
                'options': ['1-2', '3-4', '5-6', '7-8'],
                'answer': '3-4'
            }
        ]
    },
    4: {
        'questions': [
            {
                'text': 'Which fruit is added to the wine and apple juice in Warm Drinks for Cold Days?',
                'options': ['Peaches', 'Oranges', 'Lemons', 'Apples'],
                'answer': 'Peaches'
            },
            {
                'text': 'What is the main liquid base in Warm Drinks for Cold Days?',
                'options': ['Beer', 'Vodka', 'Red Wine', 'Whiskey'],
                'answer': 'Red Wine'
            }
        ]
    },
    5: {
        'questions': [
            {
                'text': 'What kind of wine is used in Relax on the couch?',
                'options': ['Red Wine', 'White Wine', 'Champagne/Sparkling Wine', 'Rose Wine'],
                'answer': 'Champagne/Sparkling Wine'
            },
            {
                'text': 'What is mixed with the champagne in Relax on the couch?',
                'options': ['Lemon Juice', 'Apple Juice', 'Grapefruit Juice', 'Orange Juice'],
                'answer': 'Orange Juice'
            }
        ]
    }
}


@app.route('/')
def home():
    return render_template('home.html')


# Learn menu route
@app.route('/learn_menu')
def learn_menu():
    return render_template('learn_menu.html', lessons=lessons)

# Quiz menu route
@app.route('/quiz_menu')
def quiz_menu():
    return render_template('quiz_menu.html', lessons=lessons)

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
        return render_template('learn.html', data=lesson, previous_lesson=previous_lesson, next_lesson=next_lesson, quiz=quiz, lesson_id=lesson_number)
    else:
        return "Lesson not found"
@app.route('/quiz/<int:quiz_id>', methods=['GET', 'POST'])
def quiz_page(quiz_id):
    if request.method == 'GET':
        quiz = quizzes.get(quiz_id, {})
        next_quiz = quiz_id + 1 if quiz_id < len(quizzes) else None
        return render_template('quiz.html', quiz=quiz, quiz_id=quiz_id, next_quiz=next_quiz)

@app.route('/quiz/result')
def submit_total_score():
    return render_template('result.html')

if __name__ == "__main__":
    app.run(debug=True)
