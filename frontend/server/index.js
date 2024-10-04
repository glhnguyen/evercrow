const path = require("path");
const express = require("express");
require("dotenv").config;

const port = process.env.SERVER_PORT;
const environment = process.env.NODE_ENV;

const buildPath = path.join(__dirname, "..", "build");
const indexPath = path.join(buildPath, "index.html");

const app = express();

app.use(
  express.urlencoded({ extended: true }),
  express.json(),
  express.static(buildPath)
);

app.use((req, res, next) => {
  res.sendFile(indexPath);
});

app.listen(port, () => {
  console.log(`Node Server listening on port: ${port} [${environment}]`);
});
