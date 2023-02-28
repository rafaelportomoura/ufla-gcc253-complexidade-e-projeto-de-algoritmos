function calcula(m, v, horas, valor) {
  return v + m - horas < 0 ? 0 : (v + m - horas) * valor;
}

const IN = [
  {
    nome: '12',
    matutinas: [
      9485, 9192, 8049, 7719, 7273, 7174, 6996, 6669, 6564, 6504, 6229, 5448, 4953, 3887, 3844,
      3693, 3674, 3324, 3280, 3167, 3047, 3041, 2738, 2655, 2491, 2198, 1953, 1720, 1197, 655, 406,
      161,
    ],
    vespertinas: [
      660, 796, 933, 966, 1093, 1226, 1814, 1843, 2341, 2462, 2534, 2583, 3255, 3480, 3923, 4198,
      4559, 5181, 5453, 5769, 5984, 6060, 6536, 6775, 7365, 7386, 7957, 7971, 7987, 8536, 8592,
      9443,
    ],
    motoristas: 32,
    horas: 7682,
    valor: 3,
    esperado: 120393,
  },
  {
    nome: '72',
    horas: 9366,
    valor: 5,
    esperado: 52730,
    vespertinas: [
      74, 110, 992, 1045, 1222, 1788, 1852, 2182, 2283, 3152, 4710, 4920, 6078, 6151, 6241, 6479,
      7990, 8016, 8526, 9021, 9131, 9238, 9269, 9376, 9779, 9849,
    ],
    matutinas: [
      286, 612, 636, 675, 1593, 1708, 2082, 2245, 2309, 2332, 2758, 3269, 3493, 3834, 4101, 4111,
      4500, 4942, 5260, 5727, 7132, 7825, 8788, 8876, 8921, 9511,
    ],
    motoristas: 26,
  },
];

function add({ vespertinas, matutinas, motoristas, horas, valor, esperado, nome }) {
  console.log(nome);
  console.log(`Horas: ${horas}`);
  for (const matutina of matutinas) {
    k = vespertinas.map((u) => (u + matutina - horas < 0 ? 0 : (u + matutina - horas) * valor));
    console.log(k.join('\t'));
  }
  console.log();
  soma = 0;
  for (let i = 0; i < motoristas; i++) {
    k = [];
    for (let j = 0; j < motoristas; j++) {
      if (i == j) k.push(calcula(matutinas[i], vespertinas[j], horas, valor));
      else k.push('_');
    }
    console.log(k.join('\t'));
    soma += k.reduce((a, b) => (typeof b === 'number' ? b : a));
  }
  console.log(soma);
}

for (const iN of IN) {
  add(iN);
}
