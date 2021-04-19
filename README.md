# simple_rpc_calculator
Simple implementation of a rpc calculator in python
Python 3.8.9

To run you need to install **jsonrpclib**

	-- pip install jsonrpclib

Then you open two terminals and go to the folder where the files is

In the first terminal you run the server:

	-- python server_rpc.py

On the other you run the client

	-- python client_rpc.py $fuction $number1 $number2

Here we have 3 parameters

	**function** will recive the name of the math fuction implemented on the server [sum, sub, mult, div]

	**number1** the first number

	**number2** the second number

The program assums that the numbers every > 0 (this is on the requisits)

