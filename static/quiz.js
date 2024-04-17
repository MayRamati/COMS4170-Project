let answers = {};
let total_score = 0;

function loadQuiz() {
    displayQuiz(quizData);
}

function displayQuiz(quiz) {
    const container = document.getElementById('quiz-container');
    container.innerHTML = '';

    quiz.questions.forEach((question, index) => {
        const questionElem = document.createElement('div');
        questionElem.classList.add('question');
        const questionText = document.createElement('p');
        questionText.textContent = question.text;
        questionElem.appendChild(questionText);

        question.options.forEach(option => {
            const optionButton = document.createElement('button');
            optionButton.textContent = option;
            optionButton.classList.add('option');
            optionButton.onclick = function() {
                answers[index] = option;
                let buttons = questionElem.getElementsByClassName('option');
                for (let btn of buttons) {
                    btn.classList.remove('selected');
                }
                this.classList.add('selected');
                this.disabled = false;
            };
            questionElem.appendChild(optionButton);
        });

        container.appendChild(questionElem);
    });
}

function submitQuiz() {
    let score = 0;
    quizData.questions.forEach((question, index) => {
        if (answers[index] === question.answer) {
            score += 1;
        }
    });
    fetch(`/quiz/${quiz_id}/score`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({score: score})
    }).then(response => response.json())
        .then(data => {
            console.log('Score submission response:', data);
        }).catch(error => {
        console.error('Error submitting score:', error);
    });

    document.getElementById('result').textContent = `Your score: ${score}/${quizData.questions.length}`;
}
window.onload = loadQuiz;
