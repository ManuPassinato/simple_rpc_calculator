# Call by client
import sys
from jsonrpclib import Server
def main():
    conn = Server('http://172.31.86.210:12000')
    parameters = sys.argv[1:]
    function = parameters[0]
    number1 = parameters[1]
    number2 = parameters[2]
    print("calling: " + function + '(' + number1 + ', ' + number2 + ')')
    print(conn.execute(function, number1, number2))

if __name__ == '__main__':
    main()