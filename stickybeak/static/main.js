// <!-- CODE ADAPTED FROM: https://github.com/bedimcode/portfolio-responsive-complete/blob/master/index.html -->

// SHOW THE MENU SQARE MENU ON SMALL WINDOWS
const showMenu = (toggleId, navId) =>{
    const toggle = document.getElementById(toggleId),
    nav = document.getElementById(navId)
    
    // Validate that variables exist
    if(toggle && nav){
        toggle.addEventListener('click', ()=>{
            nav.classList.toggle('show-menu')
        })
    }
}
showMenu('nav-toggle','nav-menu')

// REMOVE MENU ON MOBILE
const navLink = document.querySelectorAll('.nav_link')

function linkAction(){
    const navMenu = document.getElementById('nav-menu')
    // When we click on each nav__link, we remove the show-menu class
    navMenu.classList.remove('show-menu')
}
navLink.forEach(n => n.addEventListener('click', linkAction))

// ACTIVE LINK DOT BELOW NAVIGATION BAR
const sections = document.querySelectorAll('section[id]')

function scrollActive(){
    const scrollY = window.pageYOffset

    sections.forEach(current =>{
        const sectionHeight = current.offsetHeight
        const sectionTop = current.offsetTop - 50;
        sectionId = current.getAttribute('id')

        if(scrollY > sectionTop && scrollY <= sectionTop + sectionHeight){
            document.querySelector('.nav_menu a[href*=' + sectionId + ']').classList.add('active-link')
        }else{
            document.querySelector('.nav_menu a[href*=' + sectionId + ']').classList.remove('active-link')
        }
    })
}
window.addEventListener('scroll', scrollActive)

// CHANGE BACKGROUND HEADER
function scrollHeader(){
    const nav = document.getElementById('header')
    // When the scroll is greater than 200 viewport height, add the scroll-header class to the header tag
    if(this.scrollY >= 200) nav.classList.add('scroll-header'); else nav.classList.remove('scroll-header')
}
window.addEventListener('scroll', scrollHeader)

// REVEALS ON SCROLL ANIMATIONS
const sr = ScrollReveal({
    distance: '30px',
    duration: 1800,
    reset: true,
});

sr.reveal(`.home_data, .home_img, 
           .audience_data,
           .footer__content, .footer__content`, {
    origin: 'top',
    interval: 200,
})

sr.reveal(`.story_img, .newsletter_content,
          .grid__checker, .grid__information,
          .grid__identify`, {
    origin: 'left'
})

sr.reveal(`.story_data, .newsletter_img,
          .grid__curve, .grid__source,
          .grid__educate`, {
    origin: 'right'
    
})
