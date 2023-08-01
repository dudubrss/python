#funções de entrada (input function)
#quando usamos o print, é um comando de saída de dados
#para ser impresso na tela do console
#para o console receber entrada de dados usa-se o input

#print ("qual o seu nome?")
#input ("qual o seu nome?") 

#não importa o que seja digitado pelo usuário, será convertido em string
#string = conjunto de caracteres
#nomes variam, portanto são variáveis
#uma variável é um método de armazenamento de dados para serem reutilizados
#o computador deve lembrar do nome quando um cliente disser

#name = "eduardo"
#a variável name foi criada assim que o = foi inserido
#dentro das aspas são criadas strings
#a variável name representa a string dentro das aspas

#print (name)
#será impresso a string dentro das aspas

#exercício para criar um robo atendente de uma loja
print ("hello, welcome to eduardo's coffe!!")
#print ("what is your name?")
#o conjunto de caracteres (string) que o usuário colocar será uma variável
#nesse caso tem que especificar que a string digitada pelo usuário será uma variável
name = input("what is your name?\n")
print ("hello " + name + " , thank you for coming in today.\n\n\n")
#pode-se também printar na tela do console através do input
#mas logo em seguida terá que haver uma entrada de dados do usuário
menu = "black coffe, espresso, latte, cappucino"
print (name + ", what would you like from our menu today? here is what we are serving. \n" + menu)
order = input ()
print ("sounds good " + name + ", we'll have that " + order + "  ready for you in a moment ")
