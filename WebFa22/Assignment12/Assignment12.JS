const canvas = document.querySelector('canvas');

var randomInt = Math.floor(Math.random() * 1000000000 + 1);

const yesButton = document.querySelector('.yes-button').addEventListener('click', yes);
const noButton = document.querySelector('.no-button').addEventListener('click', no);
const output = document.querySelector('.output');

function random(){
    outputInt = randomNumber(1000000000,9999999999);
    output.textContent = outputInt;
}

function randomNumber(min,max) {
    const num = Math.floor(Math.random() * (max - min + 1)) + min;
    return num;
}

function yes() {
    alert(output.textContent + "  This is someones phone number but it sure aint yours...  Please try again");
    random();
}

function no(){
    outputInt = randomNumber(1000000000,9999999999);
    output.textContent = outputInt;
}
