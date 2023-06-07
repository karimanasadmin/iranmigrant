const express = require("express");
const bodyParser = require("body-parser");
const fs = require("fs");

const app = express();
app.use(bodyParser.json());

app.post("/save-data", function(req, res) {
    // Get form data from the request body
    const { name, family, email } = req.body;

    // Prepare CSV data
    const csvData = `Name,Family,Email,Date\n${name},${family},${email},${new Date().toLocaleString()}\n`;

    // Append CSV data to the file
    fs.appendFile("usersreq.csv", csvData, function(err) {
        if (err) {
            console.error("Failed to save data:", err);
            res.sendStatus(500);
        } else {
            console.log("Data saved successfully");
            res.sendStatus(200);
        }
    });
});

app.listen(3000, function() {
    console.log("Server started on port 3000");
});
