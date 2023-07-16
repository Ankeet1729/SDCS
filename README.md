# Secure Distributed Cloud Storage

## Project Group: Ankeet Saha and Jahnvi Shaw

The relay server for assignment 1 is contained in the folder `relayServer` under folder `assignment1`

**Assignment1**

**Usage**

To test the relay server, first run the dump server with the command

`python3 dump.py <host> <port>`

Next, run the relay server using the command

`python3 relay.py <host> <port> <dumpHost> <dumpPort>`

Finally, run the client with the command

`python3 client.py <clientHost> <clientPort>`

and input the message you desire to be sent

**Assignment3**

**amicable.py usage**

`python3 amicable.py`

This would generate the required first 10 amicable pairs

**carmichael.py usage**

`python3 carmichael.py`

This code takes as input a number N from the user and prints all the carmichael numbers upto N in the form of a list

**4tuple.py usage**

`python3 4 tuple.py`

takes in a positive integer k as input from the user and outputs a 4-tuple (p, q, a, b), where p and q are distinct k-digit primes and a and b are integers such that ap + bq = 1
