d you know what happens when you type a website’s name into your browser?.
I'm going to talk about the different technologies that work together to make something as typing https://www.google.com into your browser provide you with the documents inside that website.

at first step we have the Domain name servers (DNS); but what are they? and what do they do? 
without DNS using the internet would be having to memorize a huge number of numbers(ip)
 
without it you would have to remember things like 8.8.8.8 instead of an easier www.google.com. thise numbers represent the address of a computer containing files and is called and IP address. 
For our browser to know where the website is located it will ask to the operating system.
If operating system does not know the location will ask the DNS resolver whose provide your computer with the right IP address where the website resides. 
The DNS resolver is given by the Internet Service Provider or ISP data center’s. 
If The DNS resolver don't know the correct IP because it goes and asks The Root Domain Name Server that will provide the resolver with the Top Level Domain IP address in this case the address for COM. 
The resolver will then ask the TLD if it knows the IP of the https://www.google.com but COM will not know the answer of the whole address, But what COM does know is where google.com resides and It will provides. 
The resolver will then go to one of the Authoritative Name Servers and that name server will provide the resolver with the right IP. The resolver return to the operating that said IP and the operating system will then pass it onto the browser. 
The browser will then go to the IP address.

what is HTTPS (Hypertext Transfer Protocol Secure). 
All the traffic going through this protocol is encrypted so if a malicious agent tries to acces to the information that is being transferred is imposible because information is encrypted. 
the computer and the server start a process call in which they will first agree on how to encrypt the data between them. The client(our pc) sends a message to the server, in that message contains the key to exchange method, 
the way data was encrypted between the two servers is called cypher, 
the hash which is used to generate the Message Authentication Code sent with the messages, the version of SSL that is being used and a random number used to create the master secret. which is used to calculate the encryption keys. 
The server response to the client agreeing to the specific key, cipher and hash method.then server sends to the client a certificate containing details about key to encrypt the data, and a public key.


HTTPS is possible thanks to SSL (Secure Socket Layer) which is the certificate that needs to be created to guarantee that the HTTPS connection are going through to a verified company. 

there are some pieces of the architecture behind websites like https://www.google.com. 
likes firewall, the Firewall is a piece of software or hardware system that monitors and controls traffic based on security rules established by an administrator. 

other piece of architecture is called Load Balancer. load balancer is to distribute traffic among different servers to prevent overwhelmed in the case of excesive traffic. 

web server are to serve static pages stored in the file system of the server itself, or make request to the application server for dynamic content. 
The application server takes in a request and process the data in that request sometimes needing to connect to a database to retrieve necessary data to form the content that the web server is requesting.
