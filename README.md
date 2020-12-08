index.html
{% load static %}
<!DOCTYPE html>
<html lang="en">
	<head>
		<title>Hot Tours</title>
		<meta charset="utf-8">
		<meta name="format-detection" content="telephone=no" />
		<link rel="icon" href="{% static 'images/favicon.ico' %}">
		<link rel="shortcut icon" href="{% static 'images/favicon.ico' %}" />
		<link rel="stylesheet" href="{% static 'css/style.css' %}">
		<script src="{% static 'js/jquery.js' %}"></script>
		<script src="{% static 'js/jquery-migrate-1.2.1.js' %}"></script>
		<script src="{% static 'js/script.js' %}"></script>
		<script src="{% static 'js/superfish.js' %}"></script>
		<script src="{% static 'js/jquery.ui.totop.js' %}"></script>
		<script src="{% static 'js/jquery.equalheights.js' %}"></script>
		<script src="{% static 'js/jquery.mobilemenu.js' %}"></script>
		<script src="{% static 'js/jquery.easing.1.3.js' %}"></script>
		<script>
		$(document).ready(function(){
			$().UItoTop({ easingType: 'easeOutQuart' });
		});
		</script>
		<!--[if lt IE 8]>
		<div style=' clear: both; text-align:center; position: relative;'>
			<a href="http://windows.microsoft.com/en-US/internet-explorer/products/ie/home?ocid=ie6_countdown_bannercode">
				<img src="http://storage.ie6countdown.com/assets/100/images/banners/warning_bar_0000_us.jpg" border="0" height="42" width="820" alt="You are using an outdated browser. For a faster, safer browsing experience, upgrade for free today." />
			</a>
		</div>
		<![endif]-->
		<!--[if lt IE 9]>
		<script src="js/html5shiv.js"></script>
		<link rel="stylesheet" media="screen" href="css/ie.css">
		<![endif]-->
	</head>
	<body>
<!--==============================header=================================-->
		<header>
			<div class="container_12">
				<div class="grid_12">
					<div class="menu_block">
						<nav class="horizontal-nav full-width horizontalNav-notprocessed">
							<ul class="sf-menu">
								<li><a href="{% url 'index' %}">ABOUT</a></li>
								<li class="current"><a href="{% url 'indexa' %}">HOT TOURS</a></li>
								<li><a href="{% url 'indexb' %}">SPECIAL OFFERS</a></li>
								<li><a href="{% url 'indexc' %}">BLOG</a></li>
								<li><a href="{% url 'indexd' %}">CONTACTS</a></li>
							</ul>
						</nav>
						<div class="clear"></div>
					</div>
				</div>
				<div class="grid_12">
					<h1>
						<a href="{% url 'index' %}">
							<img src="{% static 'images/logo.png' %}" alt="Your Happy Family">
						</a>
					</h1>
				</div>
			</div>
		</header>
<!--==============================Content=================================-->
		<div class="content"><div class="ic">More Website Templates @ TemplateMonster.com - February 10, 2014!</div>
			<div class="container_12">
				<div class="banners">
					<div class="grid_4">
						<div class="banner">
							<img src="{% static 'images/page2_img1.jpg' %}" alt="">
							<div class="label">
								<div class="title">NEW ZEALAND</div>
								<div class="price">from<span>$ 1.200</span></div>
								<a href="#">LEARN MORE</a>
							</div>
						</div>
					</div>
					<div class="grid_4">
						<div class="banner">
							<img src="{% static 'images/page2_img2.jpg' %}" alt="">
							<div class="label">
								<div class="title">GOA</div>
								<div class="price">from<span>$ 1.500</span></div>
								<a href="#">LEARN MORE</a>
							</div>
						</div>
					</div>
					<div class="grid_4">
						<div class="banner">
							<img src="{% static 'images/page2_img3.jpg' %}" alt="">
							<div class="label">
								<div class="title">FRANCE</div>
								<div class="price">from<span>$ 1.600</span></div>
								<a href="#">LEARN MORE</a>
							</div>
						</div>
					</div>
					<div class="clear"></div>
					<div class="grid_4">
						<div class="banner">
							<img src="{% static 'images/page2_img4.jpg' %}" alt="">
							<div class="label">
								<div class="title">CANADA</div>
								<div class="price">from<span>$ 2000</span></div>
								<a href="#">LEARN MORE</a>
							</div>
						</div>
					</div>
					<div class="grid_4">
						<div class="banner">
							<img src="{% static 'images/page2_img5.jpg' %}" alt="">
							<div class="label">
								<div class="title">TURKEY</div>
								<div class="price">from<span>$ 1.500</span></div>
								<a href="#">LEARN MORE</a>
							</div>
						</div>
					</div>
					<div class="grid_4">
						<div class="banner">
							<img src="{% static 'images/page2_img6.jpg' %}" alt="">
							<div class="label">
								<div class="title">EGYPT</div>
								<div class="price">from<span>$ 1.500</span></div>
								<a href="#">LEARN MORE</a>
							</div>
						</div>
					</div>
					<div class="clear"></div>
					<div class="grid_4">
						<div class="banner">
							<img src="{% static 'images/page2_img7.jpg' %}" alt="">
							<div class="label">
								<div class="title">JAPAN</div>
								<div class="price">from<span>$ 1000</span></div>
								<a href="#">LEARN MORE</a>
							</div>
						</div>
					</div>
					<div class="grid_4">
						<div class="banner">
							<img src="{% static 'images/page2_img8.jpg' %}" alt="">
							<div class="label">
								<div class="title">BRAZIL</div>
								<div class="price">from<span>$ 1.700</span></div>
								<a href="#">LEARN MORE</a>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
