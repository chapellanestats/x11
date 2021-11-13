const navSlide = () => {
    const burger = document.querySelector('#main-toggle');
    const nav = document.querySelector('nav');
    const navLinks = document.querySelectorAll('.home, li .toggle')
    
  
    burger.addEventListener('click', () => {
      //Toggle Nav
      nav.classList.toggle('nav-active');
  
      //Animate Links
      navLinks.forEach((link, index) => {
          if(link.style.animation) {
              link.style.animation = ''
          } else {
              link.style.animation = `navLinkFade ease forwards ${index / 10 + 0.3}s`;
          }    
      });
      
      //Burger animation
      burger.classList.toggle('toggle');
  });
    
}
  
  
navSlide();
  