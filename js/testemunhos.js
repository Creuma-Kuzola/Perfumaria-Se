const quotes = [ 
    
    {
        img: '20201031_140502~2.jpg',
        name: 'Creuma Matias',
        quote: 'Escolher LIG  como a minha escola de condução foi a melhor escolha, e hoje tenho a minha habilitação na mão'
    },
    {
        img: 'tahiti-spears-Me-MSv_dUNU-unsplash.jpg',
        name: 'Ana Emanuela',
        quote: 'Uma escola excelente em todos os sentidos, desde as condições de ensino até aos entusiasmados funcionários. Recomendo '
    },
    
    {
        img: 'logan-weaver-yRpe13BHdKw-unsplash.jpg',
        name: 'Suzete Lukeny',
        quote: 'Eu gostei tanto de estudar na LIG porque os meus professores eram super pacientes e profissionais.'
    },
    {
        img: 'tahiti-spears-Me-MSv_dUNU-unsplash.jpg',
        name: 'Rosied Dekgado',
        quote: 'Uma escola excelente em todos os sentidos, desde as condições de ensino até aos entusiasmados funcionários. Recomendo '
    },
    
    {
        img: 'logan-weaver-yRpe13BHdKw-unsplash.jpg',
        name: 'Catarina Lisica',
        quote: 'Eu gostei tanto de estudar na LIG porque os meus professores eram super pacientes e profissionais.'
    },
    
    {
        img: 'logan-weaver-yRpe13BHdKw-unsplash.jpg',
        name: 'Maria Pedro',
        quote: 'Eu gostei tanto de estudar na LIG porque os meus professores eram super pacientes e profissionais.'
    }
]


let quoteIndex = 0;
const basePictureUrl = '/img/'
const quoteCircles = document.querySelectorAll('.div-fifth-section-description-div-circles--item')
setInterval(() => {
    quoteCircles[quoteIndex].classList.add('active-item-quote')
    console.log(quotes[quoteIndex])
    renderQuote(quotes[quoteIndex])

    if(quoteIndex==0) {
        quoteCircles[5].classList.remove('active-item-quote')
    }
    else if(quoteIndex!=0)
    {
        quoteCircles[quoteIndex-1].classList.remove('active-item-quote')
    }

    if(quoteIndex == 5){
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