function generateHashedURL() {
    var longUrl = document.getElementById("longUrlInput").value;
    fetch('http://127.0.0.1:5000/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ long_url: longUrl }),
    })
    .then(response => response.json())
    .then(data => {
        var encodedLinkElement = document.getElementById("encodedLink");
        encodedLinkElement.innerHTML = `<a href="${data.hashed_url}" target="_blank">${data.hashed_url}</a>`;

        var expirationInfoElement = document.getElementById("expirationInfo");
        expirationInfoElement.innerText = `Expires in 24 hours`;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
