// TODO: JOIN RANDOM FONT WITH INPUT DETECTION SO IT CHANGES FONT AFTER EVERY WORD
// To show a preview of each font in the checkboxes
document.querySelectorAll(".font-type").forEach((check) => {
  check.parentElement.classList.add(check.value, "preview-kana");
});

// Random font selector according to checked boxes
// (currently works with button, objective is for it to change when the word changes so it refreshes the new list)
const checked = document.querySelectorAll('input[type="checkbox"]:checked');

const btn = document.getElementById("submit-word");

function random(number) {
  return Math.floor(Math.random() * (number + 1));
}

btn.addEventListener("click", () => {
  const col = `rgb(${random(255)} ${random(255)} ${random(255)})`;
  const h = document.getElementById("show-word");
  h.style.color = col;
  const font = checked[random(checked.length)].value;
  h.className = font;
});

// Made to detect the input and change the word is it's correct
const test = [
  { hiragana: "いぬ", meaning: "inu" },
  { hiragana: "ねこ", meaning: "neko" },
  { hiragana: "みず", meaning: "mizu" },
  { hiragana: "やま", meaning: "yama" },
  { hiragana: "ひと", meaning: "hito" },
  { hiragana: "くるま", meaning: "kuruma" },
];

const liveIn = document.getElementById("answer");
// const pressed = document.createElement("div");
const show = document.getElementById("show-word");

show.innerHTML = test[0]["hiragana"];
let meaning = test[0]["meaning"];

// ans.after(pressed);
liveIn.addEventListener("input", (event) => {
  //  pressed.textContent = `pressed: "${event.key}"`;

  if (event.target.value == meaning) {
    console.log("True, changed");
    const ran = random(5);
    meaning = test[ran]["meaning"];
    show.innerHTML = test[ran]["hiragana"];

    event.target.value = "";
  } else {
    console.log("false");
  }
});
