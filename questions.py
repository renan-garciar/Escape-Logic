
data_facil = {
    "Fase": ["1", "1", "1", "1", "1", "2", "2", "2", "2", "2"],
    "Subfase": [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
    "Pergunta": [
        "P -> Q significa que se P então Q. Se P é Falso, o que é Q?",
        "Se P v Q é verdadeiro e P é falso, o que é Q?",
        "Se P -> Q e Q -> R são verdadeiros, P -> R é:",
        "Se nem P nem Q são verdadeiros, P ^ Q é:",
        "Se P <-> Q é verdadeiro, e P é verdadeiro, então Q é:",
        "Todos os homens são mortais. Sócrates é um homem. Sócrates é:",
        "Existe um x tal que x é maior que 2. Isso significa que 3 > 2:",
        "Para todo x, se x é um pássaro, x pode voar. Pinguins são pássaros. Logo:",
        "Existe algum x tal que x é um peixe e x pode voar. Isso é:",
        "Para todos x, se x é um carro, então x tem rodas. Bicicletas têm rodas. Logo:"
    ],
    "Respostas": [
        ["Verdadeiro", "Falso", "Indeterminado", "Nenhuma das anteriores"],
        ["Verdadeiro", "Falso", "Indeterminado", "Nenhuma das anteriores"],
        ["Verdadeiro", "Falso", "Indeterminado", "Nenhuma das anteriores"],
        ["Verdadeiro", "Falso", "Indeterminado", "Nenhuma das anteriores"],
        ["Verdadeiro", "Falso", "Indeterminado", "Nenhuma das anteriores"],
        ["Mortal", "Imortal", "Indeterminado", "Nenhuma das anteriores"],
        ["Verdadeiro", "Falso", "Indeterminado", "Nenhuma das anteriores"],
        ["Podem voar", "Não podem voar", "Indeterminado", "Nenhuma das anteriores"],
        ["Verdadeiro", "Falso", "Indeterminado", "Nenhuma das anteriores"],
        ["Bicicletas são Carros", "Bicicletas não são carros", "Indeterminado", "Nenhuma das anteriores"]
    ],
    "Correta": [1, 0, 0, 1, 0, 0, 0, 1, 1, 1],
    "Dificuldade": ["Fácil"]*10
}

data_medio = {
    "Fase": ["1", "1", "1", "1", "1", "2", "2", "2", "2", "2"],
    "Subfase": [1, 2, 3, 4, 5, 1, 2, 3, 4, 5],
    "Pergunta": [
        "P -> Q é verdadeiro. Se Q é falso, o que é P?",
        "Se P v Q é falso e P é verdadeiro, o que é Q?",
        "Se P -> Q e Q -> R são falsos, P -> R é:",
        "Se P ^ Q é verdadeiro, o que é P e Q?",
        "Se P <-> Q é falso, e P é verdadeiro, então Q é:",
        "Alguns homens são mortais. Sócrates é um homem. Sócrates é:",
        "Para todo x, se x é maior que 2, então x é maior que 1. 1 é maior que 0:",
        "Para todo x, se x é um pássaro, x pode voar. Galinhas são pássaros. Logo:",
        "Existe algum x tal que x é um peixe e x pode nadar. Isso é:",
        "Para todos x, se x é um carro, então x tem rodas. Aviões têm rodas. Logo:"
    ],
    "Respostas": [
        ["Verdadeiro", "Falso", "Indeterminado", "Nenhuma das anteriores"],
        ["Verdadeiro", "Falso", "Indeterminado", "Nenhuma das anteriores"],
        ["Verdadeiro", "Falso", "Indeterminado", "Nenhuma das anteriores"],
        ["Ambos verdadeiros", "Ambos falsos", "Um verdadeiro, outro falso", "Indeterminado"],
        ["Verdadeiro", "Falso", "Indeterminado", "Nenhuma das anteriores"],
        ["Mortal", "Imortal", "Indeterminado", "Nenhuma das anteriores"],
        ["Verdadeiro", "Falso", "Indeterminado", "Nenhuma das anteriores"],
        ["Podem voar", "Não podem voar", "Indeterminado", "Nenhuma das anteriores"],
        ["Verdadeiro", "Falso", "Indeterminado", "Nenhuma das anteriores"],
        ["Aviões são carros", "Aviões não são carros", "Indeterminado", "Nenhuma das anteriores"]
    ],
    "Correta": [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    "Dificuldade": ["Médio"]*10
}