<!--==============================footer=================================-->
		<footer>
			<div class="container_12">
				<div class="grid_12">
					<div class="socials">
						<a href="#" class="fa fa-facebook"></a>
						<a href="#" class="fa fa-twitter"></a>
						<a href="#" class="fa fa-google-plus"></a>
					</div>
					<div class="copy">
						Your Trip (c) 2014 | <a href="#">Privacy Policy</a> | Website Template Designed by TemplateMonster.com
					</div>
				</div>
			</div>
		</footer>
		<script>
		$(function (){
			$('#bookingForm').bookingForm({
				ownerEmail: '#'
			});
		})
		</script>
	</body>
</html>
{% load static %}
<!DOCTYPE html>
<html lang="en">
	<head>
		<title>Special Offers</title>
		<meta charset="utf-8">
		<meta name="format-detection" content="telephone=no" />
		<link rel="icon" href="{% static 'images/favicon.ico' %}">
		<link rel="shortcut icon" href="{% static 'images/favicon.ico' %}" />
		<link rel="stylesheet" href="{% static 'css/style.css' %}">
		<script src="{% static 'js/jquery.js' %}"></script>
		<script src="{% static 'js/jquery-migrate-1.2.1.js' %}"></script>
		<script src="{% static 'js/script.js' %}"></script>
		<script src="{% static 'js/superfish.js' %}"></script>
		<script src="{% static 'js/jquery.ui.totop.js' %}"></script>
		<script src="{% static 'js/jquery.equalheights.js' %}"></script>
		<script src="{% static 'js/jquery.mobilemenu.js' %}"></script>
		<script src="{% static 'js/jquery.easing.1.3.js' %}"></script>
		<script>
		$(document).ready(function(){
			$().UItoTop({ easingType: 'easeOutQuart' });
			});
		</script>
		<!--[if lt IE 8]>
		<div style=' clear: both; text-align:center; position: relative;'>
			<a href="http://windows.microsoft.com/en-US/internet-explorer/products/ie/home?ocid=ie6_countdown_bannercode">
				<img src="http://storage.ie6countdown.com/assets/100/images/banners/warning_bar_0000_us.jpg" border="0" height="42" width="820" alt="You are using an outdated browser. For a faster, safer browsing experience, upgrade for free today." />
			</a>
		</div>
		<![endif]-->
		<!--[if lt IE 9]>
		<script src="js/html5shiv.js"></script>
		<link rel="stylesheet" media="screen" href="css/ie.css">
		<![endif]-->
	</head>
	<body>
<!--==============================header=================================-->
		<header>
			<div class="container_12">
				<div class="grid_12">
					<div class="menu_block">
						<nav class="horizontal-nav full-width horizontalNav-notprocessed">
							<ul class="sf-menu">
								<li><a href="{% url 'index' %}">ABOUT</a></li>
								<li><a href="{% url 'indexa' %}">HOT TOURS</a></li>
								<li class="current"><a href="{% url 'indexb' %}">SPECIAL OFFERS</a></li>
								<li><a href="{% url 'indexc' %}">BLOG</a></li>
								<li><a href="{% url 'indexd' %}">CONTACTS</a></li>
							</ul>
						</nav>
						<div class="clear"></div>
					</div>
				</div>
				<div class="grid_12">
					<h1>
						<a href="{% url 'index' %}">
							<img src="{% static 'images/logo.png' %}" alt="Your Happy Family">
						</a>
					</h1>
				</div>
			</div>
		</header>
