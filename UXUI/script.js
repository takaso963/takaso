const menuTitle = document.getElementById("menu-title");
const currentImage = document.getElementById("current-image");
const nextButton = document.getElementById("next-button");

// スライドに表示するデータ
const slides = [
  { title: "今日のメニュー", image: "hiiragi1.jpg" },
  { title: "本日のパン", image: "bread.jpg" }
];

let currentSlide = 0;

nextButton.addEventListener("click", () => {
  currentSlide = (currentSlide + 1) % slides.length; // 次のスライドへ
  menuTitle.textContent = slides[currentSlide].title;
  currentImage.src = slides[currentSlide].image;
});

