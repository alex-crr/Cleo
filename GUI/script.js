function sendInput() {
    const inputField = document.getElementById('inputField');
    const chatHistory = document.getElementById('chatHistory');

    const userMessage = inputField.value;
    if (userMessage) {
        // Display the user message immediately
        chatHistory.innerHTML += `<div class="user-message">${userMessage}</div>`;
        inputField.value = ''; // Clear the input field
        chatHistory.scrollTop = chatHistory.scrollHeight; // Scroll to the bottom

        // Call the API and wait for the response
        pywebview.api.handle_input(userMessage).then(response => {
            chatHistory.innerHTML += response;
            chatHistory.scrollTop = chatHistory.scrollHeight; // Scroll to the bottom
        });
    }
}

// Add event listener for the Enter key
document.getElementById('inputField').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        sendInput();  // Call sendInput function when Enter is pressed
    }
});
