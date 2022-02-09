var frase = {}
let quotes = []
let quoteIndex = 0;
const basePictureUrl = '/static/./img/'
const quoteCircles = document.querySelectorAll('.div-fifth-section-description-div-circles--item')

fetch('http://127.0.0.1:5000/testemunhosdosclientes/get/testemunhos')
.then(res => res.json())
.then(data => {
    
    for(var i=0;i<=5; i++)
    {
        var j = 3;
        frase = { img: data.result[i][j], name: data.result[i][j-1],quote: data.result[i][j-2]}
        quotes[i] = frase;
    }
    console.log('quotes', quotes)
})
.catch(error => {
    console.log('erro')
    console.log(error)
})

setInterval(() => {
    quoteCircles[quoteIndex].classList.add('active-item-quote')
    console.log(quotes[quoteIndex])
    renderQuote(quotes[quoteIndex])

    if (quoteIndex == 0) {
        quoteCircles[5].classList.remove('active-item-quote')
    } else if (quoteIndex != 0) {
        quoteCircles[quoteIndex - 1].classList.remove('active-item-quote')
    }

    if (quoteIndex == 5) {
        quoteIndex = 0;
    } else {
        quoteIndex++;
    }

}, 3000)

function renderQuote(quote) {

    imagem = document.querySelector('.div-fifth-section-description-img')
    imagem.src = `${basePictureUrl}${quote.img}`

    document.querySelector('.div-fifth-section-description-p-name').innerText = quote.name
    document.querySelector('.div-fifth-section-description-p-description').innerText = quote.quote
}