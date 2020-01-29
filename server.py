import socket
import threading
import os

def verificaArquivo(name, sock):				# funcao que vai verificar a existencia do arquivo solicitado
    nomeArq = sock.recv(1024)					# recebendo o nome do arquivo
    if os.path.isfile(nomeArq):					# se o arquivo for encontrado no diretorio
        sock.send("Confirmar " + str(os.path.getsize(nomeArq)))	# manda confirmacao e o tamanho do arquivo solicitado para o cliente
        resp = sock.recv(1024)					# recebe resposta de confirmacao
        if resp[:2] == 'OK':
            with open(nomeArq, 'rb') as f:			# abre o arquivo solicitado
                enviar = f.read(1024)				# variavel pra manter a leitura do arquivo
                sock.send(enviar)				# enviando arquivo pro cliente
                while enviar != "":				# o arquivo deve ser lido ate o final, pra ser enviado por completo
                    enviar = f.read(1024)			
                    sock.send(enviar)
    else:
        sock.send("Erro")

    sock.close()

def Main():
    host = ''
    port = 7081


    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	# criando socket tcp/ip
    server.bind((host,port))					# ligando o socket ao endereco especificado

    server.listen(3)						# preparando o server pra escutar ate 3 clientes

    print "Servidor pronto."
    while True:
        c, addr = server.accept()				# preparando pra aceitar conexoes
        print "cliente conectado IP: " + str(addr)		# le o ip do cliente que se conectou 
        t = threading.Thread(target=verificaArquivo, args=("RetrThread", c))	# chama a funcao pra pegar o arquivo
        t.start()
         
    server.close()

if __name__ == '__main__':
    Main()

