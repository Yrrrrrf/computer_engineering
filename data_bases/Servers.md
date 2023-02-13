# Server
Is a piece of computer hardware or software that provides functionality for other programs or devices, called **clients**. This architecture is called the **client–server model**.
- The main duty of a server is hosting applications to send (as a [[http#Response|response]]) to the **client**.

![[Request Response.png]]

### Server types
##### Local Host
Inside our machine the local environment is created by our IP address & a port.
$default$ $port:$  $127.0.0.1:8000$ 

##### Infrastructure as a Service
This allow us to manipulate specific requierments for our proyect, this could be RAM, CPU, etc.
	- Amazon Web Services
	- Microsoft Azure
	- Digital Ocean (the cheapest)
This kind could be Virtual Private Server (superior yield) or Shared Hosting (cheaper).

##### Platform as a Service
This kind of server is managed by a company that that is responsible for keeping updated the dependencies of your application. (firewalls, dbs).
Just gives you an UI in which you'll ask for the **tools** that you need to run your application. 
Thinked **just to deploy**
	- Google Aee Engine
	- Firebase ([[nosql|NOSQL]])
	- Heroku

##### Sotfware as a Service
This kind of server offers you a complete application in which you won't need to code anything.
- Google Docs
- Slack
- WordPress

![[server types.png]]