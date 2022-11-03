const catButton = document.getElementById('js-new-cat');
catButton.addEventListener("click", showCatImage);
let image = document.getElementById('catImage');

const endpoint = 'https://cataas.com/cat/cute';

async function showCatImage() {
    image.src="https://cataas.com/cat/cute";    
}
