# WEB DEVELOPMENT
This djangoProject is about important concepts of  web development. 

all designing procedures , technologies , architectures , 
protocols and frameworks that will be used in this project are going to be explained in details.

## University Sport Club
This project is designed for website  of a  university sport club.

### OSI MODEL
![OSI-Model](https://user-images.githubusercontent.com/93463377/170128204-44847582-ceb6-420e-ade3-42afbd3a8ae8.png)

the communications between a computing system are split into seven different abstraction layers: Physical, Data Link, Network, Transport, Session, Presentation, and Application.

#### Physical Layer
The lowest layer of the OSI Model is concerned with electrically or optically transmitting raw unstructured data bits across the network from the physical layer of the sending device to the physical layer of the receiving device. It can include specifications such as voltages, pin layout, cabling, and radio frequencies. At the physical layer, one might find “physical” resources such as network hubs, cabling, repeaters, network adapters or modems.

#### Data Link Layer
At the data link layer, directly connected nodes are used to perform node-to-node data transfer where data is packaged into frames. The data link layer also corrects errors that may have occurred at the physical layer.

#### Network Layer
The network layer is responsible for receiving frames from the data link layer, and delivering them to their intended destinations among based on the addresses contained inside the frame. The network layer finds the destination by using logical addresses, such as IP (internet protocol). At this layer, routers are a crucial component used to quite literally route information where it needs to go between networks.

#### Transport Layer
The transport layer manages the delivery and error checking of data packets. It regulates the size, sequencing, and ultimately the transfer of data between systems and hosts. One of the most common examples of the transport layer is TCP or the Transmission Control Protocol.

#### Session Layer
The session layer controls the conversations between different computers. A session or connection between machines is set up, managed, and termined at layer 5. Session layer services also include authentication and reconnections.

#### Presentation Layer
The presentation layer formats or translates data for the application layer based on the syntax or semantics that the application accepts. Because of this, it at times also called the syntax layer. This layer can also handle the encryption and decryption required by the application layer.

#### Application Layer
The Application Layer is topmost layer in the Open System Interconnection (OSI) model. This layer provides several ways for manipulating the data (information) which actually enables any type of user to access network with ease. This layer also makes a request to its bottom layer, which is presentation layer for receiving various types of information from it. The Application Layer interface directly interacts with application and provides common web application services. This layer is basically highest level of open system, which provides services directly for application process.

##### Application Layer Protocols
1- TELNET

2- DNS

3- DHCP

4- SMTP

5- NFS

6- SNMP

7-HTTP

usually working with these protocols is not so easy therefore an interface is use which its name is API ( application programm interface)

### API
api and stateful stateless??? http? 7 layer nemoodar exchaning information

I have chosen Service Oriented Architecture for my project architecture

### SOA
Service-oriented architecture (SOA) is a type of software design that makes software components reusable using service interfaces that use a common communication language over a network. 

A service is a self-contained unit of software functionality, or set of functionalities, designed to complete a specific task such as retrieving specified information or executing an operation. It contains the code and data integrations necessary to carry out a complete, discrete business function and can be accessed remotely and interacted with or updated independently.

In other words, SOA integrates software components that have been separately deployed and maintained and allows them to communicate and work together to form software applications across different systems.

In this project a message broker is used in order to separate requests between various services.

#### NATS
NATS is an open-source, cloud-native, high-performance messaging system. At its core, it’s a Publish/Subscribe (PubSub) system whereby clients can communicate with one another without knowledge of where services are located or what their precise endpoints are. Clients simply publish/subscribe to a subject and NATS takes full responsibility for routing the messages.

#### NATS STREAMING
Where NATS provides at most once quality of service, streaming adds at least once. Streaming is implemented as a request-reply service on top of NATS.

In other words, Nats Streaming introduces message persistence & message delivery guarantees.



