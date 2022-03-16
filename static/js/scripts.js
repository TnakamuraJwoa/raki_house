/*!
* Start Bootstrap - One Page Wonder v6.0.4 (https://startbootstrap.com/theme/one-page-wonder)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-one-page-wonder/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project


$(function(){

    $('.js-modal-open').on('click',function(){
        $('.js-modal').fadeIn();
        return false;
    });

    $('.js-modal-close').on('click',function(){
        $('.js-modal').fadeOut();
        return false;
    });

    $('.js-modal-people-open').on('click',function(){
        $('.js-modal-people').fadeIn();
        return false;
    });

    $('.js-modal-people-close').on('click',function(){
        var person = $('#id_person').val();
        var kids1 = $('#id_kids1').val();
        var kids2 = $('#id_kids2').val();
        var kids3 = $('#id_kids3').val();
        var kids4 = $('#id_kids4').val();
        var serch_txt = "";

        if (person >= 1) {
            $('#hid-person').val(person);
            serch_txt += person + "名"
        }
        if (kids1 >= 1) {
//            $('#hid-kids1').val(kids1);
            serch_txt += ", A:" + kids1 + "名"
        }
        if (kids2 >= 1) {
//            $('#hid-kids2').val(kids2);
            serch_txt += ", B:" + kids2 + "名"
        }
        if (kids3 >= 1) {
//            $('#hid-kids3').val(kids3);
            serch_txt += ", C:" + kids3 + "名"
        }
        if (kids4 >= 1) {
//            $('#hid-kids4').val(kids4);
            serch_txt += ", D:" + kids4 + "名"
        }

        $('#serch-box-person').val(serch_txt);
        $('.js-modal-people').fadeOut();
        return false;
    });


    $('.slider').slick({
      autoplay: false,//自動的に動き出すか。初期値はfalse。
      infinite: true,//スライドをループさせるかどうか。初期値はtrue。
      slidesToShow: 1,//スライドを画面に3枚見せる
      slidesToScroll: 1,//1回のスクロールで3枚の写真を移動して見せる
      prevArrow: '<div class="slick-prev"></div>',//矢印部分PreviewのHTMLを変更
      nextArrow: '<div class="slick-next"></div>',//矢印部分NextのHTMLを変更
      dots: true,//下部ドットナビゲーションの表示
      responsive: [
        {
        breakpoint: 769,//モニターの横幅が769px以下の見せ方
        settings: {
          slidesToShow: 1,//スライドを画面に2枚見せる
          slidesToScroll: 1,//1回のスクロールで2枚の写真を移動して見せる
        }
      },
      {
        breakpoint: 426,//モニターの横幅が426px以下の見せ方
        settings: {
          slidesToShow: 1,//スライドを画面に1枚見せる
          slidesToScroll: 1,//1回のスクロールで1枚の写真を移動して見せる
        }
      }
    ]
    });
});