const navSlide = () => {
  const burger = document.querySelector('.burger');
  const nav = document.querySelector('.dropdown');
  const navLinks = document.querySelectorAll('.dropdown button');


  burger.addEventListener('click', () => {
    //Toggle Nav
    nav.classList.toggle('nav-active');

    //Animate Links
    navLinks.forEach((link, index) => {
        if(link.style.animation) {
            link.style.animation = ''
        } else {
            link.style.animation = `navLinkFade 0.5s ease forwards ${index / 10 + 0.2}s`;
        }
    });
    //Burger animation
    burger.classList.toggle('toggle');
    

});

}

navSlide();
