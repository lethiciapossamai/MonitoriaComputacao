def saudação():
    tarefa=input('Olá, como posso lhe ajudar?')
    resposta_01=input(f'Para lhe ajudar com {tarefa}, vou precisar de alguns dados, tudo bem?')
    if resposta_01=='Sim':
        print('Ótimo, vamos continuar!')
    else:
        print('Que pena, até a próxima!')
def pergunta_nome():
    nome=input('Me diga seu nome completo')
    return nome
def pergunta_idade():
    idade=int(input('Qual sua idade?'))
    if idade<18:
        print('Você é menor de idade, não será possível')
    return idade
def pergunta_email():
    email=input('Qual seu e-mail?')
    return email
def pergunta_confirmação(nomecerto, idadecerta, emailcerto):
    confirmação=input(f'Me confirme os seguintes dados: seu nome é {nomecerto}, sua idade é {idadecerta} e seu e-mail é {emailcerto}?')

def atendimento():
    saudação()
    pergunta_confirmação(pergunta_nome(), pergunta_idade(), pergunta_email())

atendimento()
#