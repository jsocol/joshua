================
Joshua Protocols
================

There are multiple protocols within Joshua, server-to-server, client-to-server,
and public-to-server. All three operate over HTTP and use HTTP verbs.


Server-to-Server
================

The server-to-server, or N2N, protocol in Joshua describes how nodes talk to
each other to exchange data.


Goals
-----

The N2N protocol MUST cover the following actions:

* Introduce a new node to the cluster.
* Passively replicate new data from any node.
* Actively replicate data to any node on demand.
* Passively propagate deletes from any node.


Client-to-Server
================

The client-to-server protocol describes how clients, such as web apps,
communicate with any given Joshua node.


Goals
-----

The client-to-server protocol MUST cover the following actions:

* Add a new file to the Joshua cluster.
* Delete a file from the cluster.

Communicating with *any* node MUST be sufficient.


Public-to-Server
================

This simple API describes how web browsers communicate with any Joshua node.


Goals
-----

The public-to-server protocol MUST cover the following actions:

* Conditional HTTP GET of resources.
