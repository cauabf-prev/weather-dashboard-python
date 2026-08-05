#Importações de funções da pasta Weather.py
from api.weather import buscar_clima


continuar = True

while continuar:
    
 cidade = input("Qual cidade deseja consultar?")                   #Usuario deve inserir a cidade na qual deseja consultar o clima 

 resposta = buscar_clima(cidade)                          #Então chamamos a função buscar clima para que a API possa encontrar o clima da cidade

 dados = resposta.json()                                         #E em seguida nos devolve os dados em JSON e guarda na variavel DADOS

 temperatura_celcius = (dados["main"]["temp"])       #Aqui abrimos os dados e localizamos o que queremos MAIN->TEMP, nesse caso a temperatura

 local = (dados["name"])                                                                       

 umidade = (dados["main"]["humidity"])                                                      

 descrição = (dados["weather"][0]['description'])

#AGORA DEVEMOS PRINTAR TUDO PARA DARMOS A RESPOSTA AO USUÁRIO

 print(f"temperatura:{temperatura_celcius}")
 print(f"Local:{local}")
 print(f"umidade:{umidade}")
 print(descrição)


 confirmação = input("Deseja consultar novamente? S/N").strip().upper()
 if confirmação == "N":
    break

 elif confirmação != "S":
    invalides = input("Opção Inválida. Digite S/N").strip().upper()
 
   