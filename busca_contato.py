contatos = [
    {'nome': 'João Vitor', 'telefone': '6299249-5863'},
    {'nome': 'Luciana Araujo', 'telefone': '3481-1313'},
    {'nome': 'Adriana Pereira de Lima', 'telefone': '61999852536'},
]
def buscar_contato(contatos, nome):
    for numero in contatos:
        if numero['nome'].lower() == nome.lower():
            return f"Número de telefone de {nome}: {numero['telefone']}"
    return "Contato não encontrado."

nome = input("Digite o nome do contato: ")
print(buscar_contato(contatos, nome))
