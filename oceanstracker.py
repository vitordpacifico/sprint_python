# lista das regiões dos oceanos e suas temperaturas mínimas e máximas
temperatura_oceanos = {
    "Atlântico do Norte": {"min": 0, "max": 25},
    "Atlântico Central": {"min": 20, "max": 30},
    "Atlântico Sul": {"min": 15, "max": 28},
    "Pacífico Norte": {"min": 5, "max": 20},
    "Pacífico Central": {"min": 24, "max": 30},
    "Pacífico Sul": {"min": 18, "max": 28},
    "Índico": {"min": 22, "max": 28},
    "Ártico": {"min": -2, "max": 6},
    "Antártico": {"min": -2, "max": 2},
    "Próximo à Antártida (Atlântico Sul)": {"min": -2, "max": 5}
}

registros_salvos = []

def checagem_temperatura(regiao, temperatura):
    if regiao not in temperatura_oceanos:
        return f"A região {regiao} não foi encontrada."

    limite_temperatura = temperatura_oceanos[regiao]
    temperatura_minima = limite_temperatura["min"]
    temperatura_maxima = limite_temperatura["max"]

    if temperatura_minima <= temperatura <= temperatura_maxima:
        return None
    else:
        return f"A temperatura {temperatura}°C está fora da faixa padrão para a região {regiao}."

def analise_objetos(leitura_distancia):
    if not leitura_distancia:
        return "Dados obtidos insuficientes."

    if leitura_distancia < 125:
        return "Um ser vivo em movimento."
    else:
        return "Detritos no mar."

def escolha_regiao():
    print("Regiões disponíveis:")
    for idx, regiao in enumerate(temperatura_oceanos.keys(), 1):
        print(f"{idx}. {regiao}")

    escolha = input("Escolha a região digitando o número correspondente: ")
    while not (escolha.isdigit() and 1 <= int(escolha) <= len(temperatura_oceanos)):
        print("Escolha inválida. Por favor, tente novamente.")
        escolha = input("Escolha a região digitando o número correspondente: ")

    regiao_selecionada = list(temperatura_oceanos.keys())[int(escolha) - 1]
    return regiao_selecionada

def sistema_monitoramento():
    print("Bem-vindo ao Sistema de Monitoramento Ambiental da OceansTracker++!\n")
    
    distancia = input("Digite a distância captada pelo sensor ultrassônico (até 400 cm): \n")
    while not (distancia.replace('.', '', 1).isdigit() and 0 <= float(distancia) <= 400):
        print("Entrada inválida. Por favor, digite um número correto.")
        distancia = input("Digite a distância captada pelo sensor ultrassônico (até 400 cm): \n")
    distancia = float(distancia)

    temperatura = input("Digite a temperatura captada pelo sensor de temperatura (em °C): \n")
    while not temperatura.replace('.', '', 1).isdigit():
        print("Entrada inválida. Por favor, digite um número válido.")
        temperatura = input("Digite a temperatura captada pelo sensor de temperatura (em °C): \n")
    temperatura = float(temperatura)

    regiao = escolha_regiao()

    objetos_detectados = analise_objetos(distancia)
    temperatura_obtida = checagem_temperatura(regiao, temperatura)

    entrada = {
        "distancia": distancia,
        "temperatura": temperatura,
        "regiao": regiao,
        "objetos_detectados": objetos_detectados,
        "temperatura_obtida": temperatura_obtida
    }
    registros_salvos.append(entrada)

    print(f"\nResultado do monitoramento:")
    if objetos_detectados:
        print("Detectado:", objetos_detectados)
    if temperatura_obtida:
        print("Alerta da temperatura marítma:", temperatura_obtida)
    else:
        print(f"A temperatura {temperatura}°C está na faixa normal para a região {regiao}.")

    print("\nMonitoramento registrado com sucesso!.")

def exibir_registros_salvos():
    if not registros_salvos:
        print("Nenhuma entrada foi salva por enquanto.")
        return
    
    for entrada in registros_salvos:
        print("\n-----------------------------")
        print(f"Distância: {entrada['distancia']} cm")
        print(f"Temperatura: {entrada['temperatura']}°C")
        print(f"Região: {entrada['regiao']}")
        if entrada['objetos_detectados']:
            print(f"Objeto detectado: {entrada['objetos_detectados']}")
        if entrada['temperatura_obtida']:
            print(f"Alerta de temperatura: {entrada['temperatura_obtida']}")
        else:
            print(f"A temperatura {entrada['temperatura']}°C está dentro da faixa normal para a região {entrada['regiao']}.")
        print("-----------------------------")

def menu_principal():
    while True:
        print("\nMenu do OceansTracker++:")
        print("1. Monitorar o ambiente")
        print("2. Ver as entradas salvas")
        print("3. Sair do programa")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            sistema_monitoramento()
        elif escolha == '2':
            exibir_registros_salvos()
        elif escolha == '3':
            print("Saindo da aplicação!")
            break
        else:
            print("Escolha inválida. Selecione uma das três opções disponíveis.")

# executa o menu do sistema até a finalização do programa  
menu_principal()
