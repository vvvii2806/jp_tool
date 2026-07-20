// const show = document.getElementById("show-word");
// const n = document.createElement("div");
// n.textContent = "ola";
// show.after(n);

//for answer detection
const ans = document.getElementById("answer");
const pressed = document.createElement("div");
ans.after(pressed);
ans.addEventListener("keydown", (event) => {
  pressed.textContent = `pressed: "${event.key}"`;
});

document.querySelectorAll(".font-type").forEach((check) => {
  check.parentElement.classList.add(check.value, "preview-kana");
});

// font changer with randomizer (currently works with button, objective is for it to change when word is changed so it gets the new list of checked fonts)
const show = document.getElementById("show-word");
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
