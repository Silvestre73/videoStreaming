# videoStreaming

Aplicação cliente/servidor por linha de comando Linux para transmitir e executar arquivos de vídeo através do comando **mplayer**.

## Orientações
1. Deve-se instalar o **mplayer** com: **sudo apt-get install mplayer**
2. Se for rodar em duas máquinas diferentes, deve-se mudar o valor da variável "host" no arquivo **client.py** para o IP da máquina que for rodar o server
3. O valor da variável "port" deve ser o mesmo nos dois arquivos
4. Essa demonstração usou os filmes da trilogia "De Volta para o Futuro", que devem estar na mesma pasta que o **server.py**

## Para executar:
1. Abra um terminal e inicie o server com o comando: **python server.py**
2. Abra outro terminal e inicie o cliente com o comando: **python client.py**
