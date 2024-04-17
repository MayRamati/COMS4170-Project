from flask import Flask, render_template, request, jsonify, session
import datetime

app = Flask(__name__)
app.secret_key = 'COMS4170'


lessons = {
    1: {
        "name": "Ol Fashioned",
        "ingredients": ["Scotch Whiskey", "Granulated Sugar", "Dashes Bitters", "Orange Slice", "Water", "Ice"],
        "preparation_steps": [
            "Put the sugar, bitters and water in a small tumbler.",
            "Mix until the suger dissolves if using granulated.",
            "Fill your glass with ice and stir in the Whiskey.",
            "Garnish with the orange.",
            "Drink!"
        ],
        "image": "learn1.jpeg"
    },
    2: {
        "name": "Sex on the Beach",
        "ingredients": ["Vodka", "peach schnapps", "Orange Juice","Cranberry Juice", "Orange slice", "glace cherry","Ice"],
        "preparation_steps": [
            "Fill the glass with ice.",
            "Pour some vodka, peach schnapps and fruit juices and stir.",
            "Decorate with the cherry and orange slice",
            "Salute!"
        ],
        "image": "learn2.jpeg"
    },
    3: {
        "name": "Classic Negroni",
        "ingredients": ["Campari", "Gin", "Orange Juice", "Orange", "Ice"],
        "preparation_steps": [
            "Pour in 3 shots of campari, 3 shots of gin into a glass or jug with ice.",
            "Stir well until the outside of the glass feels cold."
            "Fill with orange juice till ¾ of the glass is filled.",
            "Add a large ice sphere or some fresh ice."
            "Cut a slice of orange and lay it down inside the glass.",
            "Call your friends!"
        ],
        "image": "learn3.jpeg"
    },
    4: {
        "name": "Sangaria",
        "ingredients": ["Red Wine","Brandy", "Chopped Orange","Chopped Pear", "Chopped Lemon", "Cinnamon Sticks", "Sugar", "Ice","Sparkling Water"],
        "preparation_steps": [
            "Put the chopped fruits in a bowl.",
            "Sprinkle in the sugar and cinnamon and stir to coat.",
            "Stir the mixture with ice.",
            "Pour in the whine and brandy.",
            "Top with sparkling water.",
            "Enjoy! Relax on the couch"
        ],
        "image": "learn4.jpeg"
    },
    5: {
        "name": "Hot Toddy",
        "ingredients": ["Whisky", "Honey","Cinnamon Stick","Lemon - half juiced/half sliced",],
        "preparation_steps": [
            "Whisk the whisky and honey together.",
            "Add a cinnamon stick.",
            "Pour in boiling water.",
            "Add a splash of lemon juice."
            "Throw in a sliced lemon",
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
                'options': ['Arak', 'Rum', 'Tequila', 'Whiskey'],
                'answer': 'Arak'
            },
            {
                'text': 'How much ice is typically used in a Coco Loco?',
                'options': ['None', 'Quarter', 'Half', 'As desired'],
                'answer': 'Quarter'
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
    total_score = session.get('total_score', 0)
    session['total_score'] = 0
    return render_template('result.html', total_score=total_score)

@app.route('/quiz/<int:quiz_id>/score', methods=['POST'])
def update_score(quiz_id):
    score = request.json.get('score', 0)
    if 'total_score' not in session:
        session['total_score'] = 0
    session['total_score'] += score
    return jsonify({"message": "Score updated successfully", "total_score": session['total_score']})



if __name__ == "__main__":
    app.run(debug=True)
