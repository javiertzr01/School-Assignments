const express = require('express');

var publicDir = require('path').join(__dirname, '/public');
const app = express()

app.use(express.static(publicDir));

app.get('/index.html', (req, res) => {
        res.end(`
        <html>
            <head>
                <meta charset = "utf-8">
                    <title>index page</title>
                </meta>
                <style>
                    #title {
                        text-align : center;
                        color : blue;
                        font-size : 80px;
                        }
                </style>
            </head>
            <body>
                <p id="title">Welcome to the index page!</p>
                <p>I have no idea what to write here.</p>
            </body>
        </html>
        `)})

app.get('/contact.html', (req, res)=>{
    res.end(`
            <html>
                <head>
                    <meta charset = "utf-8">
                        <title>index page</title>
                    </meta>
                    <style>
                        #title {
                            text-align : center;
                            color : blue;
                            font-size : 40px;
                            }
                        #body{
                            text-align: left;
                            color: crimson;
                            font-size : 20px;
                        }
                    </style>
                </head>
                <body>
                    <p id="title">Contact Me!</p>
                    <p id="body">My contact information </p>
                    <a href="mailto:javier_teo@mymail.sutd.edu.sg">Here.</a>
                </body>
            </html>
            `)
    })

app.get("*", (req,res) => {
    res.end(`
    <html>
        <head>
            <meta charset = "utf-8">
                <title>index page</title>
            </meta>
            <style>
                #title {
                    text-align : center;
                    color : Red;
                    font-size : 80px;
                    }
            </style>
        </head>
        <body>
            <p id="title">Error 404</p>
        </body>
    </html>
    `)
})
app.listen(5000)