<!--==============================Content=================================-->
		<div class="content"><div class="ic">More Website Templates @ TemplateMonster.com - February 10, 2014!</div>
			<div class="container_12">
				<div class="grid_8">
					<h3>Special offers</h3>
					<div class="block2">
						<img src="{% static 'images/page3_img1.jpg' %}" alt="" class="img_inner fleft">
						<div class="extra_wrapper">
							<div class="text1 col1"><a href="#">Barcelona</a></div>
							<p>Cras facilisis, nulla vel viverra auctor, leo gna sodales felis, quis malesuada nibh odio ut velit. Proin pharetra luctus diam, a celerisque eros convallis accumsan. </p>Maecenas vehicula egestas venenatis. Duis massa elit, auctor non pellentesque vel
							<br>
							<a href="#" class="link1">LEARN MORE</a>
						</div>
					</div>
					<div class="block2">
						<img src="{% static 'images/page3_img2.jpg' %}" alt="" class="img_inner fleft">
						<div class="extra_wrapper">
							<div class="text1 col1"><a href="#">Moscow</a></div>
							<p>Cras facilisis, nulla vel viverra auctor, leo gna sodales felis, quis malesuada nibh odio ut velit. Proin pharetra luctus diam, a celerisque eros convallis accumsan. </p>Maecenas vehicula egestas venenatis. Duis massa elit, auctor non pellentesque vel
							<br>
							<a href="#" class="link1">LEARN MORE</a>
						</div>
					</div>
					<div class="block2">
						<img src="{% static 'images/page3_img3.jpg' %}" alt="" class="img_inner fleft">
						<div class="extra_wrapper">
							<div class="text1 col1"><a href="#">Thailand</a></div>
							<p>Cras facilisis, nulla vel viverra auctor, leo gna sodales felis, quis malesuada nibh odio ut velit. Proin pharetra luctus diam, a celerisque eros convallis accumsan. </p>Maecenas vehicula egestas venenatis. Duis massa elit, auctor non pellentesque vel
							<br>
							<a href="#" class="link1">LEARN MORE</a>
						</div>
					</div>
				</div>
				<div class="grid_3 prefix_1">
					<h5>CHOOse the country</h5>
					<ul class="list">
						<li><a href="#">Albania</a></li>
						<li><a href="#">American Samoa</a></li>
						<li><a href="#">Antarctica</a></li>
						<li><a href="#">Argentina</a></li>
						<li><a href="#">Armenia</a></li>
						<li><a href="#">Australia</a></li>
						<li><a href="#">Austria</a></li>
						<li><a href="#">Bahrain</a></li>
						<li><a href="#">Barbados</a></li>
						<li><a href="#">Belgium</a></li>
						<li><a href="#">Belize</a></li>
						<li><a href="#">Bermudas</a></li>
					</ul>
					<a href="#" class="link1">VIEW A<span class="low">ll</span></a>
				</div>
			</div>
		</div>
<!--==============================footer=================================-->
		<footer>
			<div class="container_12">
				<div class="grid_12">
					<div class="socials">
						<a href="#" class="fa fa-facebook"></a>
						<a href="#" class="fa fa-twitter"></a>
						<a href="#" class="fa fa-google-plus"></a>
					</div>
					<div class="copy">
						Your Trip (c) 2014 | <a href="#">Privacy Policy</a> | Website Template Designed by TemplateMonster.com
					</div>
				</div>
			</div>
		</footer>
		<script>
		$(function (){
			$('#bookingForm').bookingForm({
				ownerEmail: '#'
			});
		})
		</script>
	</body>
</html>
{% load static %}
<!DOCTYPE html>
<html lang="en">
	<head>
		<title>Blog</title>
		<meta charset="utf-8">
		<meta name="format-detection" content="telephone=no" />
		<link rel="icon" href="{% static 'images/favicon.ico' %}">
		<link rel="shortcut icon" href="{% static 'images/favicon.ico' %}" />
		<link rel="stylesheet" href="{% static 'css/style.css' %}">
		<script src="{% static 'js/jquery.js' %}"></script>
		<script src="{% static 'js/jquery-migrate-1.2.1.js' %}"></script>
		<script src="{% static 'js/script.js' %}"></script>
		<script src="{% static 'js/superfish.js' %}"></script>
		<script src="{% static 'js/jquery.ui.totop.js' %}"></script>
		<script src="{% static 'js/jquery.equalheights.js' %}"></script>
		<script src="{% static 'js/jquery.mobilemenu.js' %}"></script>
		<script src="{% static 'js/jquery.easing.1.3.js' %}"></script>
		<script>
		$(document).ready(function(){
			$().UItoTop({ easingType: 'easeOutQuart' });
			});
		</script>
		<!--[if lt IE 8]>
		<div style=' clear: both; text-align:center; position: relative;'>
			<a href="http://windows.microsoft.com/en-US/internet-explorer/products/ie/home?ocid=ie6_countdown_bannercode">
				<img src="http://storage.ie6countdown.com/assets/100/images/banners/warning_bar_0000_us.jpg" border="0" height="42" width="820" alt="You are using an outdated browser. For a faster, safer browsing experience, upgrade for free today." />
			</a>
		</div>
		<![endif]-->
		<!--[if lt IE 9]>
		<script src="js/html5shiv.js"></script>
		<link rel="stylesheet" media="screen" href="css/ie.css">
		<![endif]-->
	</head>
	<body>
