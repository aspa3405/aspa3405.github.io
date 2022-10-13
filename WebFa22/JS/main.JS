const customName = document.getElementById('customname');
const randomize = document.querySelector('.randomize');
const story = document.querySelector('.story');

function randomValueFromArray(array){
  const random = Math.floor(Math.random()*array.length);
  return array[random];
}
//variables//

let storytext = "It was 94 fahrenheit outside, so :insertx: and Bob and went to the store to get fresh basil to make caprese salad for a refreshing meal on a hot day. When they got to :inserty:, all they had were the live plants of basil and unfortunately, :insertx: kills plants at the blink of an eye. Bob was about to make the yummy dish, but was not surprised when a few seconds later — :insertz: from simply being in :insertx:'s presence... oops:/  So instead, they ordered 40 pizzas, ate them all and now they both weigh 300 pounds."

let insertX = ["Snoop Dog","Devin Booker",    
"Adam Levine"];

let insertY = ["the farmers market",
"Disneyland gift store",
"Trader Joes"];

let insertZ = ["the plant was deceased",
"it had turned into a sunflower",
"**BOOM!!!!** it exploded"];

//functions//

randomize.addEventListener('click', result);

function result() {
    newStory = storytext;
    let xItem = randomValueFromArray(insertX);
    let yItem = randomValueFromArray(insertY);
    let zItem = randomValueFromArray(insertZ);
    newStory = newStory.replaceAll(':insertx:',xItem);
    newStory = newStory.replaceAll(':inserty:',yItem);
    newStory = newStory.replaceAll(':insertz:',zItem);
  if(customName.value !== '') {
    const name = customName.value;
    newStory = newStory.replaceAll('Bob',name);
  }

  if(document.getElementById("uk").checked) {
    const weight = Math.round((300 * 0.0714286)*5/9) + ' stone';
    const temperature =  Math.round(94 - 32) + ' centigrade';
    newStory = newStory.replaceAll('94 fahrenheit',temperature);
    newStory = newStory.replaceAll('300 pounds', weight);
  }

  story.textContent = newStory;
  story.style.visibility = 'visible';
}