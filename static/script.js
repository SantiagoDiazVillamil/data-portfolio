function toggleMenu() {
  document.getElementById("sidebar").classList.toggle("active");
}

// Animaciones al hacer scroll
const sections = document.querySelectorAll('.section');
const revealSections = () => {
  const trigger = window.innerHeight * 0.85;
  sections.forEach(sec => {
    const top = sec.getBoundingClientRect().top;
    if (top < trigger) sec.classList.add('visible');
  });
};
window.addEventListener('scroll', revealSections);
window.addEventListener('load', revealSections);
