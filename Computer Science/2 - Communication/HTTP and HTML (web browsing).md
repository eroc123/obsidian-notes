---
tags:
  - comsci/chapter-2
---

**HTTP** - **H**yper**T**ext **T**ransfer **P**protocol - langauge that computers uses
- Requests that are sent by a computer such as GET requests and POST requests are examples of HTTP methods.
**HTTPS** - **H**yper**T**ext **T**ransfer **P**rotocal **S**ecure - HTTP but secured with [[Secure Socket Layer]] and [[Transport Layer Security]]
**HTML** - Code used in order to "draw" a website 
**Cookie data** - An ID number that is saved by the browser (your computer browser) 
- It is sent by the website to your browser and can be used to identify you next time you access the website.
### Process when web browsing (entering a URL)
1. Once a URL is entered in and the web server is found (check [[IP address]] as a reminder on how a computer finds a web server)
	- Servers can be thousands of miles away, yet the communication remains instantaneous
2.  Computer sends HTTP **GET** requests to the server.
	- Get requests is the computer asking the web server for information such as document name and the HTML code of the website 
	- For example GET /login (sent from a computer) is like asking the web server for the HTML for the login page, which the web server then sends back to the computer.
3. Once the computer has recieved the HTML code, the computer can load the website on the web browser that was used.
	- Other parts such as images, videos and sound files need to be requested seperately with their own HTTP **GET** requests
	- Computer does this by sending more HTTP **GET** requests to the webpage
	- The webpage then sends the information back, which can then be loaded as images or videos on the website
### Process when sending information to a loaded web page
1. When the user enters information via a search query or a form, it gets sent via plain text
	- Uses a HTTP **POST** request to send plain text information to the web server
	- e.g. when logging in, the web server processes the HTTP **POST** request and can thus identify your identity
2. The website then sends back a response, plus **cookie data** that can be saved by the browser