
const express = require("express");
const port = process.env.PORT || 3000;
const app = express();

import myJson from "./hadoop/info.json" assert {type: "json"};

arr = ["Intelligence assessment","Jujutsu Kaisen","One Piece (TV series)","Monkey D. Luffy","Diane Shaw","Artificial intelligence","Greek mythology","Book burning","Cryptography","Information theory"]

//recibe un parametro y los busca en el archivo json

app.get("/search/:item", async (req, res) => {
  const { item } = req.params;
    if(myJson.item != null)
      console.log("Esa palabra no esta la base de datos");
    else
      console.log(myJson.item)
});


app.listen(port, () => {
  console.log(`La API esta corriendo en  http://localhost:${port}`);
});