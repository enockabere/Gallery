$(document).ready(function(){
    $("#overs").show(function(){
      $("#overs").animate({
        width: "100%",
        opacity: 1,
        left: "50px",
        speed:"slow"
      }, 4000);
    });
  });
  $(window).load(function () {
    //normally you'd wait for document.ready, but you'd likely to want to wait
    //for images to load in case they reflow the page
    $('body').delay(5000) //wait 5 seconds
        .animate({
            //animate jQuery's custom "scrollTop" style
            //grab the value as the offset of #second from the top of the page
            'scrollTop': $('#second').offset().top
        }, 300); //animate over 300ms, change this to however long you want it to animate for
});