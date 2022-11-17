const aliceTumbling = [
  { transform: "rotate(0) scale(1)" },
  { transform: "rotate(360deg) scale(0)" },
];

const aliceTiming = {
  duration: 2000,
  iterations: 1,
  fill: "forwards",
};

const alice1 = document.querySelector("#alice1");
const alice2 = document.querySelector("#alice2");
const alice3 = document.querySelector("#alice3");

alice1.animate(aliceTumbling, aliceTiming).finished
  .then(() => alice2.animate(aliceTumbling, aliceTiming).finished)
  .then(() => alice3.animate(aliceTumbling, aliceTiming).finished)

//async function() {
  //var animate1 = alice1.animate(aliceTumbling, aliceTiming);
  //await animate1.finished;
  //var animate2 = alice2.animate(aliceTumbling, aliceTiming);
  //await animate2.finished;
  //var animate3 = alice3.animate(aliceTumbling, aliceTiming);
  //
animate();

