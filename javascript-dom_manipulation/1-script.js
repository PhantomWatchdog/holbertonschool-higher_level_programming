document.addEventListener('DOMContentLoaded', function() {
  const header = document.querySelector('#red_header');
  header.addEventListener('click', function() {
    header.style.color = '#FF0000';
  });
});
