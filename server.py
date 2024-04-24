from flask import Flask, render_template, request, jsonify, session
import datetime

app = Flask(__name__)
app.secret_key = 'COMS4170'


lessons = {
    1: {
        "name": "Old Fashioned",
        "ingredients": ["Scotch Whiskey", "Granulated Sugar", "Dashes Bitters", "Orange Slice", "Water", "Ice"],
        "preparation_steps": [
            "Put the sugar, bitters and water in a small tumbler.",
            "Mix until the suger dissolves if using granulated.",
            "Fill your glass with ice and stir in the Whiskey.",
            "Garnish with the orange.",
            "Drink!"
        ],
        "image": "learn8.jpeg"
        "video": 'Old Fashioned.mp4'
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
        "image": "learn7.jpeg"
        "video": 'sex on the beach.mp4'
    },
    3: {
        "name": "Classic Negroni",
        "ingredients": ["Campari", "Gin", "Orange Juice", "Orange", "Ice"],
        "preparation_steps": [
            "Pour in 3 shots of campari, 3 shots of gin into a glass or jug with ice.",
            "Stir well until the outside of the glass feels cold."
            "Fill with orange juice till ¾ of the glass is filled.",
            "Add a large ice sphere.",
            "Cut a slice of orange and lay it down inside the glass.",
            "Call your friends!"
        ],
        "image": "learn3.jpeg"
        "video": 'Classic Negroni.mp4'
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
        "video": 'Sangeria.mp4'
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
        "image": "learn6.jpeg"
        "video": 'hot toddy.mp4'
    }
}

quizzes = {
    1: {
        'questions': [
            {
                'text': 'What is the main ingredient in an Old Fashioned cocktail?',
                'options': ['Arak', 'Rum', 'Tequila', 'Scotch Whiskey'],
                'answer': 'Scotch Whiskey'
            },
            {
                'text': 'How much ice is typically used in an Old Fashioned cocktail?',
                'options': ['None', 'Full', 'Half', 'As desired'],
                'answer': 'Full'
            },
            {
                'text': 'Which fruit is used to garnished an Old Fashioned cocktail?',
                'options': ['Lemon', 'Orange', 'Grapefruit', 'Lime'],
                'answer': 'Orange'
            }
        ]
    },
    2: {
        'questions': [
            {
                'text': 'What type of alcohol is used in Sex on the Beach?',
                'options': ['Vodka', 'Gin', 'Whiskey', 'Rum'],
                'answer': 'Vodka'
            },
            {
                'text': 'What is the suggested decoration in the preparation of Sex on the Beach?',
                'options': ['Watermelon', 'Sliced grapes', 'Cherry and orange slice', 'Cucumber stripes'],
                'answer': 'Cherry and orange slice'
            }
        ]
    },
    3: {
        'questions': [
            {
                'text': 'What is the primary alcoholic ingredient in a Classic Negroni?',
                'options': ['Vodka', 'Gin and tonic', 'Gin and Campari', 'Rum and Coke'],
                'answer': 'Gin and Campari'
            },
            {
                'text': 'What type of juice complements Campari in a Classic Negroni?',
                'options': ['Lemon Juice', 'Apple Juice', 'Orange Juice', 'Grapefruit Juice'],
                'answer': 'Orange Juice'
            },
            {
                'text': 'How many ice cubes are typically used in a Classic Negroni?',
                'options': ['A large ice sphere', 'half full class', 'full', 'None'],
                'answer': 'A large ice sphere'
            }
        ]
    },
    4: {
        'questions': [
            {
                'text': 'What is the main alcoholic ingredient used in Sangaria?',
                'options': ['Vodka', 'Rose Wine', 'Red Wine', 'White Wine'],
                'answer': 'Red Wine'
            },
            {
                'text': 'Which of the following steps is involved in preparing Sangaria?',
                'options': ['Freeze the mixture until solid', 'Blend all ingredients until smooth', 'Pour in the wine and brandy', 'Bake the ingredients for 10 minutes'],
                'answer': 'Pour in the wine and brandy'
            }
        ]
    },
    5: {
        'questions': [
            {
                'text': 'Which ingredient gives the Hot Toddy its sweet flavor?',
                'options': ['Sugar', 'Honey', 'Maple Syrup', 'Agave Nectar'],
                'answer': 'Honey'
            },
            {
                'text': 'What is the final step in the preparation of a Hot Toddy?',
                'options': ['Chill in the refrigerator', 'Lay down and relax', 'Serve over ice', 'Garnish with mint'],
                'answer': 'Lay down and relax'
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

@app.route('/match_quiz', methods=['GET'])
def match_quiz():
    # You can customize this data structure based on how you want to display images and names
    cocktails = [
        {"name": "Old Fashioned", "image": "learn8.jpeg"},
        {"name": "Sex on the Beach", "image": "learn7.jpeg"},
        {"name": "Classic Negroni", "image": "learn3.jpeg"},
        {"name": "Sangaria", "image": "learn4.jpeg"},
        {"name": "Hot Toddy", "image": "learn6.jpeg"}
    ]
    return render_template('match_quiz.html', cocktails=cocktails)

@app.route('/result')
def show_result():
    total_score = session.get('total_score', 0)
    session['total_score'] = 0  # Reset score if needed or handle differently depending on requirements
    return render_template('result.html', total_score=total_score)

if __name__ == "__main__":
    app.run(debug=True)
