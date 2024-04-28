//her lager jeg referanser til HTML koden og setter opp event listeners.
document.addEventListener('DOMContentLoaded', function() {
    const itemList = document.getElementById('itemList');
    const itemInput = document.getElementById('itemInput');
    const addItemBtn = document.getElementById('addItemBtn');

    // Her henter jeg ting fra local storage ved bruk av json.parse
    const savedItems = JSON.parse(localStorage.getItem('items')) || [];
    savedItems.forEach(item => addItem(item));

    // denne funksjonen legger til ting når jeg klikker på "legg til" og oppdaterer local storage, sånn at tingene ikke kommer tilbake når man refresher siden.
    function addItem(text) {
        const li = document.createElement('li');
        const span = document.createElement('span');
        span.textContent = text;
        const removeButton = document.createElement('button');
        removeButton.textContent = 'Remove';
        removeButton.addEventListener('click', function() {
            li.remove();
            updateLocalStorage();
        });
        li.appendChild(span);
        li.appendChild(removeButton);
        itemList.appendChild(li);
        updateLocalStorage();
    }

    // Her bruker jeg event listener for å legge til knappen som gjør at du kan legge ting til i handlelisten din.
    addItemBtn.addEventListener('click', function() {
        const itemText = itemInput.value.trim();
        if (itemText !== '') {
            addItem(itemText);
            itemInput.value = '';
        }
    });

    // Her bruker jeg event listeners for å finne ut om du presser enter, som da legger til det du har skrevet i tekst boksen.
    itemInput.addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            addItemBtn.click();
        }
    });

    // Her oppdaterer jeg local storage
    function updateLocalStorage() {
        const items = [];
        itemList.querySelectorAll('span').forEach(span => items.push(span.textContent));
        localStorage.setItem('items', JSON.stringify(items));
    }
});
