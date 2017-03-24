from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 8590),
                            requestHandler=RequestHandler)
server.register_introspection_functions()

# Register pow() function; this will use the value of
# pow.__name__ as the name, which is just 'pow'.

# Register a function under a different name

# Register an instance; all the methods of the instance are
# published as XML-RPC methods (in this case, just 'div').
def Follow(nome, topico):
	if(topico == "#sod"):
		arquivo=open('/home/vinicius/Desktop/UEL/Sistemas_Operacionais/Terceiro_Bimestre/Trabalho_RPC/Sistemas_Operacionais_Distribuidos_Usuarios.txt','a')
		arquivo.write(nome)
	elif(topico == "#cc"):
		arquivo=open('/home/vinicius/Desktop/UEL/Sistemas_Operacionais/Terceiro_Bimestre/Trabalho_RPC/Ciencia_da_Computacao_Usuarios.txt','a')
		arquivo.write(nome)
	elif(topico == "#cd"):
		arquivo=open('/home/vinicius/Desktop/UEL/Sistemas_Operacionais/Terceiro_Bimestre/Trabalho_RPC/Computacao_Distribuida_Usuarios.txt','a')
		arquivo.write(nome)
	arquivo.close()
	return 1

server.register_function(Follow, 'follow')

def Post(usuario, topico, texto):
	arquivo=open('/home/vinicius/Desktop/UEL/Sistemas_Operacionais/Terceiro_Bimestre/Trabalho_RPC/Posts.txt','a')
	if(topico == "#sod"):
		arquivo.write("TÓPICO: Sistemas Operacionais Distribuidos\nPOST:"+texto+"\n"+usuario+"---------------------------------\n\n")
	elif(topico == "#cc"):
		arquivo.write("TÓPICO: Ciência da Computação\nPOST:"+texto+"\n"+usuario+"---------------------------------\n\n")
	elif(topico == "#cd"):
		arquivo.write("TÓPICO: Computação Distribuida\nPOST:"+texto+"\n"+usuario+"---------------------------------\n\n")
	arquivo.close()
	return 1

server.register_function(Post, 'post')


def Unsubscribe(nome, topico):

	if(topico == "#sod"):
		arquivo=open('/home/vinicius/Desktop/UEL/Sistemas_Operacionais/Terceiro_Bimestre/Trabalho_RPC/Sistemas_Operacionais_Distribuidos_Usuarios.txt','r+')
	elif(topico == "#cc"):
		arquivo=open('/home/vinicius/Desktop/UEL/Sistemas_Operacionais/Terceiro_Bimestre/Trabalho_RPC/Ciencia_da_Computacao_Usuarios.txt','r+')
	elif(topico == "#cd"):
		arquivo=open('/home/vinicius/Desktop/UEL/Sistemas_Operacionais/Terceiro_Bimestre/Trabalho_RPC/Computacao_Distribuida_Usuarios.txt','r+')
	
	i = 0
	lista = range(1000)
	for line in arquivo:
		lista.insert(i,line)
		i=i+1
			
	return 1

server.register_function(Unsubscribe, 'unsubscribe')
# Run the server's main loop
server.serve_forever()
