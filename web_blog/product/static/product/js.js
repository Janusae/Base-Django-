//filter products
var $mediaElements = $(".cd-item");
$(".filter_link").click(function(e) {
  e.preventDefault();
  var filterVal = $(this).data("filter");
  if (filterVal === "all") {
    $mediaElements.slideDown("slow");
  } else {
    $mediaElements
      .hide("slow")
      .filter("." + filterVal)
      .slideDown("slow");
  }
});
//filter products