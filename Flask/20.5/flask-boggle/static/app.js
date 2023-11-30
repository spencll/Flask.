 let points = 0
 let time = 60
let guesses = []

//timer

function timer(){
const countdown = setInterval(() => {
  if (time===0){
    $('button').prop("disabled", true)
    score();
    clearInterval(countdown);
  }
  $('#time').text(time)
  time -=1 
}, 1000);
}

timer();

 async function submitGuess(e) {
  e.preventDefault();
  //getting server response
  const input= $('input').val()
  const res = await axios.get('/guess',{params: {input:input}});
  $('input').val('') 
  
  //checks validity
  if (res.data.result==='ok' && !guesses.includes(res.data.word)) {
    $('#guesses').append($('<li>', {text: input + ` `}))
    guesses.push(res.data.word)
    points += res.data.word.length
  }
  $('#score').text(points)
}
$('.guess').on('submit', submitGuess)

//stores high score to session via post 
async function score() {
  const curScore = parseInt($('#score').text())
  await axios.post('/score',{score: curScore})
}