<!--==============================header=================================-->
		<header>
			<div class="container_12">
				<div class="grid_12">
					<div class="menu_block">
						<nav class="horizontal-nav full-width horizontalNav-notprocessed">
							<ul class="sf-menu">
								<li><a href="{% url 'index' %}">ABOUT</a></li>
								<li><a href="{% url 'indexa' %}">HOT TOURS</a></li>
								<li><a href="{% url 'indexb' %}">SPECIAL OFFERS</a></li>
								<li class="current"><a href="{% url 'indexc' %}">BLOG</a></li>
								<li><a href="{% url 'indexd' %}">CONTACTS</a></li>
							</ul>
						</nav>
						<div class="clear"></div>
					</div>
				</div>
				<div class="grid_12">
					<h1>
						<a href="{% url 'index' %}">
							<img src="{% static 'images/logo.png' %}" alt="Your Happy Family">
						</a>
					</h1>
				</div>
			</div>
		</header>
<!--==============================Content=================================-->
		<div class="content"><div class="ic">More Website Templates @ TemplateMonster.com - February 10, 2014!</div>
			<div class="container_12">
				<div class="grid_7">
					<h3>Recent Posts</h3>
					<div class="blog">
						<time datetime="2014-10-01">15<span>Feb</span></time>
						<div class="extra_wrapper">
							<div class="text1 col1"><a href="#">uamnibh Edet Mertolo numi</a></div>Posted by
							<a href="#">Admin</a>
						</div>
						<div class="clear"></div>
						<img src="{% static 'images/page4_img1.jpg' %}" alt="" class="img_inner">
						<p>Cras facilisis, nulla vel viverra auctor, leo gna sodales felis, quis malesuada nibh odio ut velit. Proin pharetra luctus diam, a celerisque eros convallis accumsan. </p>Maecenas vehicula egestas venenatis. Duis massa elit, auctor non pellentesque vel aliquet sit amet erat. Nullam eget dignissim nisi, aliquam feugiat nibh.
						<br>
						<a href="#" class="link1">LEARN MORE</a>
					</div>
					<div class="blog">
						<time datetime="2014-10-01">17<span>Feb</span></time>
						<div class="extra_wrapper">
							<div class="text1 col1"><a href="#">ERh EMertlo numolo</a></div>Posted by
							<a href="#">Admin</a>
						</div>
						<div class="clear"></div>
						<img src="{% static 'images/page4_img2.jpg' %}" alt="" class="img_inner">
						<p>Cras facilisis, nulla vel viverra auctor, leo gna sodales felis, quis malesuada nibh odio ut velit. Proin pharetra luctus diam, a celerisque eros convallis accumsan. </p>Maecenas vehicula egestas venenatis. Duis massa elit, auctor non pellentesque vel aliquet sit amet erat. Nullam eget dignissim nisi, aliquam feugiat nibh.
						<br>
						<a href="#" class="link1">LEARN MORE</a>
					</div>
				</div>
				<div class="grid_3 prefix_1">
					<h3 class="head1">CATEGORIES</h3>
					<ul class="list">
						<li><a href="#">Suspendisse massa mi </a></li>
						<li><a href="#">Porttitor at velit id </a></li>
						<li><a href="#">Congue adipiscing </a></li>
						<li><a href="#">Vestibulum vitae porta </a></li>
						<li><a href="#">Vivamus ac sodales </a></li>
						<li><a href="#">Massa quis adipiscing </a></li>
						<li><a href="#">Phasellus hendrerit </a></li>
						<li><a href="#">Libero in sapien </a></li>
						<li><a href="#">Dignissim vel imperdiet </a></li>
					</ul>
					<h3 class="head1">ARchives</h3>
					<ul class="list">
						<li><a href="#">November 2013</a></li>
						<li><a href="#">October 2013</a></li>
						<li><a href="#">September 2013</a></li>
						<li><a href="#">August 2013</a></li>
						<li><a href="#">July 2013</a></li>
					</ul>
				</div>
			</div>
		</div>
<!--==============================footer=================================-->
		<footer>
			<div class="container_12">
				<div class="grid_12">
					<div class="socials">
						<a href="#" class="fa fa-facebook"></a>
						<a href="#" class="fa fa-twitter"></a>
						<a href="#" class="fa fa-google-plus"></a>
					</div>
					<div class="copy">
						Your Trip (c) 2014 | <a href="#">Privacy Policy</a> | Website Template Designed by TemplateMonster.com
					</div>
				</div>
			</div>
		</footer>
		<script>
		$(function (){
			$('#bookingForm').bookingForm({
				ownerEmail: '#'
			});
		})
		</script>
	</body>
