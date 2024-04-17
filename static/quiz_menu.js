document.addEventListener('DOMContentLoaded', function () {
    const learning = [
        {
            id: 1,
            name: 'Old Fashioned',
            image_url: 'static/img/learn8.jpeg'
        },
        {
            id: 2,
            name: 'Sex on the Beach',
            image_url: 'static/img/learn7.jpeg'
        },
        {
            id: 3,
            name: 'Classic Negroni',
            image_url: 'static/img/learn3.jpeg'
        },
        {
            id: 4,
            name: 'Sangaria',
            image_url: 'static/img/learn4.jpeg'
        },
        {
            id: 5,
            name: 'Hot Toddy',
            image_url: 'static/img/learn6.jpeg'
        }
    ];

    const learningContainer = document.querySelector('.row');

    learning.forEach(item => {
        const cardDiv = document.createElement('div');
        cardDiv.classList.add('col-md-4', 'mb-4');

        const cardLink = document.createElement('a');
        cardLink.href = `/quiz/${item.id}`;
        cardLink.classList.add('card-link');

        const card = document.createElement('div');
        card.classList.add('card');

        const img = document.createElement('img');
        img.src = item.image_url;
        img.alt = item.name;
        img.classList.add('card-img-top');

        const cardBody = document.createElement('div');
        cardBody.classList.add('card-body');

        const title = document.createElement('h5');
        title.classList.add('card-title');
        title.textContent = item.name;

        cardBody.appendChild(title);

        card.appendChild(img);
        card.appendChild(cardBody);

        cardLink.appendChild(card);
        cardDiv.appendChild(cardLink);

        learningContainer.appendChild(cardDiv);
    });
});
