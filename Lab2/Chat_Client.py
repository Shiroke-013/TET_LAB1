import http.client
import sys

if len(sys.argv) != 3:
    print ("How to make it work: script, IP address, PORT number")
    exit()

# The first argument from the prompt is saved in IP_ADDRESS as a IP address.
IP_ADDRESS = str(sys.argv[1])

# The second argument from the prompt is saved in PORT as a port number.
PORT = int(sys.argv[2])

conn = http.client.HTTPConnection(IP_ADDRESS, PORT)

while True:
    while True:
        n_name = input("Nickname: ")
        if len(n_name) > 0:
            break
        else:
            print("Please enter a Nickname/Username")

    conn.request('POST',"/nickname", n_name.encode())
    r = conn.getresponse()
    if (r.status == 201):
        break
    else:
        print("Nickname already taken, try another one")

while True:
    try:
        while True:
            m = input("<{}>".format(n_name))
            print("m: ", m)
            if len(m) != 0:
                m = "<" + n_name + "> " + m
                conn.request("POST","/",m.encode())
                r = conn.getresponse()

            conn.request("POST","/getM",n_name.encode())
            r = conn.getresponse()
            d = r.read().decode()
            print(d)

    except KeyboardInterrupt as error:
        print("Keyboard Interruption... bye bye: {}".format(str(error)))
        conn.close()
        sys.exit()

conn.close()