</html>
{% load static %}
<!DOCTYPE html>
<html lang="en">
	<head>
		<title>Contacts</title>
		<meta charset="utf-8">
		<meta name="format-detection" content="telephone=no" />
		<link rel="icon" href="{% static 'images/favicon.ico' %}">
		<link rel="shortcut icon" href="{% static 'images/favicon.ico' %}" />
		<link rel="stylesheet" href="{% static 'css/form.css' %}">
		<link rel="stylesheet" href="{% static 'css/style.css' %}">
		<script src="{% static 'js/jquery.js' %}"></script>
		<script src="{% static 'js/jquery-migrate-1.2.1.js' %}"></script>
		<script src="{% static 'js/script.js' %}"></script>
		<script src="{% static 'js/TMForm.js' %}"></script>
		<script src="{% static 'js/superfish.js' %}"></script>
		<script src="{% static 'js/jquery.ui.totop.js' %}"></script>
		<script src="{% static 'js/jquery.equalheights.js' %}"></script>
		<script src="{% static 'js/jquery.mobilemenu.js' %}"></script>
		<script src="{% static 'js/jquery.easing.1.3.js' %}"></script>
		<script>
		$(document).ready(function(){
			$().UItoTop({ easingType: 'easeOutQuart' });
			});
		</script>
		<!--[if lt IE 8]>
		<div style=' clear: both; text-align:center; position: relative;'>
			<a href="http://windows.microsoft.com/en-US/internet-explorer/products/ie/home?ocid=ie6_countdown_bannercode">
				<img src="http://storage.ie6countdown.com/assets/100/images/banners/warning_bar_0000_us.jpg" border="0" height="42" width="820" alt="You are using an outdated browser. For a faster, safer browsing experience, upgrade for free today." />
			</a>
		</div>
		<![endif]-->
		<!--[if lt IE 9]>
		<script src="js/html5shiv.js"></script>
		<link rel="stylesheet" media="screen" href="css/ie.css">
		<![endif]-->
	</head>
	<body>
<!--==============================header=================================-->
		<header>
			<div class="container_12">
				<div class="grid_12">
					<div class="menu_block">
						<nav class="horizontal-nav full-width horizontalNav-notprocessed">
							<ul class="sf-menu">
								<li><a href="{% url 'index' %}">ABOUT</a></li>
								<li><a href="{% url 'indexa' %}">HOT TOURS</a></li>
								<li><a href="{% url 'indexb' %}">SPECIAL OFFERS</a></li>
								<li><a href="{% url 'indexc' %}">BLOG</a></li>
								<li class="current"><a href="{% url 'indexd' %}">CONTACTS</a></li>
							</ul>
						</nav>
						<div class="clear"></div>
					</div>
				</div>
				<div class="grid_12">
					<h1>
						<a href="{% url 'index' %}">
							<img src="{% static 'images/logo.png' %}" alt="Your Happy Family">
						</a>
					</h1>
				</div>
			</div>
		</header>
<!--==============================Content=================================-->
		<div class="content"><div class="ic">More Website Templates @ TemplateMonster.com - February 10, 2014!</div>
			<div class="container_12">
				<div class="grid_5">
					<h3>CONTACT INFO</h3>
					<div class="map">
						<p><span class="blog">Maecenas vehicula egestas venenatis. Duis massa elit, auctor non pellentesque vel aliquet sit amet erat. Nullam eget dignissim nisi, aliquam feugiat nibh. </span></p>
						<div class="clear"></div>
						<figure class="">
							<iframe src="http://maps.google.com/maps?f=q&amp;source=s_q&amp;hl=en&amp;geocode=&amp;q=Brooklyn,+New+York,+NY,+United+States&amp;aq=0&amp;sll=37.0625,-95.677068&amp;sspn=61.282355,146.513672&amp;ie=UTF8&amp;hq=&amp;hnear=Brooklyn,+Kings,+New+York&amp;ll=40.649974,-73.950005&amp;spn=0.01628,0.025663&amp;z=14&amp;iwloc=A&amp;output=embed"></iframe>
						</figure>
						<address>
							<dl>
								<dt>The Company Name Inc. <br>
									8901 Marmora Road,<br>
									Glasgow, D04 89GR.
								</dt>
								<dd><span>Freephone:</span>+1 800 559 6580</dd>
								<dd><span>Telephone:</span>+1 800 603 6035</dd>
								<dd><span>FAX:</span>+1 800 889 9898</dd>
								<dd>E-mail: <a href="#" class="col1">mail@demolink.org</a></dd>
							</dl>
						</address>
					</div>
				</div>
				<div class="grid_6 prefix_1">
					<h3>GET IN TOUCH</h3>
					<form id="form">
						<div class="success_wrapper">
							<div class="success-message">Contact form submitted</div>
						</div>
						<label class="name">
							<input type="text" placeholder="Name:" data-constraints="@Required @JustLetters" />
							<span class="empty-message">*This field is required.</span>
							<span class="error-message">*This is not a valid name.</span>
						</label>
						<label class="email">
							<input type="text" placeholder="Email:" data-constraints="@Required @Email" />
							<span class="empty-message">*This field is required.</span>
							<span class="error-message">*This is not a valid email.</span>
						</label>
						<label class="country">
							<input type="text" placeholder="Country:" data-constraints="@Required @JustLetters"/>
							<span class="empty-message">*This field is required.</span>
							<span class="error-message">*This is not a valid phone.</span>
						</label>
						<label class="message">
							<textarea placeholder="Message:" data-constraints='@Required @Length(min=20,max=999999)'></textarea>
							<span class="empty-message">*This field is required.</span>
							<span class="error-message">*The message is too short.</span>
						</label>
						<div>
							<div class="clear"></div>
							<div class="btns">
								<a href="#" data-type="reset" class="btn">Clear</a>
								<a href="#" data-type="submit" class="btn">Submit</a>
							</div>
						</div>
					</form>
				</div>
			</div>
		</div>
