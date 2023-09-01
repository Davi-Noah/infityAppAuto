from webbrowser import open
from os import system

def criarMensagem(bruto):
    horario, aluno, telefone, metodo, data = bruto.split(" - ")
    if metodo == 'Particular':
        aux = 'particular'
        metodo = 'Também queria saber se sua aula é presencial ou online'
    else:
        aux = 'de reposição'
        auxiliar = metodo
        metodo = f'Também queria confirmar se sua aula é {auxiliar}'

    mensagem = (f'Opa, tudo bom {aluno}? Aqui é o Davi monitor da Infinity, estou entrando em contato para confirmar sua aula {aux} dia *{data}* as *{horario}* hrs. {metodo}, e perguntar *qual seria o módulo e a aula da reposição.*')
    link = f'https://api.whatsapp.com/send?phone=55{telefone}'
    open(link)
    system(f'echo {mensagem} | clip')
    return mensagem, link

