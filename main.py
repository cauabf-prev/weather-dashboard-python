#Importações de funções da pasta Weather.py
from api.weather import buscar_clima


continuar = True

while continuar:
    
 cidade = input("Qual cidade deseja consultar?")                   #Usuario deve inserir a cidade na qual deseja consultar o clima 

 clima = buscar_clima(cidade)                          #Então chamamos a função buscar clima para que a API possa encontrar o clima da cidade
 if clima is None:
    print("❌ Cidade inexistente")
    continue
  
 print(clima["cidade"])
 print(clima["temperatura"])
 print(clima["umidade"])
 print(clima["descrição"])


 confirmação = input("Deseja consultar novamente? S/N").strip().upper()
 if confirmação == "N":
    break

 elif confirmação != "S":
    invalides = input("Opção Inválida. Digite S/N").strip().upper()

 
   