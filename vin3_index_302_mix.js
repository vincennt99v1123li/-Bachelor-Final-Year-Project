#!/usr/bin/env node
 
var express = require('express');
var bodyParser = require('body-parser');
 
var app = express();
 
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

var Notification_content =''
var Notification_time = ''
app.post("/postdata", (req, res) => {
    Notification_content = req.body.Notification_content;
    Notification_time = req.body.Notification_time;


    console.log(Notification_content);
    console.log(Notification_time);
    res.send("process complete");
});

app.get("/getdata", (req, res) => {

    var ORDER = { // this is the data you're sending back during the GET request
        "Notification_content": Notification_content,
        "Notification_time": Notification_time,

    }
    res.status(200).json(ORDER)
});
 
app.listen(3000);


