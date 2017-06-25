var express = require('express');
var bodyParser = require('body-parser');

var fs = require('fs');
var util = require('util');
var path = require('path');


var app = express();
app.use( bodyParser.json() );       // to support JSON-encoded bodies
app.use(bodyParser.urlencoded({     // to support URL-encoded bodies
  extended: true
}));

app.use(express.static(path.join(__dirname, 'public')));

/* Handle the post request to parse a sentence.*/
app.get('/get_image', function(req, res) {
    // recieve, tokenise and determine sentiment of sentences.
    var image_requested = req.body.sentence;
    
});

var server = app.listen(12312, function() {
    var host = server.address().address;
    var port = server.address().port;
    console.log('Server App running at http://%s:%s', host, port);
});
