# Secure Distributed Cloud Storage

## Project Group: Ankeet Saha and Jahnvi Shaw

The relay server for assignment 1 is contained in the folder `relayServer` under folder `assignment1`

**Usage**

To test the relay server, first run the dump server with the command

`python3 dump.py <host> <port>`

Next, run the relay server using the command

`python3 relay.py <host> <port> <dumpHost> <dumpPort>`

Finally, run the client with the command

`python3 client.py <clientHost> <clientPort>`

and input the message you desire to be sent
