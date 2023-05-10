# ChatPDF

## Introdução

Este projeto é uma demonstração de como usar a biblioteca Langchain para realizar perguntas e respostas em um documento PDF. O Langchain é uma biblioteca que fornece diversas ferramentas de processamento de linguagem natural, como incorporação de texto, busca de vetores e perguntas e respostas.

Esse projeto é uma adaptação do Notebook do youtuber Prompt Engineering:
[link para o notebook original](https://colab.research.google.com/drive/181BSOH6KF_1o2lFG8DQ6eJd2MZyiSBNt?usp=sharing)

## Configuração

Para executar este projeto, você precisará seguir estas etapas:

1. Clone o repositório.
2. Instale os pacotes necessários executando
```bash
pip install -r requirements.txt
```
(Eu recomendo a criação de um ambiente virtual)

3. Crie um arquivo chamado env.json no diretório raiz do projeto com sua chave de API do OpenAI. O modelo do arquivo está no arquivo `env.sample.json`
4. Baixe um documento PDF de exemplo e salve-o na pasta pdf do projeto. O código espera que o nome do arquivo seja `sample.pdf`.
5. Execute o arquivo `main.py` usando
```python
python main.py
```

## Como o processo funciona

O canal Prompt Engineering explica passo a passo a arquitetura e o processo. Recomendo que assista esse [vídeo](https://www.youtube.com/watch?v=TLf90ipMzfE&t=554s&ab_channel=PromptEngineering)