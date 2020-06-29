//обработчик
jQuery(document).ready(function () {
    jQuery("#jquery-accordion-menu").jqueryAccordionMenu();

});
//активный класс
$(function () {
    $("#list-menu li").click(function () {
        $("#list-menu li.active").removeClass("active");
        $(this).addClass("active");
    })
});

$(function () {
    $("#list-menu li a").click(function (event) {
        event.preventDefault();
        alert(event.target);
        // event.preventDefault();

        $.ajax({
            url: event.target,
            // url: '/category' + "/" + target.value + "/",
            // dataType: 'html',
            // type: 'get',
            // data: 'div:[class="content"]',
            // data: $('div[class="content"]'),
            // async: false,
            // dataType: "html",
            // target.name + "/" + target.value + "/",
            // '/category/0/',
            // event.target,
            
            success: function (data) {
                // alert(data)
                // console.log(data);
                // $('.content2').html(data,'.content2');
                // .find('.need_you').html());
                // $('.content2').html($(data).filter('.content2'));

                // var el = $(data).find('div.content2');
                // $('.content2').html(el);
                
                // var el = $(data).filter('.content2');
                // $('.content2').append(el);

                var el = $(data).filter('.content2');
                $('.content2').html(el);

            }
            event.preventDefault();
        });
        // return false;
        // event.preventDefault();
    })
});

// window.onload = function () {
//    console.log("загрузили DOM");
    // $("#list-menu li").on("clik", "a", function (event) {
//        console.log(event.target);
        // alert(event);
        // var target = event.target;        
//         $.ajax({
//             url: "/basket/update/" + target.name + "/" + target.value + "/",
//             success: function (data) {
// //                console.log(data);
//                 $('.basket-list').html(data.result);
//             }
//         });
    // });
// }


//поисковая строка
$(function ($) {
    $.expr[":"].Contains = function (a, i, m) {
        return (a.textContent || a.innerText || "").toUpperCase().indexOf(m[3].toUpperCase()) >= 0;
    };
    function filterList(header, list) {
        var form = $("<form>").attr({
            "class": "filterform",
            action: "#"
        }), input = $("<input>").attr({
            "class": "filterinput",
            type: "text"
        });
        $(form).append(input).appendTo(header);
        $(input).change(function () {
            var filter = $(this).val();
            if (filter) {
                $matches = $(list).find("a:Contains(" + filter + ")").parent();
                $("li", list).not($matches).slideUp();
                $matches.slideDown();
            } else {
                $(list).find("li").slideDown();
            }
            return false;
        }).keyup(function () {
            $(this).change();
        });
    }
    $(function () {
        filterList($("#form"), $("#list-menu"));
    });
});

