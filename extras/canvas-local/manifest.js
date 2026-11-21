// Manifesto do canvas — mantido pelo agente designer. UM canvas por projeto: toda tela nova entra aqui.
// Cada tela é um HTML autônomo em screens/<id>.html (sem dependências externas).
window.CANVAS = {
  project: "Meu projeto",
  version: 0,
  updated: "",
  direction: "",            // direção estética em 1–2 frases
  tokens: {
    colors: {},             // { "fundo": "#0f1020", "destaque": "#ff4fa3" }
    fonts: {},              // { "títulos": "Space Grotesk 700", "texto": "Inter 400" }
    other: {}               // { "raio": "12px", "espaçamento": "8px base" }
  },
  screens: [
    // { id: "home", title: "Início", group: "Site", file: "screens/home.html",
    //   status: "novo" | "revisao" | "aprovado" | "mudar", notes: "o que observar", links: ["galeria"] }
  ],
  history: [
    // { version: 1, date: "2026-11-20", summary: "Primeira versão: home e galeria" }
  ]
};
