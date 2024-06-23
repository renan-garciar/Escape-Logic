# Documentação do Jogo de Lógica

Jogo de Lógica – Escape Room

## Autores

> Renan Garcia e Hericles Ferraz

### Público-alvo

> Estudantes de Pós Graduação, interessados em melhorar suas habilidades de raciocínio lógico e conhecimento sobre lógica proposicional e lógica de predicados.

### Conceito do Jogo

> O Jogo de Lógica é uma ferramenta educacional interativa projetada para testar e aprimorar o conhecimento dos jogadores em lógica proposicional e lógica de predicados. Através de perguntas e respostas, os jogadores são desafiados a aplicar conceitos de lógica de maneira prática e divertida, avançando por diferentes fases com dificuldade crescente.

### Conceitos Utilizados

Lógica Proposicional: Inclui conceitos como implicação, disjunção, conjunção, equivalência e negação.

Lógica de Predicados: Envolve a compreensão de quantificadores universais e existenciais, e a aplicação de predicados em diferentes contextos.

Artefatos Necessários para Executar o Jogo
Python 3.x

Streamlit: Para instalar, utilize o comando `pip install streamlit`.

Pandas: Para instalar, utilize o comando `pip install pandas`.

Arquivo de imagem: `image.webp` utilizado no cabeçalho do jogo.

### Como Jogar

1. Inicie o jogo: Abra o terminal e execute o comando `streamlit run app.py`.
2. Selecione a dificuldade: Escolha entre 'Fácil' ou 'Médio' na tela inicial.
3. Responda às perguntas: Cada fase contém 5 perguntas. Selecione a resposta correta para cada pergunta.
4. Avance nas fases: Você deve acertar pelo menos 4 de 5 perguntas para avançar para a próxima fase.
5. Complete o jogo: Após completar as duas fases, você verá uma mensagem de sucesso e terá a opção de voltar ao início.
Soluções das Tarefas do Jogo

Fase Fácil:

1. P -> Q significa que se P então Q. Se P é Falso, o que é Q?

   Resposta Correta: Falso

2. Se P v Q é verdadeiro e P é falso, o que é Q?

   Resposta Correta: Verdadeiro

3. Se P -> Q e Q -> R são verdadeiros, P -> R é:

   Resposta Correta: Verdadeiro

4. Se nem P nem Q são verdadeiros, P ^ Q é:

   Resposta Correta: Falso

5. Se P <-> Q é verdadeiro, e P é verdadeiro, então Q é:

   Resposta Correta: Verdadeiro

6. Todos os homens são mortais. Sócrates é um homem. Sócrates é:

   Resposta Correta: Mortal

7. Existe um x tal que x é maior que 2. Isso significa que 3 > 2:

   Resposta Correta: Verdadeiro

8. Para todo x, se x é um pássaro, x pode voar. Pinguins são pássaros. 
   Resposta Correta: Não podem voar

9. Existe algum x tal que x é um peixe e x pode voar. Isso é:
   Resposta Correta: Falso

10. Para todos x, se x é um carro, então x tem rodas. Bicicletas têm rodas. Logo:

    Resposta Correta: Carros


Fase Médio:
1. P -> Q é verdadeiro. Se Q é falso, o que é P?
   Resposta Correta: Verdadeiro
2. Se P v Q é falso e P é verdadeiro, o que é Q?
   Resposta Correta: Falso
3. Se P -> Q e Q -> R são falsos, P -> R é:
   Resposta Correta: Verdadeiro
4. Se P ^ Q é verdadeiro, o que é P e Q?
   Resposta Correta: Ambos verdadeiros
5. Se P <-> Q é falso, e P é verdadeiro, então Q é:
   Resposta Correta: Falso
6. Alguns homens são mortais. Sócrates é um homem. Sócrates é:
   Resposta Correta: Mortal
7. Para todo x, se x é maior que 2, então x é maior que 1. 1 é maior que 0:
   Resposta Correta: Verdadeiro
8. Para todo x, se x é um pássaro, x pode voar. Galinhas são pássaros. Logo:
   Resposta Correta: Não podem voar
9. Existe algum x tal que x é um peixe e x pode nadar. Isso é:
   Resposta Correta: Verdadeiro
10. Para todos x, se x é um carro, então x tem rodas. Aviões têm rodas. Logo:
    Resposta Correta: Não carros