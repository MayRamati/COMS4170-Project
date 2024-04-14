function submitQuiz() {
    // Send a GET request to the server to retrieve the quiz result
    fetch(`/quiz/{{ quiz_id }}`)
    .then(response => response.json())
    .then(data => {
        console.log(data);
        const resultMessage = `You scored ${data.result} out of ${data.total}`;
        document.getElementById('quizResult').innerText = resultMessage;
            window.location.href = `/quiz/${data.next_quiz_id}`;

    })
    .catch(error => {
        console.error('Error:', error);
        alert('Failed to retrieve the quiz result.');
    });
}
