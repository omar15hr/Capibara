document.addEventListener('DOMContentLoaded', (event) => {
  const countSpan = document.getElementById('count');
  const decrementBtn = document.getElementById('decrementBtn');
  const incrementBtn = document.getElementById('incrementBtn');

  let count = 0;

  function updateCount() {
      countSpan.textContent = count;
      decrementBtn.disabled = count <= 0;
  }

  incrementBtn.addEventListener('click', () => {
      count++;
      updateCount();
  });

  decrementBtn.addEventListener('click', () => {
      if (count > 0) {
          count--;
      }
      updateCount();
  });

  // Initial update to set the initial state of the buttons
  updateCount();
});
