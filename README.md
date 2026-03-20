# Geração de Arquivos Aleatórios de Provas - Quiz de Capitais do Brasil 

Este projeto em Python gera automaticamente múltiplas provas sobre **capitais dos estados brasileiros**, junto com seus respectivos gabaritos.

## Funcionalidades

* Gera **35 provas diferentes automaticamente**
* Cada prova contém:
  * 10 perguntas
  * 4 alternativas (A, B, C, D)
* Alternativas são embaralhadas aleatoriamente
* Ordem dos estados muda em cada prova
* Cria também um arquivo separado com o **gabarito**

## Estrutura dos Arquivos Gerados

Para cada prova, dois arquivos são criados:

```
capitalsquiz1.txt
capitalsquiz_answers1.txt

capitalsquiz2.txt
capitalsquiz_answers2.txt
...
```

* `capitalsquizX.txt` → Prova
* `capitalsquiz_answersX.txt` → Gabarito

## Como Executar

### 1. Pré-requisitos

* Python 3 instalado

### 2. Execute o script

```bash
python randomQuizGenerador.py
```

Após executar, os arquivos serão gerados na mesma pasta.

## Como Funciona

* Um dicionário (`capitals`) armazena os estados e suas capitais
* Para cada prova:
  * A lista de estados é embaralhada
  * 10 estados são selecionados
  * Para cada pergunta:
    * A resposta correta é definida
    * 3 respostas erradas são sorteadas
    * As alternativas são embaralhadas
* O gabarito é salvo separadamente

## Exemplo de Pergunta Gerada

```
1. Capital de Minas Gerais:

  A. Curitiba
  B. Belo Horizonte
  C. Recife
  D. Manaus
```
