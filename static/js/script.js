const form = document.getElementById('contactForm');

form.addEventListener('submit', async (e) => {
    e.preventDefault(); // Prevent page reload

    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());

    try {
        const response = await fetch('/submit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();
        alert(result.message); // Show alert after successful submission
        form.reset(); // Clear the form
    } catch (error) {
        alert('Error submitting form. Please try again.');
    }
});


function sendValue(val) {
    // Redirect to Flask route with value as query parameter
    window.location.href = '/receive?value=' + val;
    
  }