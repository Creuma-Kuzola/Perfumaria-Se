const quotes = [ 
    
    {
        img: '20201031_140502~2.jpg',
        name: 'Creuma Matias',
        quote: 'Tem um conceito completamente diferente das perfumarias convencionais e creio que seja por isso que tem se destacado e cumprido com o seu propósito'
    },
    {
        img: 'tahiti-spears-Me-MSv_dUNU-unsplash.jpg',
        name: 'Ana Emanuela',
        quote: 'Sou uma mulher mais segura graças a Sê e ao seu propósito. Recomendo! '
    },
    
    {
        img: 'logan-weaver-yRpe13BHdKw-unsplash.jpg',
        name: 'Suzete Lukeny',
        quote: 'Eu gostei tanto de estudar fazer comprar na Sê porque os funcionarários eram super pacientes e profissionais. E queriam que eu escolhesse exatamente o perfume de que realmente gosto'
    }
]


let quoteIndex = 0;
const basePictureUrl = './img/'
const quoteCircles = document.querySelectorAll('.div-fifth-section-description-div-circles--item')
setInterval(() => {
    quoteCircles[quoteIndex].classList.add('active-item-quote')
    console.log(quotes[quoteIndex])
    renderQuote(quotes[quoteIndex])

    if(quoteIndex==0) {
        quoteCircles[2].classList.remove('active-item-quote')
    }
    else if(quoteIndex!=0)
    {
        quoteCircles[quoteIndex-1].classList.remove('active-item-quote')
    }

    if(quoteIndex == 2){
        quoteIndex = 0;
    } else {
        quoteIndex++;
    }

    

}, 3000)

function renderQuote(quote){

    imagem = document.querySelector('.div-fifth-section-description-img')
    imagem.src =`${basePictureUrl}${quote.img}`

    document.querySelector('.div-fifth-section-description-p-name').innerText = quote.name
    document.querySelector('.div-fifth-section-description-p-description').innerText = quote.quote
}


