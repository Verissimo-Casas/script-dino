import os

def verificar_classe_person(arquivo_txt):
    with open(arquivo_txt, "r") as f:
        linhas = f.readlines()
    
    for linha in linhas:
        partes = linha.strip().split()
        if partes[0] == "person":
            return True
    return False

def remover_arquivos_nao_person(pasta_labels, pasta_imagens):
    for arquivo_txt in os.listdir(pasta_labels):
        if arquivo_txt.endswith(".txt"):
            caminho_arquivo_txt = os.path.join(pasta_labels, arquivo_txt)
            caminho_imagem = os.path.join(pasta_imagens, os.path.splitext(arquivo_txt)[0] + ".png")
            if not verificar_classe_person(caminho_arquivo_txt):
                if os.path.exists(caminho_imagem):
                    os.remove(caminho_imagem)
                os.remove(caminho_arquivo_txt)

def main():
    pasta_labels = "/home/getter-lab/Vídeos/new_dataset/labels/"
    pasta_imagens = "/home/getter-lab/Vídeos/new_dataset/images/"
    
    remover_arquivos_nao_person(pasta_labels, pasta_imagens)

if __name__ == "__main__":
    main()
