
const express = require("express");
const port = process.env.PORT || 3000;
const app = express();

arr = ["Intelligence assessment","Jujutsu Kaisen","One Piece (TV series)","Monkey D. Luffy","Diane Shaw","Artificial intelligence","Greek mythology","Book burning","Cryptography","Information theory"]

app.post("/", async (req, res) => {
    
});


app.listen(port, () => {
  console.log(`La API esta corriendo en  http://localhost:${port}`);
});