<!--==============================footer=================================-->
		<footer>
			<div class="container_12">
				<div class="grid_12">
					<div class="socials">
						<a href="#" class="fa fa-facebook"></a>
						<a href="#" class="fa fa-twitter"></a>
						<a href="#" class="fa fa-google-plus"></a>
					</div>
					<div class="copy">
						Your Trip (c) 2014 | <a href="#">Privacy Policy</a> | Website Template Designed by TemplateMonster.com
					</div>
				</div>
			</div>
		</footer>
		<script>
		$(function (){
			$('#bookingForm').bookingForm({
				ownerEmail: '#'
			});
		})
		</script>
	</body>
</html>
{% load static %}
{%static "images" as baseurl %}

<!DOCTYPE html>
<html lang="en">
	<head>
		<title>navjot travl</title>
		<meta charset="utf-8">
		<meta name="format-detection" content="telephone=no" />
		<link rel="icon" href="{% static 'images/favicon.ico' %}">
		<link rel="shortcut icon" href="{% static 'images/favicon.ico' %}" />
		<link rel="stylesheet" href="{% static 'booking/css/booking.css' %}">
		<link rel="stylesheet" href="{% static 'css/camera.css' %}">
		<link rel="stylesheet" href="{% static 'css/owl.carousel.css' %}">
		<link rel="stylesheet" href="{% static 'css/style.css' %}">
		<script src="{% static 'js/jquery.js' %}"></script>
		<script src="{% static 'js/jquery-migrate-1.2.1.js' %}"></script>
		<script src="{% static 'js/script.js' %}"></script>
		<script src="{% static 'js/superfish.js' %}"></script>
		<script src="{% static 'js/jquery.ui.totop.js' %}"></script>
		<script src="{% static 'js/jquery.equalheights.js' %}"></script>
		<script src="{% static 'js/jquery.mobilemenu.js' %}"></script>
		<script src="{% static 'js/jquery.easing.1.3.js' %}"></script>
		<script src="{% static 'js/owl.carousel.js' %}"></script>
		<script src="{% static 'js/camera.js' %}"></script>
		<!--[if (gt IE 9)|!(IE)]><!-->
		<script src="{% static 'js/jquery.mobile.customized.min.js' %}"></script>
		<!--<![endif]-->
		<script src="{% static 'booking/js/booking.js' %}"></script>
		<script>
			$(document).ready(function(){
			jQuery('#camera_wrap').camera({
				loader: false,
				pagination: false ,
				minHeight: '444',
				thumbnails: false,
				height: '48.375%',
				caption: true,
				navigation: true,
				fx: 'mosaic'
			});
			/*carousel*/
			var owl=$("#owl");
				owl.owlCarousel({
				items : 2, //10 items above 1000px browser width
				itemsDesktop : [995,2], //5 items between 1000px and 901px
				itemsDesktopSmall : [767, 2], // betweem 900px and 601px
				itemsTablet: [700, 2], //2 items between 600 and 0
				itemsMobile : [479, 1], // itemsMobile disabled - inherit from itemsTablet option
				navigation : true,
				pagination : false
				});
			$().UItoTop({ easingType: 'easeOutQuart' });
			});
		</script>
		<!--[if lt IE 8]>
		<div style=' clear: both; text-align:center; position: relative;'>
			<a href="http://windows.microsoft.com/en-US/internet-explorer/products/ie/home?ocid=ie6_countdown_bannercode">
				<img src="http://storage.ie6countdown.com/assets/100/images/banners/warning_bar_0000_us.jpg" border="0" height="42" width="820" alt="You are using an outdated browser. For a faster, safer browsing experience, upgrade for free today." />
			</a>
		</div>
		<![endif]-->
		<!--[if lt IE 9]>
		<script src="js/html5shiv.js"></script>
		<link rel="stylesheet" media="screen" href="css/ie.css">
		<![endif]-->
	</head>
	<body class="page1" id="top">
