
#! LISTAS

x = [0, 1, 2, 3]

x.append(4) #* add elemento na lista
x.insert(1, 'elemento') #* add elemento na posição 1
x.pop() #* remove o ultimo
del x[1] #* deleta o indice 1
x.remove('elemento') #* remove o elemento
x.count('elementos') #* conta quantos elementos achou
x.reverse() #* inverte a ordem
x.sort() #* organiza em ordem alfanumerica

#? lista = ['expression' for x in y] podendo ser condicional tb -> ['expression' for x in y 'condição']
y = [numero * 2 for numero in x] #* cria outra lista com o dobro dos valores de x 

#! POO

#* Declarando classes e chamando funções
class objeto:
    marca = 'x'
    valor = y
    cor = 'roxo'

    def exemplo():
        print("exemplo")

chamar_classe = objeto()
print(objeto.marca)
objeto.exemplo()

#* HERANÇA = pega todos os elementos da classe 'objeto' para evitar repetições 
class garrafa(objeto):
    conteudo = 'agua'
    tamanho = '500ml'

#* POLIMORFISMO DE CLASSE = modifica funções
class garfo(objeto):
    def exemplo():
        print("Exemplo modificado na class garfo")

#* POLIMORFISMO DE INTERFACE = imprime valores diferentes para cada valor passado
class fruta(objeto):
    def __init__(self, sabor):
        self.sabor = sabor
        return sabor + 'é gostoso'
sabor_fruta = fruta('doce')
