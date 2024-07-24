document.addEventListener('DOMContentLoaded', function() {
  const helloElement = document.getElementById('hello');

  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())
    .then(data => {
      helloElement.textContent = data.hello;
    })
    .catch(error => {
      console.log('An error occurred:', error);
    });
});
