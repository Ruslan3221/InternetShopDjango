const shop = document.getElementById('shop');
const images = shop.querySelectorAll('.image-container');




images.forEach(image => {
  image.addEventListener('mouseenter', () => {
    image.querySelector('.image').style.opacity = '0.5';
    image.querySelector('.overlay').style.opacity = '1';
  });

  image.addEventListener('mouseleave', () => {
    image.querySelector('.image').style.opacity = '1';
    image.querySelector('.overlay').style.opacity = '0';
  });
});

function test(){
  alert("Work")
}


//details


function more(){
  const more_item = document.getElementById('overlay-details-item')
  const displayValue = window.getComputedStyle(more_item.querySelector('.overlay-details')).getPropertyValue('display');

  if (displayValue == 'block'){
    more_item.querySelector('.overlay-details').style.display = 'none';
  }
  else{
    more_item.querySelector('.overlay-details').style.display = 'block';
  }

}
