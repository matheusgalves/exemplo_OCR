import pytesseract
from pdf2image import convert_from_path
import os

# Função para extrair o texto do PDF
def extrair_texto(pdf_caminho, caminho_output):
    # Converte o PDF para imagem
    imagens = convert_from_path(pdf_caminho)
    for i, img in enumerate(imagens):
        # Extrair texto da imagem
        texto_pagina = pytesseract.image_to_string(img, lang='por')
        output = os.path.join(caminho_output, f'page_{i+1}.txt')
        
        # Salvar o texto extraído em um TXT
        with open(output, 'w', encoding='utf8') as arq_txt:
            arq_txt.write(texto_pagina)
            
if __name__ == "__main__":
    # Declarando os argumentos para chamar a função
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    pdf_caminho = os.path.join(diretorio_atual, 'example_pdf.pdf')
    caminho_output = os.path.join(diretorio_atual, 'output')
    
    # Chama função para extrair o texto do PDF
    extrair_texto(pdf_caminho, caminho_output)