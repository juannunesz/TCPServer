import socket
def server(host = 'localhost', port=5000):
    data_payload = 2048 #A quantidade máxima de dados a serem recebidos de uma vez
    # Cria um TCP socket
    sock = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
    # Habilita reuso de endereço/porta
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # de para socket á porta
    server_address = (host, port)
    print ("Iniciando o servidor em %s porta %s" % server_address)
    sock.bind(server_address)
    # Ouvindo clients, argumento especifica o no máximo. de conexões na fila
    sock.listen(5) 
    i = 0
    while True: 
        print("Esperando receber mensagem do cliente")
        client, address = sock.accept() 
        data = client.recv(data_payload) 
        if data:
            print("Data: %s" %data)
            client.send(data)
            print("sent %s bytes back to %s" % (data, address))
            # fechando conexão
            client.close()
            i+=1
            if i>=3: break           
server()