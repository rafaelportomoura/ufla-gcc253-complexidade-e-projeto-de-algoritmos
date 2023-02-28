# Questão 2: Planejamento de Alocação de Motoristas

A prefeitura de Parapuã possui **n** motoristas terceirizados. Todos os dias, é dever da Secretaria da Saúde programar o transporte de pacientes para hospitais e clínicas da região em **n** rotas matutinas e **n** rotas vespertinas. Cada motorista é responsável por exatamente uma rota matutina e uma rota vespertina.

Para qualquer motorista, caso o total percorrido pela sua rota exceda o instante de **x** horas, sua empresa terceirizada terá que pagar para o município para cada hora após o instante **x** um valor de **y** reais por hora ultrapassada.

Seu objetivo é determinar qual será o planejamento de rotas para cada motorista de forma que o possível valor extra pago pela empresa terceirizada seja minimizado.

## Entradas:

Cada linha contém três inteiros: n, x e y. As próximas duas linhas contém a duração estimada de cada rota matutina e vespertina, respectivamente. Todos os casos de teste finalizam com uma sequência de 3 zeros.

## Saídas:

Para cada caso de teste, imprima em uma linha separada qual é o valor mínimo a ser pago pela empresa terceirizada.

### Exemplo de Entrada:

```txt
2 20 5
10 15
10 15
2 20 5
10 10
10 10
0 0 0
```

### Exemplo de Saída:

```txt
50
0
```