<!--==============================header=================================-->
		<header>
			<div class="container_12">
				<div class="grid_12">
					<div class="menu_block">
						<nav class="horizontal-nav full-width horizontalNav-notprocessed">
							<ul class="sf-menu">
								<li class="current"><a href="{% url 'index' %}">ABOUT</a></li>
								<li><a href="{% url 'indexa' %}">HOT TOURS</a></li>
								<li><a href="{% url 'indexb' %}">SPECIAL OFFERS</a></li>
								<li><a href="{% url 'indexc' %}">BLOG</a></li>
								<li><a href="{% url 'indexd' %}">CONTACTS</a></li>
								
								{% if user.is_authenticated %}
								<li>hello , {{user.first_name}}</li>
								<li><a href="accounts/logout">Logout</a></li>
								{% else %}
								<li><a href="accounts/register">Register</a></li>
								<li><a href="accounts/login">Login</a></li>
								{% endif %}
							</ul>
						</nav>
						<div class="clear"></div>
					</div>
				</div>
				<div class="grid_12">
					<h1>
						<a href="{% url 'index' %}">
							<img src="{% static 'images/logo.png' %}" alt="Your Happy Family">
						</a>
					</h1>
				</div>
			</div>
		</header>
		<div class="slider_wrapper">
			<div id="camera_wrap" class="">
				<div data-src="{% static 'images/slide.jpg' %}">
					<div class="caption fadeIn">
						<h2>LONDON</h2>
						<div class="price">
							FROM
							<span>$1000</span>
						</div>
						<a href="#">LEARN MORE</a>
					</div>
				</div>
				<div data-src="{% static 'images/slide1.jpg' %}">
					<div class="caption fadeIn">
						<h2>Maldives</h2>
						<div class="price">
							FROM
							<span>$2000</span>
						</div>
						<a href="#">LEARN MORE</a>
					</div>
				</div>
				<div data-src="{% static 'images/slide2.jpg' %}">
					<div class="caption fadeIn">
						<h2>Venice</h2>
						<div class="price">
							FROM
							<span>$1600</span>
						</div>
						<a href="#">LEARN MORE</a>
					</div>
				</div>
			</div>
		</div>
		
