const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.mobile');
    const navLinks = document.querySelectorAll('.mobile li');
  
    burger.addEventListener('click', () => {
      //Toggle Nav
      nav.classList.toggle('nav-active');
  
      //Animate Links
      navLinks.forEach((link, index) => {
          if(link.style.animation) {
              link.style.animation = ''
          } else {
              link.style.animation = `navLinkFade ease forwards ${index / 10 + 0.15}s`;
          }
      });
      //Burger animation
      burger.classList.toggle('toggle');
  });
    
}
  
  
navSlide();
  