var up = new Button();
var down = new Button();
var image = new Image();
var movie = new Label();
var rating = new Label();

movie.createLabel("which movie?", "movie");
rating.createLabel("Rating", "rating");
up.createButton("UP", "up");
down.createButton("DOWN", "down");
image.createImage("image");

var uid = Number("5"); //arbitrary
var mid = Number("80");

getMovie(uid);

up.addClickEventHandler(Up);
down.addClickEventHandler(Down);

//image button formatting
var image_buttons = new Format();
image_buttons.createFormat("image_buttons");
image_buttons.appendChild(up.getItem());
image_buttons.appendChild(image.getItem());
image_buttons.appendChild(down.getItem());

//main formatting
var main = new Format();
main.createFormat("main");
main.appendChild(movie.getItem());
main.appendChild(image_buttons.getItem());
main.appendChild(rating.getItem());

main.addToDocument();

function getMovie(uid) {
	var request = new XMLHttpRequest();
	request.open("GET", "http://student04.cse.nd.edu:51080/recommendations/" + uid, true);

	request.onload = function(e) {
		var response = JSON.parse(request.responseText);
		mid = response["movie_id"]
		setMovie();
		setRating();
	}
	request.send(null);
}
function setMovie() {
	var request = new XMLHttpRequest();
	request.open("GET", "http://student04.cse.nd.edu:51080/movies/" + mid, true);
	
	request.onload = function(e) {
                var response = JSON.parse(request.responseText);
		movie.setText(response["title"]);
		image.setImage(response["img"]);
        }
        request.send(null);
}
function setRating() {
	var request = new XMLHttpRequest();
	request.open("GET", "http://student04.cse.nd.edu:51080/ratings/" + mid, true);

        request.onload = function(e) {
                var response = JSON.parse(request.responseText);
		rating.setText(response["rating"]);
        }
        request.send(null);
}
function Up() {
	var dict = {"movie_id": mid,"rating": 5};
	var json_dict = JSON.stringify(dict);

	var request = new XMLHttpRequest();
	request.open("PUT", "http://student04.cse.nd.edu:51080/recommendations/" + uid, true);
	request.onload = function(e) {
		getMovie(uid);
	}
	request.send(json_dict);
}
function Down() {
        var dict = {"movie_id": mid,"rating": 1};
	var json_dict = JSON.stringify(dict);

        var request = new XMLHttpRequest();
	request.open("PUT", "http://student04.cse.nd.edu:51080/recommendations/" + uid, true);
        request.onload = function(e) {
                getMovie(uid);
        }
	request.send(json_dict);
}
