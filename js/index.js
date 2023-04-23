const registration = document.getElementById('registration')
const entrance = document.getElementById('entrance')
const registrationLink = document.getElementById('registration_link')
const entranceLink = document.getElementById('entrance_link')

registrationLink.addEventListener('click', function(){
    registration.style.display = 'none'
    entrance.style.display = 'block'
})

entranceLink.addEventListener('click', function(){
    entrance.style.display = 'none'
    registration.style.display = 'block'
})