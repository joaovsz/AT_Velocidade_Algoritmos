import os

def listar_arquivos_recursivo(diretorio):
    try:
        for item in os.listdir(diretorio):
            caminho_completo = os.path.join(diretorio, item)
            if os.path.isdir(caminho_completo):
                listar_arquivos_recursivo(caminho_completo)
            else:
                print(caminho_completo)
    except PermissionError:
        print(f"Sem permissão para acessar: {diretorio}")

pasta_inicial = "/home/joaovsz/Documentos/AT_Velocidade_Algoritmos"
print(f"Listando arquivos em '{pasta_inicial}':\n")
listar_arquivos_recursivo(pasta_inicial)
