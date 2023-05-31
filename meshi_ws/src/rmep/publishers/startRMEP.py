#!/usr/bin/env python3

import socket
import sys
sys.version_info


# In direct connection mode, the default IP address of the robot is 192.168.2.1 and the control command port is port 40923.
host = "192.168.2.1"
port = 40923

def main():

        address = (host, int(port))

        # Establish a TCP connection with the control command port of the robot.
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        print("Connecting...")

        s.connect(address)

        print("Connected!")

        while True:

                msg = input(">>> please input SDK cmd: ")
                # Wait for the uf.decode('utf-8'))
                
                # When the user enters Q or q, exit the current program.
                if msg.upper() == 'Q':
                        break

                # Add the ending character.
                msg += ';'

                # Send control commands to the robot.
                s.send(msg.encode('utf-8'))
            

                try:
                        # Wait for the robot to return the execution result.
                        buf = s.recv(1024)

                        print(buf.decode('utf-8'))
                except socket.error as e:
                        print("Error receiving :", e)
                        sys.exit(1)
                if not len(buf):
                        break

        # Disconnect the port connection.
        s.shutdown(socket.SHUT_WR)
        s.close()


if __name__ == '__main__':
        assert sys.version_info >= (3, 7)
        print(sys.version) 
        main()



