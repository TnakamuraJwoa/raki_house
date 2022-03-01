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