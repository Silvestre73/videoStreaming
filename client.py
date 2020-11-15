import socket
from os import system

# comentario

def opcaoFilme():
    print('Escolha o filme\n')
    print('[1] Back to the Future (1985)')
    print('[2] Back to the Future II (1989)')
    print('[3] Back to the Future III (1990)\n')
    opcao = input()
    if opcao not in (1, 2, 3):
        print('Opcao invalida')
        opcaoFilme()
    return str(opcao) + '.mp4'

def Main():
    host = 'localhost'
    port = 7081

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # criando socket tcp/ip
    client.connect((host, port))			       # conectando no host	

    nomeArquivo = opcaoFilme()
    if nomeArquivo != 'q':
        client.send(nomeArquivo)                               # enviando a escolha para o server
        data = client.recv(1024)			       # recebendo confirmacao do server
        if data[:9] == 'Confirmar':
            tamArquivo = long(data[9:])			       # variavel com o tamanho em bytes do arquivo recbido
            message = raw_input("Confirmar filme? " + nomeArquivo + "(s/n)")
            if message == 's':
                client.send("OK")				# enviando confirmacao pro server
                f = open('new_'+nomeArquivo, 'wb')		# criando arquivo vazio para escrever o arquivo a ser baixado
                data = client.recv(1024)			# recebendo o arquivo
                totalRecebido = len(data)			# variavel pra controlar a quantidade de bytes recebida
                f.write(data)					# escrevendo no arquivo criado
                while totalRecebido < tamArquivo:		# loop pra manter recebimento enquanto o server estiver enviando 
                    data = client.recv(1024)
                    totalRecebido += len(data)
                    f.write(data)
                    porcentagem = (totalRecebido/float(tamArquivo))*100 # calculando a porcentagem ja recebida do arquivo
                    print "Carregando: {:.2f}%".format(porcentagem)	# mensagem de carregamento
                f.close()
        else:
            print "Arquivo nao existe"
        
        comando = 'mplayer ' + nomeArquivo				# comando a ser executado no mplayer
        system(comando)							# executando o comando
	
    client.close()							# fechando a conexao					
    

if __name__ == '__main__':
    Main()

