// To show a preview of each font in the checkboxes
document.querySelectorAll(".font-type").forEach((check) => {
  check.parentElement.classList.add(check.value, "preview-kana");
});

// Random font selector according to checked boxes

function random(number) {
  return Math.floor(Math.random() * number);
}

function randomFont() {
  const checked = document.querySelectorAll('input[type="checkbox"]:checked');
  const showbox = document.getElementById("show-word");
  const font = checked[random(checked.length)].value;
  showbox.className = font;
  return font;
}

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
    const ran = random(5);
    meaning = test[ran]["meaning"];
    show.innerHTML = test[ran]["hiragana"];
    f = randomFont();
    console.log(`New word ${test[ran]["hiragana"]} and ${f}`);

    event.target.value = "";
  } else {
    console.log("False");
  }
});
