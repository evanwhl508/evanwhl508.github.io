// A view preference only. No persistence, ranking, selection or studio-logo changes.
const grid = document.querySelector('.concept-grid');
document.querySelectorAll('input[name="palette"]').forEach(input => {
  input.addEventListener('change', () => {
    grid.dataset.palette = input.value;
    grid.querySelectorAll('img[data-concept]').forEach(img => {
      img.src = `${img.dataset.concept}/mark-${input.value}.svg`;
    });
  });
});
