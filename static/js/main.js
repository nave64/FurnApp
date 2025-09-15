// Simple debounce utility
function debounce(fn, wait) {
  let t;
  return function() {
    clearTimeout(t);
    const ctx = this, args = arguments;
    t = setTimeout(function(){ fn.apply(ctx, args); }, wait);
  };
}
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
		margin: 5,
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
  // Function to calculate optimal number of items based on container width
  function calculateItems() {
    const container = $(".product__hot-slider");
    const containerWidth = container.width();
    const itemWidth = 200; // Fixed item width (min-width from CSS)
    const margin = 15; // Fixed margin between items
    const minItems = 1; // Minimum items to show
    const maxItems = 5; // Maximum items to show
    
    // Calculate how many items can fit
    let items = Math.floor((containerWidth + margin) / (itemWidth + margin));
    
    // Ensure items are within bounds
    items = Math.max(minItems, Math.min(maxItems, items));
    
    return items;
  }

  // Initialize Owl Carousel for the product__hot-slider
  var hotSlider = $(".product__hot-slider").owlCarousel({
    loop: true,
    margin: 15,
    items: calculateItems(),
    nav: false, // We're using custom buttons instead
    dots: false,
    rtl: true,  // For RTL support
    responsive: false // Disable responsive to use our dynamic calculation
  });

  // Update items count on window resize
  $(window).on('resize', function() {
    const newItems = calculateItems();
    hotSlider.trigger('destroy.owl.carousel');
    hotSlider.owlCarousel({
      loop: true,
      margin: 15,
      items: newItems,
      nav: false,
      dots: false,
      rtl: true,
      responsive: false
    });
  });

  // Bind custom navigation buttons
  $('.hot-slider-prev').on('click', function () {
    hotSlider.trigger('prev.owl.carousel');
  });

  $('.hot-slider-next').on('click', function () {
    hotSlider.trigger('next.owl.carousel');
  });
});
	$(document).ready(function () {
  // Function to calculate dynamic gap based on screen width
  function calculateFurnitureGap() {
    const screenWidth = $(window).width();
    let gap = 8; // Base gap (current minimum)
    
    if (screenWidth >= 1200) {
      gap = 22; // Large screens
    } else if (screenWidth >= 992) {
      gap = 16; // Medium-large screens
    } else if (screenWidth >= 768) {
      gap = 12; // Medium screens
    } else if (screenWidth >= 576) {
      gap = 8; // Small-medium screens
    }
    // For screens < 576px, keep base gap of 8
    
    return gap;
  }

  // Function to get current breakpoint
  function getCurrentBreakpoint() {
    const screenWidth = $(window).width();
    if (screenWidth >= 1200) return 'xl';
    if (screenWidth >= 992) return 'lg';
    if (screenWidth >= 768) return 'md';
    if (screenWidth >= 576) return 'sm';
    return 'xs';
  }

  // Track current breakpoint for each slider
  const sliderBreakpoints = new Map();

  $('.furniture-slider').each(function () {
    const $slider = $(this);
    const totalItems = $slider.find('.furniture-product-card-wrapper').length;
    const currentBreakpoint = getCurrentBreakpoint();
    sliderBreakpoints.set($slider[0], currentBreakpoint);

    if (totalItems > 1) {
      // Pre-duplicate items to ensure a long stage so items don't "appear" late with autoWidth
      (function ensureLongStage() {
        const $baseItems = $slider.children('.furniture-product-card-wrapper').not('.fc-clone');
        if ($baseItems.length === 0) return;
        const containerWidth = $slider.width();
        const currentGap = calculateFurnitureGap();
        // Approximate item+gap width (matches CSS/JS config)
        const unitWidth = 192 + currentGap; // item width + dynamic margin
        let totalApprox = $slider.children('.furniture-product-card-wrapper').length * unitWidth;
        let repeats = 0;
        // Ensure at least ~3x container width worth of items present
        while (totalApprox < containerWidth * 2.5 && repeats < 5) {
          $baseItems.clone().addClass('fc-clone').appendTo($slider);
          totalApprox += $baseItems.length * unitWidth;
          repeats++;
        }
      })();

      // Initialize carousel if more than one
      $slider.owlCarousel({
        loop: true, // seamless carousel feel
        margin: calculateFurnitureGap(), // dynamic gap between items
        rtl: true,
        nav: false,
        dots: false,
        autoWidth: true, // allow partial items; width from item elements
        slideBy: 1,
        smartSpeed: 250, // Faster animation for mobile
        dragEndSpeed: 250, // Faster drag end for mobile
        responsiveRefreshRate: 150, // More responsive on mobile
        checkVisible: false,
        lazyLoad: true, // Enable lazy loading for images
        lazyLoadEager: 1, // Load 1 item ahead of visible area
        // Mobile-specific optimizations
        touchDrag: true, // Enable touch dragging
        mouseDrag: true, // Enable mouse dragging
        pullDrag: true, // Allow pulling to drag
        freeDrag: false, // Disable free drag for better control
        // Touch performance optimizations
        touchClass: 'owl-touch', // Custom touch class
        grabClass: 'owl-grab', // Custom grab class
        // Mobile-specific speed settings
        slideTransition: 'ease-out', // Smoother transition
        animateOut: false, // Disable animate out for performance
        animateIn: false, // Disable animate in for performance
        // Callbacks with mobile optimizations
        onInitialized: debounce(function(e){ $(e.target).trigger('refresh.owl.carousel'); }, 100),
        onResized: debounce(function(e){ $(e.target).trigger('refresh.owl.carousel'); }, 150),
        // Mobile touch event optimizations
        onDrag: function() {
          // Disable text selection during drag for smoother experience
          $('body').addClass('slider-dragging');
        },
        onDragged: function() {
          // Re-enable text selection after drag
          $('body').removeClass('slider-dragging');
        }
      });
    } else {
      // For single product: add styling class & hide arrows
      $slider.addClass('single-item-slider');
      $slider.closest('.subcategory-products').find('.furniture-slider-nav').hide();
    }
  });

  // Update gap only when breakpoint changes
  $(window).on('resize', function() {
    $('.furniture-slider.owl-carousel').each(function() {
      const $slider = $(this);
      const newBreakpoint = getCurrentBreakpoint();
      const currentBreakpoint = sliderBreakpoints.get($slider[0]);
      
      // Only update if breakpoint actually changed
      if (newBreakpoint !== currentBreakpoint) {
        sliderBreakpoints.set($slider[0], newBreakpoint);
        const newGap = calculateFurnitureGap();
        
        // Update the margin in the carousel
        $slider.trigger('destroy.owl.carousel');
        $slider.owlCarousel({
          loop: true,
          margin: newGap,
          rtl: true,
          nav: false,
          dots: false,
          autoWidth: true,
          slideBy: 1,
          smartSpeed: 250,
          dragEndSpeed: 250,
          responsiveRefreshRate: 150,
          checkVisible: false,
          lazyLoad: true,
          lazyLoadEager: 1,
          touchDrag: true,
          mouseDrag: true,
          pullDrag: true,
          freeDrag: false,
          touchClass: 'owl-touch',
          grabClass: 'owl-grab',
          slideTransition: 'ease-out',
          animateOut: false,
          animateIn: false,
          onInitialized: debounce(function(e){ $(e.target).trigger('refresh.owl.carousel'); }, 100),
          onResized: debounce(function(e){ $(e.target).trigger('refresh.owl.carousel'); }, 150),
          onDrag: function() {
            $('body').addClass('slider-dragging');
          },
          onDragged: function() {
            $('body').removeClass('slider-dragging');
          }
        });
      }
    });
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

      // Ensure Owl recalculates widths when a previously hidden slider becomes visible
      const $visibleSlider = $section.find('#' + subcatId + ' .furniture-slider.owl-carousel');
      if ($visibleSlider.length) {
        setTimeout(function () {
          $visibleSlider.trigger('refresh.owl.carousel');
        }, 0);
      }
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

// Refresh after all assets load to avoid incorrect autoWidth measurements
$(window).on('load', function () {
  $('.furniture-slider.owl-carousel').each(function () {
    debounce(function(){ $('.furniture-slider.owl-carousel').trigger('refresh.owl.carousel'); }, 150)();
  });
});

// Mobile-specific furniture slider optimizations
$(document).ready(function() {
  // Detect mobile devices
  const isMobile = /Android|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
  
  if (isMobile) {
    // Add mobile-specific classes for better touch handling
    $('.furniture-slider').addClass('mobile-slider');
    
    // Optimize touch events for mobile
    $('.furniture-slider').on('touchstart', function(e) {
      // Prevent default touch behaviors that might interfere
      e.preventDefault();
    }, { passive: false });
    
    // Add momentum scrolling for iOS
    $('.furniture-slider .owl-stage-outer').css({
      '-webkit-overflow-scrolling': 'touch',
      'overflow': 'hidden'
    });
    
    // Optimize for mobile performance
    $('.furniture-slider').each(function() {
      const $slider = $(this);
      
      // Reduce animation complexity on mobile
      $slider.find('.owl-item').css({
        'transform': 'translate3d(0, 0, 0)',
        'backface-visibility': 'hidden',
        '-webkit-backface-visibility': 'hidden'
      });
    });
  }
  
  // Add touch feedback for better UX
  $('.furniture-product-card').on('touchstart', function() {
    $(this).addClass('touch-active');
  });
  
  $('.furniture-product-card').on('touchend touchcancel', function() {
    $(this).removeClass('touch-active');
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