<!--==============================Content=================================-->
		<div class="content"><div class="ic">More Website Templates @ TemplateMonster.com - February 10, 2014!</div>
			{% for dest in dests %}
			<div class="container_12">
				<div class="grid_4">
					<div class="banner">
						<img src="{{dest.img.url}}" alt="">
						<div class="label">
							<div class="title">{{dest.name}}</div>
							<div class="subtitle"><p>{{dest.desc}}</p></div>
							<div class="price">FROM<span>$ {{dest.price}}</span></div>
							<a href="#">LEARN MORE</a>
						</div>
					</div>
				</div>
			{% endfor %}
				<div class="clear"></div>
				<div class="grid_6">
					<h3>Booking Form</h3>
					<form id="bookingForm">
						<div class="fl1">
							<div class="tmInput">
								<input name="Name" placeHolder="Name:" type="text" data-constraints='@NotEmpty @Required @AlphaSpecial'>
							</div>
							<div class="tmInput">
								<input name="Country" placeHolder="Country:" type="text" data-constraints="@NotEmpty @Required">
							</div>
						</div>
						<div class="fl1">
							<div class="tmInput">
								<input name="Email" placeHolder="Email:" type="text" data-constraints="@NotEmpty @Required @Email">
							</div>
							<div class="tmInput mr0">
								<input name="Hotel" placeHolder="Hotel:" type="text" data-constraints="@NotEmpty @Required">
							</div>
						</div>
						<div class="clear"></div>
						<strong>Check-in</strong>
						<label class="tmDatepicker">
							<input type="text" name="Check-in" placeHolder='10/05/2014' data-constraints="@NotEmpty @Required @Date">
						</label>
						<div class="clear"></div>
						<strong>Check-out</strong>
						<label class="tmDatepicker">
							<input type="text" name="Check-out" placeHolder='20/05/2014' data-constraints="@NotEmpty @Required @Date">
						</label>
						<div class="clear"></div>
						<div class="tmRadio">
							<p>Comfort</p>
							<input name="Comfort" type="radio" id="tmRadio0" data-constraints='@RadioGroupChecked(name="Comfort", groups=[RadioGroup])' checked/>
							<span>Cheap</span>
							<input name="Comfort" type="radio" id="tmRadio1" data-constraints='@RadioGroupChecked(name="Comfort", groups=[RadioGroup])' />
							<span>Standart</span>
							<input name="Comfort" type="radio" id="tmRadio2" data-constraints='@RadioGroupChecked(name="Comfort", groups=[RadioGroup])' />
							<span>Lux</span>
						</div>
						<div class="clear"></div>
						<div class="fl1 fl2">
							<em>Adults</em>
							<select name="Adults" class="tmSelect auto" data-class="tmSelect tmSelect2" data-constraints="">
								<option>1</option>
								<option>1</option>
								<option>2</option>
								<option>3</option>
							</select>
							<div class="clear"></div>
							<em>Rooms</em>
							<select name="Rooms" class="tmSelect auto" data-class="tmSelect tmSelect2" data-constraints="">
								<option>1</option>
								<option>1</option>
								<option>2</option>
								<option>3</option>
							</select>
						</div>
						<div class="fl1 fl2">
							<em>Children</em>
							<select name="Children" class="tmSelect auto" data-class="tmSelect tmSelect2" data-constraints="">
								<option>0</option>
								<option>0</option>
								<option>1</option>
								<option>2</option>
							</select>
						</div>
						<div class="clear"></div>
						<div class="tmTextarea">
							<textarea name="Message" placeHolder="Message" data-constraints='@NotEmpty @Required @Length(min=20,max=999999)'></textarea>
						</div>
						<a href="#" class="btn" data-type="submit">Submit</a>
					</form>
				</div>
				<div class="grid_5 prefix_1">
					<h3>Welcome</h3>
					<img src="{% static 'images/page1_img1.jpg' %}" alt="" class="img_inner fleft">
					<div class="extra_wrapper">
						<p>Lorem ipsum dolor sit ere amet, consectetur ipiscin.</p>
						In mollis erat mattis neque facilisis, sit ametiol
					</div>
					<div class="clear cl1"></div>
					<p>Proin pharetra luctus diam, a scelerisque eros convallis </p>
				  <h4>Clients’ Quotes</h4>
					<blockquote class="bq1">
						<img src="{% static 'images/page1_img2.jpg' %}" alt="" class="img_inner noresize fleft">
						<div class="extra_wrapper">
							<p>Duis massa elit, auctor non pellentesque vel, aliquet sit amet erat. Nullam eget dignissim nisi, aliquam feugiat nibh. </p>
							<div class="alright">
								<div class="col1">Miranda Brown</div>
								<a href="#" class="btn">More</a>
							</div>
						</div>
					</blockquote>
				</div>
				<div class="grid_12">
					<h3 class="head1">Latest News</h3>
				</div>
				<div class="grid_4">
					<div class="block1">
						<time datetime="2014-01-01">10<span>Jan</span></time>
						<div class="extra_wrapper">
							<div class="text1 col1"><a href="#">Aliquam nibh</a></div>
							Proin pharetra luctus diam, any scelerisque eros convallisumsan. Maecenas vehicula egestas
						</div>
					</div>
				</div>
				<div class="grid_4">
					<div class="block1">
						<time datetime="2014-01-01">21<span>Jan</span></time>
						<div class="extra_wrapper">
							<div class="text1 col1"><a href="#">Etiam dui eros</a></div>
							Any scelerisque eros vallisumsan. Maecenas vehicula egestas natis. Duis massa elit, auctor non
						</div>
					</div>
				</div>
				<div class="grid_4">
					<div class="block1">
						<time datetime="2014-01-01">15<span>Feb</span></time>
						<div class="extra_wrapper">
							<div class="text1 col1"><a href="#">uamnibh Edeto</a></div>
							Ros convallisumsan. Maecenas vehicula egestas venenatis. Duis massa elit, auctor non
						</div>
					</div>
				</div>
			</div>
		</div>
<!--==============================footer=================================-->
		<footer>
			<div class="container_12">
				<div class="grid_12">
					<div class="socials">
						<a href="#" class="fa fa-facebook"></a>
						<a href="#" class="fa fa-twitter"></a>
						<a href="#" class="fa fa-google-plus"></a>
					</div>
					<div class="copy">
						Your Trip (c) 2014 | <a href="#">Privacy Policy</a> | Website Template Designed by TemplateMonster.com
					</div>
				</div>
			</div>
		</footer>
		<script>
			$(function (){
				$('#bookingForm').bookingForm({
					ownerEmail: '#'
				});
			})
			$(function() {
				$('#bookingForm input, #bookingForm textarea').placeholder();
			});
		</script>
	</body>
</html>


<!--
							{% if dest.offer %}
							<div class="spec_offer text-center"><a href = "#">special offer</a> </div>
							{% endif %}-->

