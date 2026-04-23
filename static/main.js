const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) entry.target.classList.add('visible');
  });
}, { threshold: 0.12 });

document.querySelectorAll(
  '.skill-card, .project-featured, .edu-item, .mini-card, .about-left, .about-right, .section-title'
).forEach(el => { el.classList.add('reveal'); observer.observe(el); });

const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav-links a[href^="#"]');
window.addEventListener('scroll', () => {
  let current = '';
  sections.forEach(s => { if (window.scrollY >= s.offsetTop - 120) current = s.id; });
  navLinks.forEach(link => {
    link.style.color = link.getAttribute('href') === '#' + current ? 'var(--text)' : '';
  });
});
