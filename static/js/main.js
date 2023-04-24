document.addEventListener('DOMContentLoaded', () => {
    const inputText = document.getElementById('input-text');
    const outputText = document.getElementById('output-text');
    const submitBtn = document.getElementById('submit-btn');
    const clearBtn = document.getElementById('clear-btn');

    submitBtn.addEventListener('click', async () => {
        const prompt = inputText.value.trim();

        if (!prompt) {
            alert('Please enter a prompt.');
            return;
        }

        const formData = new FormData();
        formData.append('prompt', prompt);

        const response = await fetch('/chat', {
            method: 'POST',
            body: formData,
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
        });

        const data = await response.json();

        if (data.success) {
            outputText.value = data.message;
        } else {
            outputText.value = 'Error: ' + data.message;
        }
    });

    clearBtn.addEventListener('click', async () => {
        inputText.value = '';
        outputText.value = '';
    });
});
