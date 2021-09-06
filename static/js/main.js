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
  var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
  var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl)
  })