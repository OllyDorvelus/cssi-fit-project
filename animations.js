$(document).ready(function() {
  $('#searchtext').animate(
      {fontSize: 24},
      1500
  );


  $("#tip2").hide();
  $('#tip3').hide();
  $("#tip4").hide();
  $('#tip5').hide();
  $("#tip6").hide();
  $('#tip7').hide();
  $("#tip8").hide();
  $('#tip9').hide();
  $("#tip10").hide();

$(".find").animate({width:'toggle'},350);
  $("#tip1").click(function() {
    $("#tip1").hide();
    $("#tip2").fadeIn(1000);

});
  $('#tip2').click(function() {
    $('#tip2').hide();
    $("#tip3").fadeIn(1000);
  });

  $("#tip3").click(function() {
    $("#tip3").hide();
    $("#tip4").fadeIn(1000);

});
  $('#tip4').click(function() {
    $('#tip4').hide();
    $("#tip5").fadeIn(1000);
  });

  $("#tip5").click(function() {
    $("#tip5").hide();
    $("#tip6").fadeIn(1000);

});

$("#tip6").click(function() {
  $("#tip6").hide();
  $("#tip7").fadeIn(1000);

});


  $("#tip7").click(function() {
    $("#tip7").hide();
    $("#tip8").fadeIn(1000);

});
  $('#tip8').click(function() {
    $('#tip8').hide();
    $("#tip9").fadeIn(1000);
  });

  $("#tip9").click(function() {
    $("#tip9").hide();
    $("#tip10").fadeIn(1000);

});
  $('#tip10').click(function() {
    $('#tip10').hide();
    $("#tip1").fadeIn(1000);
  });


$(".find").hide();
$(".find").slideToggle(1000);

$(".create").hide();
$(".create").slideToggle(1000);

$("#txt").hide();
$("#txt").slideDown(1000);
$('.make').hide();
$('.make').fadeIn(2000);

	$('.cloud').jqFloat({
		width: 100,
		height: 100,
		speed: 5000
	});

  // var currentPosition = 0;
  // var slideWidth = 500;
  // var slides = $('.slide');
  // var numberOfSlides = slides.length;
  // var slideShowInterval;
  // var speed = 3000;
  //
  //
  // slideShowInterval = setInterval(changePosition, speed);
  //
  // slides.wrapAll('<div id="slidesHolder"></div>')
  //
  // slides.css({ 'float' : 'left' });
  //
  // $('#slidesHolder').css('width', slideWidth * numberOfSlides);
  //
  //
  // function changePosition() {
  //   if(currentPosition == numberOfSlides - 1) {
  //     currentPosition = 0;
  //   } else {
  //     currentPosition++;
  //   }
  //   moveSlide();
  // }
  //
  //
  // function moveSlide() {
  //     $('#slidesHolder')
  //       .animate({'marginLeft' : slideWidth*(-currentPosition)});
  // }


  // $('#createimage').jqFloat({
	// 	width: 100,
	// 	height: 100,
	// 	speed: 1000
	// });

});
