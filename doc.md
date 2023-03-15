# UI Mock-Up Documentation

Documentation to cover the basic functions used in our UI Mockup. Includes Jinja, Bootstrap, and Flask. Foundation includes Python and
HTML. The HTML reference used is [here](https://developer.mozilla.org/en-US/docs/Web/HTML/Element). Some elements will have rendered output below their respective code block but due to markdown limitations they might not show up the same as on the website.

- [Bootstrap](#bootstrap)
- [Jinja](#jinja)
- [Flask](#flask)

# Bootstrap

Used mostly for stylizing containers in HTML. Original documentation for reference is [here](https://getbootstrap.com/). 

- [Introduction](#introduction)
- [Carousel](#carousel)
- [Form Control](#form-control)
- [Header](#header)

----
## Introduction

general html strucutre and use of bootstrap stylization. 
```html
<div class="container-fluid bg-2 text-center" >
  <h3>Who Are We?</h3>
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
</div>
<br>
```
rendered output below: 
<div class="container-fluid bg-2 text-center" >
  <h3>Who Are We?</h3>
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
</div>

----

## Carousel
carousel structure used in gallery.html to show pictures on website.
  
code to have stylized buttons below
```html
<div class="container">
<div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
  <div class="carousel-indicators">
    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
  </div> 
```

code that creates the actual buttons and hides behind the stylized buttons
```html
<button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
```
rendered output below
<div class="container">
<div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
  <div class="carousel-indicators">
    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
    <button type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide-to="1" aria-label="Slide 2"></button>
  </div> 
<br> <br>

```html
<div class="carousel-inner">
    <div class="carousel-item active">
      <img src="https://www.hallmark.com/dw/image/v2/AALB_PRD/on/demandware.static/-/Sites-hallmark-master/default/dw63b5be64/images/finished-goods/Light-the-Candles-Cat-in-Sunglasses-Funny-Birthday-Card_369ZZB3738_04.jpg?sw=1920" class="d-block w-100" alt="Cat with sunglasses 1.">
  		<div class="carousel-caption d-none d-md-block text-muted">
    	<h5>Oh dang!</h5>
    	<p>Look how cool this cat is! :O</p>
  		</div>
    </div> 
```

rendered output below with a style change:
```html
style="width:300px;height:300px;"
```
<div class="carousel-inner">
    <div class="carousel-item active">
      <img src="https://www.hallmark.com/dw/image/v2/AALB_PRD/on/demandware.static/-/Sites-hallmark-master/default/dw63b5be64/images/finished-goods/Light-the-Candles-Cat-in-Sunglasses-Funny-Birthday-Card_369ZZB3738_04.jpg?sw=1920" style="width:300px;height:300px;" class="d-block w-100" alt="Cat with sunglasses 1.">
  		<div class="carousel-caption d-none d-md-block text-muted">
    	<h5>Oh dang!</h5>
    	<p>Look how cool this cat is! :O</p>
  		</div>
    </div>  
 
----

## Form Control

class form-group used to login into admin.html

```html
<div class="container">
	<form action='login' method='POST'>
  		<div class="form-group">
			<input type='text' name='email' id='email' placeholder='email' class='form-control'></input><br>
		</div>
  		<div class="form-group">
			<input type='password' name='pw' id='pw' placeholder='password' class='form-control'></input><br>
		</div>
		<input type='submit' name='submit' class="btn btn-outline-dark green_back_gold_front_lightened"></input>
	</form>
</div>
```


rendered output below:
<div class="container">
	<form action='login' method='POST'>
  		<div class="form-group">
			<input type='text' name='email' id='email' placeholder='email' class='form-control'></input><br>
		</div>
  		<div class="form-group">
			<input type='password' name='pw' id='pw' placeholder='password' class='form-control'></input><br>
		</div>
		<input type='submit' name='submit' class="btn btn-outline-dark green_back_gold_front_lightened"></input>
	</form>
</div> <br>

class form-control to alter database and elements on website, changes persist after admin logs out.

```html
<form method="POST">
  		<label for="deleteplayer">Player Name:</label><br>
    	<input name="deleteplayer" value ="Jane Doe" class="form-control"><br>
    	<input type="submit" id='delete-form' name='delete-form' value="Delete Player" class="btn btn-outline-dark green_back_gold_front_lightened">
	</form> 
	<hr/>
</div>
```

rendered output below to delete a player from the database:
<form method="POST">
  		<label for="deleteplayer">Player Name:</label><br>
    	<input name="deleteplayer" value ="Jane Doe" class="form-control"><br>
    	<input type="submit" id='delete-form' name='delete-form' value="Delete Player" class="btn btn-outline-dark green_back_gold_front_lightened">
	</form> 
</div> <br>

code block with an added text box for player description and adding players.
```html
<form method="POST" id="add-form" name="add-form">
  		<label for="addname">Player Name:</label><br>
  		<input type="text" id="addname" name="addname" value="John Doe" class="form-control"><br>
  		<label for="desc">Player Description:</label><br>
  		<input type="text" id="desc" name="desc" value="... player description here ..." class="form-control"><br>
  		<input type="submit" id='add-form' name='add-form' value="Add Player" class="btn btn-outline-dark green_back_gold_front_lightened">
	</form> 
</div>
```
structure of form control is creating label, defining input, and calling the class form control.    
rendered output for adding with and without the text description.
<form method="POST" id="add-form" name="add-form">
  		<label for="addname">Player Name:</label><br>
  		<input type="text" id="addname" name="addname" value="John Doe" class="form-control"><br>
  		<label for="desc">Player Description:</label><br>
  		<input type="text" id="desc" name="desc" value="... player description here ..." class="form-control"><br>
  		<input type="submit" id='add-form' name='add-form' value="Add Player" class="btn btn-outline-dark green_back_gold_front_lightened">
	</form> 
</div> <br>

<form method="POST" id="add-form" name="add-form">
  		<label for="addname">Player Name:</label><br>
  		<input type="text" id="addname" name="addname" value="John Doe" class="form-control"><br>
  		<input type="submit" id='add-form' name='add-form' value="Add Player" class="btn btn-outline-dark green_back_gold_front_lightened">
	</form> 
</div>

----
## Header

uses ul and li, list structure and elements to build a header at the top of the website.
```html
<footer class="footer mt-auto py-3 green_back_gold_front">
  <div class="container">
    <span class="text-muted">
      <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
        <ul class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
          <li><a href="/" class="nav-link px-2">Home</a></li>
          <li><a href="/gallery" class="nav-link px-2">Gallery</a></li>
          <li><a href="/calendar" class="nav-link px-2">Calendar</a></li>
          <li><a href="/about" class="nav-link px-2">About</a></li>
          <li><a href="/instagram" class="nav-link px-2">Instagram</a></li>
        </ul>
	</span>
  </div>
</footer> 
</html> 
```
rendered output:
![the code in markdown spits out garbage i had to just grab the header](https://cdn.discordapp.com/attachments/1014300694238482442/1085684643510108181/image.png)
<br>

additional code block to display extra login button for admins:
```html
<div class="text-end green_black_gold_front">
          <button type="button" class="btn btn-outline-dark me-2 justify-content-right green_back_gold_front_lightened" onclick="window.location.href='/login';">Login</button>
        </div>
```
ss
rendered output:

![again](https://cdn.discordapp.com/attachments/1014300694238482442/1085685783433855098/image.png)

# Jinja

Used in base.html to act as an abstraction and apply a common style easily to most elements on the website. Original documentation for reference is [here](https://palletsprojects.com/p/jinja/).

- [Introduction](#introduction-jinja)
- [% block title %](#blocktitle)
- [% block body %](#blockbody)
----
<h2 id="introduction-jinja">Introduction</h2>
To make appying styles onto all of our pages easier, we define a sac style color pallette in base.html and wrap the bulk of the html files with % block body %.  

We also end each block call with endblock to define the end of either the title or the body.   
Each of our files extends base.html as such in order to use this structure:
```html
{% extends 'base.html' %}
```

----

<h2 id="blocktitle">% block title %</h2>
Block title refers to our tab name, and as such the code is very basic.

```html
<title>
	{% block title %} {% endblock %}
</title>
```
These code blocks are placed before each block body, where it wraps the bulk of the html file. Each code block currently has the same tab name, "Rowing Club Website Templates Demo".

----

<h2 id="blockbody">% block body %</h2>

Block body refers to the text and font style that wraps around the main functions that render text and images. As the client requested a sac state color pallette, this body class defines the color as the primary sac state colors.
```html
<body class="white_back_dark_green_front">
	<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js" integrity="sha384-oBqDVmMz9ATKxIep9tiCxS/Z9fNfEXiDAYTujMAeBAsjFuCZSmKbSSUnQlmh/jp3" crossorigin="anonymous"></script>
	<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.min.js" integrity="sha384-mQ93GR66B00ZXjt0YO5KlohRA5SY2XofN4zfuZxLkoj1gXtW8ANNCe9d5Y3eG5eD" crossorigin="anonymous"></script>
	{% block body %} {% endblock %}
</body>
```
A sample code block is provided below as a wrapping demonstration.
```html
{% block body %}
<div class="jumbotron text-center">
	<h1>Welcome To The Rowing Club HomePage</h1>
	<p>Brief tagline here!</p>
</div>

<div class="container">
	<div class="row">
		{% for tup in players %}
			<h3>{{ tup[0] }}</h3>
			<p>{{ tup[1] }}</p>
		{% endfor %}
	</div>
</div>
{% endblock %}
```

# Flask

- [Introduction](#introduction-flask)
- [Database Handling](#database-handling)
- [Login Handling](#login-handling)

Used to power our login page and change data on the website. Original documentation for reference is [here](https://pypi.org/project/Flask-Login/).

<h2 id="introduction-flask">Introduction</h2>

## Database Handling

## Login Handling