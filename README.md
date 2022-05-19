# WEB DEVELOPMENT
This djangoProject is about important concepts of  web development. 

all designing procedures , technologies , architectures , 
protocols and frameworks that will be used in this project are going to be explained in details.

## University Sport Club
we are going to design a website for of a university sport club.

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



