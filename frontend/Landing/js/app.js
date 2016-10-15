$(document).ready(function () {
    init_bg();
    b();
    $(window).on("keydown", function (e) {
        var el = $("input:text").val();
        if (el.length != 0) {
            if (e.keyCode == 13) {
                if (~el.indexOf(" ")) {
                    $("#handle").removeClass("hide");
                } else {
                    !$("#handle").hasClass("hide") ? $("#handle").addClass("hide") : a();
                    //TODO: Ajax call
                }

            }
        }
    });
});
function b() {
    $("#bgImg").animate({"top":"-10000px"}, 200000, "linear");


    var scrollPosition = [ self.pageXOffset || document.documentElement.scrollLeft || document.body.scrollLeft,  self.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop];
    var html = jQuery('html');
    html.data('scroll-position', scrollPosition);
    html.data('previous-overflow', html.css('overflow'));
    html.css('overflow', 'hidden');
    window.scrollTo(scrollPosition[0], scrollPosition[1]);
}
function a() {
}
function init_bg() {
    $.ajax({
        url: "data/jh.json",
        dataType: "JSON",
        method: "GET",
        success: function (response) {
            response.forEach(function (data) {
                var el1 = $("#bgImg");
                ~data.indexOf("RT") ? el1.html(el1.html() + "<p class='item'><span class='glyphicon glyphicon-send'></span>" + data.replace("RT", '  ') + "</p><br/>") : el1.html(el1.html() + "<p class='item'>" + data + "</p><br/>");
            });
        }
    });
}