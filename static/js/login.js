document.getElementById('loginForm').addEventListener('submit', async function(event) {
    event.preventDefault(); // Prevent page reload

    let formData = new FormData(this);

    let response = await fetch("/login", {
        method: "POST",
        body: formData
    });

    let data = await response.json();

    if (data.error) {
        document.getElementById('error-message').innerText = data.error;
    } else {
        alert("Login successful! Frontend is connected to Flask backend.");
    }
});
