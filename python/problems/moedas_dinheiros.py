# Nao gostei disso (Google me deu essa)
def check_user_input(input):
    try:
        val = int(input)
        return True
    except ValueError:
        try:
            val = float(input)
            return True
        except ValueError:
            return False

# Taca moeda nessa poha
moedas = [0.50,0.25,0.10,0.05,0.01]

while(True):
    data = input("Coloca as moedinhas:\n")
    if(check_user_input(data)):
        dinheiro = float(data)
        break
    else:
        print("Dinheiro é numero po! Tenta denovo!")

faltadinheiro = dinheiro
quantasmoeda = 0
arrNmoedas = []
for x in moedas:
    if(faltadinheiro < x):
        arrNmoedas.append(0)
        continue
    else:
        rmoeda = faltadinheiro // x
        quantasmoeda += rmoeda
        faltadinheiro -= x * rmoeda
        faltadinheiro = round(faltadinheiro, 2)
        arrNmoedas.append(rmoeda)

print("O cofre recebe:", int(quantasmoeda), "moedas, sendo elas:")
for idx, x in enumerate(moedas):
    print(int(arrNmoedas[idx]), "moedas de:", x)