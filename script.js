async function checkPassword() {
    const password = document.getElementById("passwordInput").value;
    const resultBox = document.getElementById("resultBox");
    const strengthSpan = document.getElementById("strength");
    const entropySpan = document.getElementById("entropy");
    const suggestionsList = document.getElementById("suggestions");
    const meterBar = document.getElementById("meterBar");

    if (!password) {
        alert("Enter a password first!");
        return;
    }

    const response = await fetch("http://127.0.0.1:5000/check", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ password })
    });

    const data = await response.json();

    // Show box
    resultBox.classList.remove("hidden");

    // Update text values
    strengthSpan.innerText = data.strength;
    entropySpan.innerText = data.entropy_bits.toFixed(2);

    // Clear suggestions
    suggestionsList.innerHTML = "";
    data.suggestions.forEach(s => {
        let li = document.createElement("li");
        li.innerText = s;
        suggestionsList.appendChild(li);
    });

    // ⭐ Strength Meter Logic
    let score = data.score;  // assuming 0–4

    if (score === 0) {
        meterBar.style.width = "10%";
        meterBar.style.background = "red";
    } else if (score === 1) {
        meterBar.style.width = "30%";
        meterBar.style.background = "orange";
    } else if (score === 2) {
        meterBar.style.width = "60%";
        meterBar.style.background = "yellow";
    } else if (score === 3) {
        meterBar.style.width = "80%";
        meterBar.style.background = "#8fd400"; // lime green
    } else {
        meterBar.style.width = "100%";
        meterBar.style.background = "#00ff44"; // neon green
    }
}
