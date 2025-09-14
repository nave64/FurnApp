/***************************************************
==================== JS INDEX ======================
****************************************************
01. PreLoader Js
02. Mobile Menu Js
03. Sidebar Js
04. Body overlay Js
05. Search Js
06. Sticky Header Js
07. Data CSS Js
08. Nice Select Js
09. slider__active Slider Js
10. product__sale-slider
11. product__item-slider
12. product__item-slider-2
13. product-slider-3
14. product__item-trending-slider
15. product__item-trending-slider-2
16. product__hot-slider
17. banner__slider-active
18. blog__slider
19. brand__slider
20. brand__slider-2
21. blog__slider-2
22. blog__slider-3
23. product__tb-slider
24. Masonary Js
25. magnificPopup img view
26. magnificPopup video view
27. Wow Js
28. Cart Quantity Js
29. Show Login Toggle Js
30. Show Coupon Toggle Js
31. Create An Account Toggle Js
32. Shipping Box Toggle Js
33. Parallax Js
34. InHover Active Js
35. Data Countdown Js
36. range slider activation

****************************************************/

(function ($) {
	"use strict";

	////////////////////////////////////////////////////
	// 01. Preloder Js
	// $(window).on('load',function() {
	// 	$("#loading").fadeOut(500);
	// });

	////////////////////////////////////////////////////
	// 02. Mobile Menu Js
	$(document).ready(function() {
		$('#mobile-menu').meanmenu({
			meanMenuContainer: '.mobile-menu',
			meanScreenWidth: "1199",
			meanExpand: ['<i class="fal fa-plus"></i>'],
		});
		$('#mobile-menu-2').meanmenu({
			meanMenuContainer: '.mobile-menu-2',
			meanScreenWidth: "1199",
			meanExpand: ['<i class="fal fa-plus"></i>'],
		});
	});

	////////////////////////////////////////////////////
	// 03. Sidebar Js
	$(".offcanvas-toggle-btn").on("click", function () {
		$(".offcanvas__area").addClass("opened");
		$(".body-overlay").addClass("opened");
	});
	$(".offcanvas__close-btn").on("click", function () {
		$(".offcanvas__area").removeClass("opened");
		$(".body-overlay").removeClass("opened");
	});

	////////////////////////////////////////////////////
	// 04. Body overlay Js
	$(".body-overlay").on("click", function () {
		$(".offcanvas__area").removeClass("opened");
		$(".body-overlay").removeClass("opened");
	});

	////////////////////////////////////////////////////
	// 05. Search Js
	$(".search-toggle").on("click", function () {
		$(".search__area").addClass("opened");
	});
	$(".search-close-btn").on("click", function () {
		$(".search__area").removeClass("opened");
	});

	////////////////////////////////////////////////////
	// 07. Data CSS Js
	$("[data-background]").each(function () {
		$(this).css("background-image", "url( " + $(this).attr("data-background") + "  )");
	});
	$("[data-width]").each(function () {
		$(this).css("width", $(this).attr("data-width"));
	});

	$("[data-bg-color]").each(function () {
        $(this).css("background-color", $(this).attr("data-bg-color"));
    });

	////////////////////////////////////////////////////
	// 08. Nice Select Js
	$('select').niceSelect();

	////////////////////////////////////////////////////
	// 09. slider__active Slider Js
	if (jQuery(".slider__active").length > 0) {
		let sliderActive1 = ".slider__active";
		let sliderInit1 = new Swiper(sliderActive1, {
			// Optional parameters
			slidesPerView: 1,
			slidesPerColumn: 1,
			paginationClickable: true,
			loop: true,
			effect: 'fade',

			autoplay: {
				delay: 5000,
			},


			// Navigation arrows
			navigation: {
				nextEl: ".main-slider-button-next",
				prevEl: ".main-slider-button-prev",
			},

			a11y: false,
		});

		function animated_swiper(selector, init) {
			let animated = function animated() {
				$(selector + " [data-animation]").each(function () {
					let anim = $(this).data("animation");
					let delay = $(this).data("delay");
					let duration = $(this).data("duration");

					$(this)
						.removeClass("anim" + anim)
						.addClass(anim + " animated")
						.css({
							webkitAnimationDelay: delay,
							animationDelay: delay,
							webkitAnimationDuration: duration,
							animationDuration: duration,
						})
						.one(
							"webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend",
							function () {
								$(this).removeClass(anim + " animated");
							}
						);
				});
			};
			animated();
			// Make animated when slide change
			init.on("slideChange", function () {
				$(sliderActive1 + " [data-animation]").removeClass("animated");
			});
			init.on("slideChange", animated);
		}

		animated_swiper(sliderActive1, sliderInit1);
	}
	var sliderr = new Swiper('.active-class', {
		slidesPerView: 1,
		spaceBetween: 30,
		loop: true,
		pagination: {
			el: ".testimonial-pagination-6",
			clickable: true,
			renderBullet: function (index, className) {
			  return '<span class="' + className + '">' + '<button>'+(index + 1)+'</button>' + "</span>";
			},
		},
		breakpoints: {
			'1200': {
				slidesPerView: 3,
			},
			'992': {
				slidesPerView: 2,
			},
			'768': {
				slidesPerView: 2,
			},
			'576': {
				slidesPerView: 1,
			},
			'0': {
				slidesPerView: 1,
			},
		},
	});

	///////////////////////////////////////////////////
	// 10. product__sale-slider
	$(".product__sale-slider").owlCarousel({
		//add owl carousel in activation class
		loop: true,
		margin: 0,
		items: 1,
		navText: ['<button class="nav-left"><i class="far fa-angle-left"></i></button>', '<button class="nav-right"><i class="far fa-angle-right"></i></button>'],
		nav: true,
		dots: false,
		responsive: {
			0: {
				items: 1
			},
			767: {
				items: 1
			},
			992: {
				items: 1
			},
			1200: {
				items: 1
			}
		}
	});

	///////////////////////////////////////////////////
	// 11. product__item-slider
	$(".product__item-slider").owlCarousel({
		//add owl carousel in activation class
		loop: true,
		margin: 28,
		items: 3,
		navText: ['<button class="nav-left"><i class="far fa-angle-left"></i></button>', '<button class="nav-right"><i class="far fa-angle-right"></i></button>'],
		nav: true,
		dots: true,
		responsive: {
			0: {
				items: 1
			},
			576: {
				items: 2
			},
			767: {
				items: 2
			},
			992: {
				items: 2
			},
			1200: {
				items: 3
			},
			1400: {
				items: 3
			}
		}
	});

	///////////////////////////////////////////////////
	// 12. product__item-slider-2
	$(".product__item-slider-2").owlCarousel({
		//add owl carousel in activation class
		loop: true,
		margin: 30,
		items: 2,
		navText: ['<button class="nav-left"><i class="far fa-angle-left"></i></button>', '<button class="nav-right"><i class="far fa-angle-right"></i></button>'],
		nav: true,
		dots: true,
		responsive: {
			0: {
				items: 1
			},
			576: {
				items: 1
			},
			767: {
				items: 2
			},
			992: {
				items: 1
			},
			1200: {
				items: 2
			},
			1400: {
				items: 2
			}
		}
	});

	///////////////////////////////////////////////////
	// 13. product-slider-3
	$(".product-slider-3").owlCarousel({
		//add owl carousel in activation class
		loop: true,
		margin: 30,
		items: 2,
		navText: ['<button class="nav-left"><i class="far fa-angle-left"></i></button>', '<button class="nav-right"><i class="far fa-angle-right"></i></button>'],
		nav: false,
		dots: true,
		responsive: {
			0: {
				items: 1
			},
			576: {
				items: 1
			},
			767: {
				items: 1
			},
			992: {
				items: 1
			},
			1200: {
				items: 1
			},
			1400: {
				items: 1
			}
		}
	});

	///////////////////////////////////////////////////
	// 14. product__item-trending-slider
	$(".product__item-trending-slider").owlCarousel({
		//add owl carousel in activation class
		loop: true,
		margin: 30,
		items: 3,
		navText: ['<button class="nav-left"><i class="far fa-angle-left"></i></button>', '<button class="nav-right"><i class="far fa-angle-right"></i></button>'],
		nav: true,
		dots: false,
		responsive: {
			0: {
				items: 1
			},
			767: {
				items: 3
			},
			992: {
				items: 4
			},
			1200: {
				items: 5
			}
		}
	});

	///////////////////////////////////////////////////
	// 15. product__item-trending-slider-2
	$(".product__item-trending-slider-2").owlCarousel({
		//add owl carousel in activation class
		loop: true,
		margin: 30,
		items: 3,
		navText: ['<button class="nav-left"><i class="far fa-angle-left"></i></button>', '<button class="nav-right"><i class="far fa-angle-right"></i></button>'],
		nav: false,
		dots: true,
		responsive: {
			0: {
				items: 1
			},
			767: {
				items: 3
			},
			992: {
				items: 4
			},
			1200: {
				items: 5
			}
		}
	});

	///////////////////////////////////////////////////
	// 16. product__hot-slider
	$(document).ready(function () {
  // Initialize Owl Carousel for the product__hot-slider
  var hotSlider = $(".product__hot-slider").owlCarousel({
    loop: true,
    margin: 30,
    items: 3,
    nav: false, // We're using custom buttons instead
    dots: false,
    rtl: true,  // For RTL support
    touchDrag: true,
    mouseDrag: true,
    pullDrag: true,
    freeDrag: false,
    responsive: {
      0: {
        items: 1
      },
      576: {
        items: 2
      },
      992: {
        items: 2
      },
      1200: {
        items: 3
      }
    }
  });

  // Bind custom navigation buttons
  $('.hot-slider-prev').on('click', function () {
    hotSlider.trigger('prev.owl.carousel');
  });

  $('.hot-slider-next').on('click', function () {
    hotSlider.trigger('next.owl.carousel');
  });

  // Enhanced touch handling for hot slider
  var hotSliderWrapper = $('.product__hot-slider-wrapper');
  var isDragging = false;
  var startY = 0;
  var startX = 0;

  // Prevent vertical scrolling during horizontal drag
  hotSliderWrapper.on('touchstart', function(e) {
    var touch = e.originalEvent.touches[0];
    startY = touch.clientY;
    startX = touch.clientX;
    isDragging = false;
  });

  hotSliderWrapper.on('touchmove', function(e) {
    if (!isDragging) {
      var touch = e.originalEvent.touches[0];
      var deltaY = Math.abs(touch.clientY - startY);
      var deltaX = Math.abs(touch.clientX - startX);
      
      // If horizontal movement is greater than vertical, prevent page scroll
      if (deltaX > deltaY) {
        isDragging = true;
        e.preventDefault();
        hotSliderWrapper.addClass('slider-dragging');
      }
    } else {
      e.preventDefault();
    }
  });

  hotSliderWrapper.on('touchend', function(e) {
    isDragging = false;
    hotSliderWrapper.removeClass('slider-dragging');
  });

  // Additional touch event handling
  hotSliderWrapper.on('touchcancel', function(e) {
    isDragging = false;
    hotSliderWrapper.removeClass('slider-dragging');
  });
});
	$(document).ready(function () {
  $('.furniture-slider').each(function () {
    const $slider = $(this);
    const totalItems = $slider.find('.furniture-product-card-wrapper').length;

    if (totalItems > 1) {
      // Initialize carousel if more than one
      $slider.owlCarousel({
        loop: true,
        margin: 15,
        rtl: true,
        nav: false,
        dots: false,
        items: 4,
        responsive: {
          0: { items: 2 },
          576: { items: 2 },
          768: { items: 3 },
          992: { items: 4 }
        }
      });
    } else {
      // For single product: add styling class & hide arrows
      $slider.addClass('single-item-slider');
      $slider.closest('.subcategory-products').find('.furniture-slider-nav').hide();
    }
  });

  // Tab switching logic
  $('.main-furniture-section').each(function () {
    const $section = $(this);
    const $buttons = $section.find('.furniture-category-btn');
    const $blocks = $section.find('.subcategory-products');

    $buttons.on('click', function () {
      const subcatId = $(this).data('subcategory');

      $buttons.removeClass('active');
      $(this).addClass('active');

      $blocks.addClass('d-none');
      $section.find('#' + subcatId).removeClass('d-none');
    });
  });

  // Arrows functionality
  $('.furniture-slider-prev').click(function () {
    const target = $(this).data('target');
    $(target).trigger('prev.owl.carousel');
  });

  $('.furniture-slider-next').click(function () {
    const target = $(this).data('target');
    $(target).trigger('next.owl.carousel');
  });
});

	// Initialize the trending slider
$('.trending-slider').owlCarousel({
  loop: true,
  margin: 15,
  rtl: true,
  nav: false,
  dots: false,
  items: 4,
  responsive: {
    0: { items: 2 },
    576: { items: 2 },
    768: { items: 3 },
    992: { items: 4 }
  }
});

// Custom arrow binding
$('.trending-slider-prev').click(function () {
  $('.trending-slider').trigger('prev.owl.carousel');
});

$('.trending-slider-next').click(function () {
  $('.trending-slider').trigger('next.owl.carousel');
});



  $(document).ready(function() {
    // Check if Select2 is available and element exists
    if (typeof $.fn.select2 !== 'undefined' && $('#product_id').length) {
      $('#product_id').select2({
        placeholder: 'انتخاب محصول...',
        allowClear: true
      });
    }
  });





	///////////////////////////////////////////////////
	// 17. banner__slider-active
	$(".banner__slider-active").owlCarousel({
		//add owl carousel in activation class
		loop: true,
		margin: 30,
		items: 3,
		navText: ['<button class="nav-left"><i class="far fa-angle-left"></i></button>', '<button class="nav-right"><i class="far fa-angle-right"></i></button>'],
		nav: true,
		dots: false,
		responsive: {
			0: {
				items: 1
			},
			767: {
				items: 1
			},
			992: {
				items: 1
			},
			1200: {
				items: 1
			}
		}
	});

	///////////////////////////////////////////////////
	// 18. blog__slider
	$(".blog__slider").owlCarousel({
		//add owl carousel in activation class
		loop: true,
		margin: 30,
		items: 3,
		navText: ['<button class="nav-left"><i class="far fa-angle-left"></i></button>', '<button class="nav-right"><i class="far fa-angle-right"></i></button>'],
		nav: true,
		dots: false,
		responsive: {
			0: {
				items: 1
			},
			767: {
				items: 2
			},
			992: {
				items: 2
			},
			1200: {
				items: 3
			}
		}
	});

	///////////////////////////////////////////////////
	// 19. brand__slider
	$(".brand__slider").owlCarousel({
		//add owl carousel in activation class
		loop: true,
		margin: 30,
		items: 3,
		navText: ['<button class="nav-left"><i class="far fa-angle-left"></i></button>', '<button class="nav-right"><i class="far fa-angle-right"></i></button>'],
		nav: true,
		dots: false,
		responsive: {
			0: {
				items: 2
			},
			767: {
				items: 2
			},
			992: {
				items: 3
			},
			1200: {
				items: 6
			}
		}
	});

	///////////////////////////////////////////////////
	// 20. brand__slider-2
	$(".brand__slider-2").owlCarousel({
		//add owl carousel in activation class
		loop: true,
		margin: 30,
		items: 3,
		navText: ['<button class="nav-left"><i class="far fa-angle-left"></i></button>', '<button class="nav-right"><i class="far fa-angle-right"></i></button>'],
		nav: false,
		dots: false,
		responsive: {
			0: {
				items: 2
			},
			767: {
				items: 4
			},
			992: {
				items: 5
			},
			1200: {
				items: 6
			}
		}
	});

	///////////////////////////////////////////////////
	// 21. blog__slider-2
	$(".blog__slider-2").owlCarousel({
		//add owl carousel in activation class
		loop: true,
		margin: 30,
		items: 3,
		navText: ['<button class="nav-left"><i class="far fa-angle-left"></i></button>', '<button class="nav-right"><i class="far fa-angle-right"></i></button>'],
		nav: true,
		dots: false,
		responsive: {
			0: {
				items: 1
			},
			767: {
				items: 2
			},
			992: {
				items: 2
			},
			1200: {
				items: 3
			}
		}
	});

	///////////////////////////////////////////////////
	// 22. blog__slider-3
	$(".blog__slider-3").owlCarousel({
		//add owl carousel in activation class
		loop: true,
		margin: 30,
		items: 3,
		navText: ['<button class="nav-left"><i class="far fa-angle-left"></i></button>', '<button class="nav-right"><i class="far fa-angle-right"></i></button>'],
		nav: true,
		dots: false,
		responsive: {
			0: {
				items: 1
			},
			767: {
				items: 2
			},
			992: {
				items: 2
			},
			1200: {
				items: 3
			}
		}
	});

	///////////////////////////////////////////////////
	// 23. product__tb-slider
	$(".product__tb-slider").owlCarousel({
		//add owl carousel in activation class
		loop: true,
		margin: 30,
		items: 3,
		navText: ['<button class="nav-left"><i class="far fa-angle-left"></i></button>', '<button class="nav-right"><i class="far fa-angle-right"></i></button>'],
		nav: true,
		dots: false,
		responsive: {
			0: {
				items: 1
			},
			767: {
				items: 3
			},
			992: {
				items: 4
			},
			1200: {
				items: 5
			}
		}
	});

	////////////////////////////////////////////////////
	// 24. Masonary Js
	$('.grid').imagesLoaded(function () {
		// init Isotope
		var $grid = $('.grid').isotope({
			itemSelector: '.grid-item',
			percentPosition: true,
			masonry: {
				// use outer width of grid-sizer for columnWidth
				columnWidth: '.grid-item',
			}
		});


		// filter items on button click
		$('.masonary-menu').on('click', 'button', function () {
			var filterValue = $(this).attr('data-filter');
			$grid.isotope({ filter: filterValue });
		});

		//for menu active class
		$('.masonary-menu button').on('click', function (event) {
			$(this).siblings('.active').removeClass('active');
			$(this).addClass('active');
			event.preventDefault();
		});

	});

	/*  25. magnificPopup img view */
	$('.popup-image').magnificPopup({
		type: 'image',
		gallery: {
			enabled: true
		}
	});

	/* 26. magnificPopup video view */
	$(".popup-video").magnificPopup({
		type: "iframe",
	});

	////////////////////////////////////////////////////
	// 27. Wow Js
	new WOW().init();

	////////////////////////////////////////////////////
	// 28. Cart Quantity Js
	$('.cart-minus').click(function () {
		var $input = $(this).parent().find('input');
		var count = parseInt($input.val()) - 1;
		count = count < 1 ? 1 : count;
		$input.val(count);
		$input.change();
		return false;
	});
	$('.cart-plus').click(function () {
		var $input = $(this).parent().find('input');
		$input.val(parseInt($input.val()) + 1);
		$input.change();
		return false;
	});

	$(".cart-plus-minus").append('<div class="dec qtybutton">-</div><div class="inc qtybutton">+</div>');
	$(".qtybutton").on("click", function () {
		var $button = $(this);
		var oldValue = $button.parent().find("input").val();
		if ($button.text() == "+") {
			var newVal = parseFloat(oldValue) + 1;
		} else {
			// Don't allow decrementing below zero
			if (oldValue > 0) {
				var newVal = parseFloat(oldValue) - 1;
			} else {
				newVal = 0;
			}
		}
		$button.parent().find("input").val(newVal);
	});

	////////////////////////////////////////////////////
	// 29. Show Login Toggle Js
	$('#showlogin').on('click', function () {
		$('#checkout-login').slideToggle(900);
	});

	////////////////////////////////////////////////////
	// 30. Show Coupon Toggle Js
	$('#showcoupon').on('click', function () {
		$('#checkout_coupon').slideToggle(900);
	});

	////////////////////////////////////////////////////
	// 31. Create An Account Toggle Js
	$('#cbox').on('click', function () {
		$('#cbox_info').slideToggle(900);
	});

	////////////////////////////////////////////////////
	// 32. Shipping Box Toggle Js
	$('#ship-box').on('click', function () {
		$('#ship-box-info').slideToggle(1000);
	});

	////////////////////////////////////////////////////
	// 33. Counter Js
	$('.counter').counterUp({
		delay: 10,
		time: 1000
	});

	////////////////////////////////////////////////////
	// 34. Parallax Js
	if ($('.scene').length > 0) {
		$('.scene').parallax({
			scalarX: 10.0,
			scalarY: 15.0,
		});
	};

	////////////////////////////////////////////////////
	// 35. InHover Active Js
	$('.hover__active').on('mouseenter', function () {
		$(this).addClass('active').parent().siblings().find('.hover__active').removeClass('active');
	});

	////////////////////////////////////////////////////
    // 36. Data Countdown Js
    $('[data-countdown]').each(function() {

        var $this = $(this),
            finalDate = $(this).data('countdown');

        $this.countdown(finalDate, function(event) {

            $this.html(event.strftime('<span class="cdown days"><span class="time-count">%-D</span> <p>روز</p></span> <span class="cdown hour"><span class="time-count">%-H</span> <p>ساعت</p></span> <span class="cdown minutes"><span class="time-count">%M</span> <p>دقیقه</p></span> <span class="cdown second"> <span><span class="time-count">%S</span> <p>ثانیه</p></span>'));

        });

    });

	////////////////////////////////////////////////////
    // 37. range slider activation
	if ($('#slider-range').length > 0) {
		
		$("#slider-range").slider({
		range: true,
		min: 0,
		max: 500,
		values: [75, 300],
		slide: function (event, ui) {
			$("#amount").val("$" + ui.values[0] + " - $" + ui.values[1]);
		},
		});
	}

document.querySelectorAll('.main-furniture-section').forEach((section) => {
  const buttons = section.querySelectorAll('.furniture-category-btn');
  const contentBlocks = section.querySelectorAll('.subcategory-products');

  buttons.forEach((btn) => {
    btn.addEventListener('click', function () {
      // Remove active state and hide all in this section only
      buttons.forEach(b => b.classList.remove('active'));
      contentBlocks.forEach(p => p.classList.add('d-none'));

      // Activate current button and show its content
      this.classList.add('active');
      const targetId = this.getAttribute('data-subcategory');
      const targetBlock = section.querySelector('#' + targetId);
      if (targetBlock) {
        targetBlock.classList.remove('d-none');
      }
    });
  });
});



        // This section will be handled by the DOM ready function below
		// customscripts
		//////////////////////////////////////////////////////
// Custom Furniture Products Rendering
//////////////////////////////////////////////////////
//////////////////////////////////////////////////////
// Custom Furniture Products Rendering (Safe version)
//////////////////////////////////////////////////////

// Declare only if not already defined
window.furnitureProducts = window.furnitureProducts || {
  l: [
    { name: "مبل ال کلاسیک", price: "۶٬۰۰۰٬۰۰۰ تومان", image: "/static/img/pexels-kamenczak-775219.jpg" },
    { name: "مبل ال مدرن", price: "۷٬۲۰۰٬۰۰۰ تومان", image: "/static/img/pexels-kamenczak-775219.jpg" },
    { name: "مبل ال ترک", price: "۸٬۴۰۰٬۰۰۰ تومان", image: "/static/img/pexels-kamenczak-775219.jpg" },
  ],
  chester: [
    { name: "مبل چستر طوسی", price: "۹٬۰۰۰٬۰۰۰ تومان", image: "/static/img/pexels-kamenczak-775219.jpg" },
    { name: "مبل چستر سبز", price: "۹٬۸۰۰٬۰۰۰ تومان", image: "/static/img/pexels-kamenczak-775219.jpg" },
    { name: "مبل چستر کلاسیک", price: "۱۰٬۵۰۰٬۰۰۰ تومان", image: "/static/img/pexels-kamenczak-775219.jpg" },
  ],
  royal: [
    { name: "مبل سلطنتی منبت‌کاری", price: "۱۲٬۰۰۰٬۰۰۰ تومان", image: "/static/img/pexels-kamenczak-775219.jpg" },
    { name: "مبل سلطنتی طلایی", price: "۱۳٬۵۰۰٬۰۰۰ تومان", image: "/static/img/pexels-kamenczak-775219.jpg" },
    { name: "مبل سلطنتی کلاسیک", price: "۱۱٬۷۰۰٬۰۰۰ تومان", image: "/static/img/pexels-kamenczak-775219.jpg" },
  ],
  relax: [
    { name: "مبل راحتی مینیمال", price: "۵٬۵۰۰٬۰۰۰ تومان", image: "/static/img/pexels-kamenczak-775219.jpg" },
    { name: "مبل راحتی اسپرت", price: "۶٬۲۰۰٬۰۰۰ تومان", image: "/static/img/pexels-kamenczak-775219.jpg" },
    { name: "مبل راحتی پارچه‌ای", price: "۵٬۹۰۰٬۰۰۰ تومان", image: "/static/img/pexels-kamenczak-775219.jpg" },
  ]
};
// trending_products

        $(document).ready(function(){
        $('.trending-slider').owlCarousel({
            loop: true,
            margin: 15,
            nav: true,
            rtl: true,
            responsive: {
                0: { items: 1 },
                576: { items: 2 },
                768: { items: 3 },
                1200: { items: 4 }
            }
        });
    });

// Check if function already exists and define it
if (typeof window.renderFurnitureProducts !== "function") {
  window.renderFurnitureProducts = function (container, subcategory) {
    // Safety check for container
    if (!container) return;
    
    const productsContainer = container.querySelector('.furniture-products');
    if (!productsContainer) return;

    // Safety check for furnitureProducts data
    if (!window.furnitureProducts || !window.furnitureProducts[subcategory]) {
      console.warn('Furniture products data not found for subcategory:', subcategory);
      return;
    }

    productsContainer.innerHTML = '';
    window.furnitureProducts[subcategory].forEach(product => {
      productsContainer.innerHTML += `
        <div class="col-12 col-sm-6 col-md-4">
          <div class="furniture-product-card">
            <img src="${product.image}" alt="${product.name}" class="furniture-product-image">
            <div class="furniture-product-name">${product.name}</div>
            <div class="furniture-product-price">${product.price}</div>
            <button class="furniture-detail-btn">جزئیات</button>
          </div>
        </div>
      `;
    });
  };
}

// DOM Ready hook - Handle furniture sections
$(document).ready(function () {
  // Only run if renderFurnitureProducts function exists
  if (typeof window.renderFurnitureProducts === "function") {
    document.querySelectorAll('[data-section]').forEach(section => {
      const tabs = section.querySelectorAll('.furniture-category-btn');
      
      // Default render for 'l' category
      if (tabs.length > 0) {
        renderFurnitureProducts(section, 'l');
      }

      tabs.forEach(btn => {
        btn.addEventListener('click', () => {
          tabs.forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          const subcategory = btn.getAttribute('data-subcategory');
          renderFurnitureProducts(section, subcategory);
        });
      });
    });
  }
});

})(jQuery);
function addProductToOrder(productId) {
    const productCount = $('#product-count').val();

    $.get('/order/add-to-order?product_id=' + productId + '&count=' + productCount).then(res => {
        if (res.status === 'success') {
            // Success dialog with two buttons
            Swal.fire({
                title: 'اعلان',
                text: res.text,
                icon: res.icon,
                showCancelButton: true,
                confirmButtonText: 'مشاهده سبد خرید',
                cancelButtonText: 'تایید',
                confirmButtonColor: '#ff8429',
                cancelButtonColor: '#3085d6'
            }).then((result) => {
                if (result.isConfirmed) {
                    // Go to cart page
                    window.location.href = '/user-panel/user-basket';
                }
                // If cancelled, just close the dialog (no action needed)
            });
            
            // Update cart badge after successful add to cart
            if (typeof window.updateCartCount === 'function') {
                window.updateCartCount();
            }
        } else if (res.status === 'not_auth') {
            // Authentication required dialog
            Swal.fire({
                title: 'اعلان',
                text: res.text,
                icon: res.icon,
                showCancelButton: false,
                confirmButtonColor: '#3085d6',
                confirmButtonText: res.confirm_button_text
            }).then((result) => {
                if (result.isConfirmed) {
                    window.location.href = '/login';
                }
            });
        } else {
            // Error dialog
            Swal.fire({
                title: 'اعلان',
                text: res.text,
                icon: res.icon,
                showCancelButton: false,
                confirmButtonColor: '#d33',
                confirmButtonText: 'تایید'
            });
        }
    });
}

// Cart quantity functions moved to user_basket.html template for AJAX functionality



