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

function test(){
    alert("test")
  };


function alread(){
    var divElement = document.getElementById('img-conteiner');

    var imgTags = divElement.getElementsByTagName('img');


    for (var i =0;i< imgTags.length;i++){


    var a = window.getComputedStyle(imgTags[i]).getPropertyValue('display');

    if (a == 'block'){
        return parseInt(i);
    }
}


}

function photo(){
    var divEl = document.getElementById('img-conteiner');

    var imgtag = divEl.getElementsByTagName("img");



    var imglen = imgtag.length;

    var just_block = alread()


    if (just_block == imglen-1){
        var just = imgtag[0];
        just.style.display = 'block';
        imgtag[just_block].style.display = 'none';

    }
    else{
        imgtag[just_block].style.display = 'none';
        imgtag[just_block+1].style.display = 'block';

    }



}

