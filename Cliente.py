import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8590')

var = 1
while var == 1:
	opcao = input("1 - Ingressar em tópico\n2 - Fazer um post\n3 - Deixar de seguir um determinado tópico\n0 - Sair\nOpcao:")
	if (int(opcao) == 0):
		break
	elif(int(opcao) == 1):
		Username = ("@" + input("Digite o nome do usuário:")+"\n")
		Topico = ("#" + input("Digite o tópico em que quer participar:"))
		l = s.follow(Username,Topico)
	elif(int(opcao) == 2):
		Username = ("Postado por: "+"@" + input("Nome do usuário:")+"\n")
		Topico = ("#" + input("Tópico em que fará o post:"))
		Texto = (input("Texto a ser postado:"))
		l = s.post(Username, Topico, Texto)
	elif(int(opcao) == 3):
		Username = ("@" + input("Digite o nome do usuário:")+"\n")
		Topico = ("#" + input("Digite o tópico em que deseja deixar de seguir:"))
		l = s.unsubscribe(Username, Topico)
 #Print (list of available methods)
#print s.system.listMethods()
