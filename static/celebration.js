const emojis = ["🎊", "🎉", "🎁", "🎁", "🎁", "🌟", "✨"]; // Add more emojis as needed
const maxBalloons = 20; // Maximum number of balloons allowed
const maxDuration = 10000; // Maximum duration in milliseconds (e.g., 60 seconds)

let elapsedTime = 0;
let balloonInterval;

document.addEventListener("DOMContentLoaded", function() {
    balloonInterval = setInterval(createBalloon, 120); // Initial interval
    setTimeout(() => {
        clearInterval(balloonInterval); // Clear the interval after maxDuration
    }, maxDuration);
});

function createBalloon() {
    if (document.querySelectorAll('.balloon').length < maxBalloons) {
        const balloon = document.createElement("div");
        balloon.classList.add("balloon");
        const randomEmoji = emojis[Math.floor(Math.random() * emojis.length)];
        balloon.innerHTML = randomEmoji;
        document.body.appendChild(balloon);

        const randomX = Math.random() * window.innerWidth;
        const randomY = Math.random() * window.innerHeight;

        balloon.style.left = `${randomX}px`;
        balloon.style.top = `${randomY}px`;

        setTimeout(() => {
            balloon.remove();
        }, 2000); // Adjust the time for how long each balloon should stay visible
    }
}
