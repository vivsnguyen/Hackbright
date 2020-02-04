"use strict";

/******* Functions & Event Handlers *******/

function changeColor() {
  const colorChangeEls = $('.color-change');

  for (const el of colorChangeEls) {
    $(el).toggleClass('red');
  }

  // Or you can do all of the above on one line --
  // $('.color-change').each(el => el.toggleClass('red'));
}

function validateNumber(e) {
  e.preventDefault();

  const numberInput = $('input[name="number"]');
  const userNum = parseInt(numberInput.val(), 10);  // typecast to num

  const formFeedback = $('#formFeedback');
  if (!userNum || userNum > 10) {
    formFeedback.text('Please enter a smaller number');
  } else {
    formFeedback.text('You are good to go!');
  }
}


/******* Attach event handlers *******/

$('.color-changer').on('click', changeColor);
$('.number-form').on('submit', validateNumber);

