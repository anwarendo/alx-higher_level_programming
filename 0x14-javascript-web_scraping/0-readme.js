#!/usr/local/bin/node

const request = require('request');
const url = 'file:///home/anwar/alx/alx-higher_level_programming/0x14-javascript-web_scraping/cisfun';

request (url, function (error, response, body) {
    if (error) {
	console.log(error);
    } else {
	console.log(JSON.parse(body));
    }
});
