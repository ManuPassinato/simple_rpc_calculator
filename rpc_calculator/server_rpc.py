# server program
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

def sum(number1, number2):
	res = float(number1) + float(number2)
	return res

def sub(number1, number2):
	res = float(number1) - float(number2)
	return res

def mult(number1, number2):
	res = float(number1) * float(number2)
	return res
	
def div(number1, number2):
	res = float(number1) / float(number2)
	return res
	
def execute(function, number1, number2):
	return globals()[function.lower()](number1, number2)

def main():
	server = SimpleJSONRPCServer(('172.31.86.210', 12000))
	server.register_function(execute)
	print("Start server")
	server.serve_forever()
if __name__ == '__main__':  
    main()