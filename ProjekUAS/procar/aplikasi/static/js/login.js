document.addEventListener('DOMContentLoaded', function () {
  // Get the login form
  const loginForm = document.getElementById('login-form');

  // Add event listener to the form submission
  loginForm.addEventListener('submit', function (event) {
    // Prevent the default form submission
    event.preventDefault();

    // Get the email and password values from the form
    const email = document.getElementById('id_email').value;
    const password = document.getElementById('id_password').value;

    // Perform client-side validation if needed

    // Send the login request to the server using fetch API
    fetch('/login/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken'),
      },
      body: JSON.stringify({
        email: email,
        password: password,
      }),
    })
      .then((response) => {
        // Check if the response is OK
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        // If response is OK, redirect to the home page
        window.location.href = '/home';
      })
      .catch((error) => {
        // Handle errors here
        console.error('Error:', error);
      });
  });
});

// Function to get the value of a cookie by name
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Check if the cookie name matches the provided name
      if (cookie.substring(0, name.length + 1) === name + '=') {
        // Extract and return the cookie value
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
