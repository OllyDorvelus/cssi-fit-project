$(document).ready(function() {
  $('#searchtext').animate(
      {fontSize: 24},
      1500
  );

// $(".find").animate({width:'toggle'},350);

$(".find").hide();
$(".find").slideToggle(1000);

$(".create").hide();
$(".create").slideToggle(1000);

$("#txt").hide();
$("#txt").slideDown(1000);


	$('.cloud').jqFloat({
		width: 100,
		height: 100,
		speed: 5000
	});

  // $('#createimage').jqFloat({
	// 	width: 100,
	// 	height: 100,
	// 	speed: 1000
	// });

});
