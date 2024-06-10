// static/js/registration.js

function validatePasswords() {
  var password1 = document.getElementById('id_password1').value;
  var password2 = document.getElementById('id_password2').value;
  var errorDiv = document.getElementById('password-error');

  // Remove existing error message, if any
  if (errorDiv) {
    errorDiv.remove();
  }

  if (password1 !== password2) {
    // Create error message
    errorDiv = document.createElement('div');
    errorDiv.id = 'password-error';
    errorDiv.classList.add('alert', 'alert-danger');
    var errorMessage = document.createTextNode('Passwords do not match!');
    errorDiv.appendChild(errorMessage);

    // Append error message to the parent element of the password2 field
    document.getElementById('id_password2').parentNode.appendChild(errorDiv);

    return false; // Prevent form submission
  }

  // Display success message if passwords match
  alert('Registration successful!');

  return true; // Allow form submission
}
