const titulo = document.getElementById("tituloPrincipal");
const textos = ["O template feito para você!", "Não perca mais tempo!"];
let indice = 0;
let tempo = 1500; // 25 minutos
let intervalo;
let emFoco = true;
let demandas = 0;
let concluidas = 0;

setInterval(() => {
  indice = (indice + 1) % textos.length;
  titulo.textContent = textos[indice];
}, 4000);

console.log("Arquivo movimento.js carregado com sucesso!");

// /////////////////// Gráficos
if (document.getElementById("graficoTarefas")) {
  // Código do canvas
  const ctx = document.getElementById("graficoTarefas").getContext("2d");
  const grafico = new Chart(ctx, {
    type: "doughnut",
    data: {
      labels: ["Concluído", "Restante"],
      datasets: [
        {
          data: [concluidas, demandas],
          backgroundColor: ["#4285F4", "#222631"],
          borderWidth: 0,
        },
      ],
    },
    options: {
      cutout: "70%",
      responsive: true,
      plugins: {
        legend: { display: false },
        tooltip: { enabled: true },
      },
    },
  });

  function atualizarGrafico() {
    grafico.data.datasets[0].data = [concluidas, demandas - concluidas];
    grafico.update();
  }

  function adicionarTarefa() {
    const input = document.getElementById("entradaAtividades");
    const texto = input.value.trim();
    if (texto === "") {
      alert("Digite algo antes de adicionar!");
      return;
    }

    demandas++;

    const li = document.createElement("li");
    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";

    checkbox.onchange = function () {
      if (this.checked) {
        concluidas++;
      } else {
        concluidas--;
      }
      atualizarGrafico();
    };

    li.appendChild(checkbox);
    li.appendChild(document.createTextNode(" " + texto));
    document.getElementById("minhaLista").appendChild(li);

    input.value = "";
    atualizarGrafico();
  }
}

///////// Timer
function startTimer() {
  clearInterval(intervalo);
  intervalo = setInterval(() => {
    if (tempo > 0) {
      tempo--;
      atualizarDisplay();
    } else {
      emFoco = !emFoco;
      tempo = emFoco ? 1500 : 300; // 25min foco, 5min pausa
      document.getElementById("status").textContent = emFoco ? "Foco" : "Pausa";
      const div = document.getElementById("organizacao-left");
      div.className = `organizacao-left ${emFoco ? "foco" : "pausa"}`;
      console.log("TRocou de foco");
    }
  }, 1000);
}

function resetTimer() {
  clearInterval(intervalo);
  tempo = emFoco ? 1500 : 300;
  atualizarDisplay();
}

function atualizarDisplay() {
  let minutos = Math.floor(tempo / 60);
  let segundos = tempo % 60;
  document.getElementById("timer").textContent = `${minutos
    .toString()
    .padStart(2, "0")}:${segundos.toString().padStart(2, "0")}`;
}

//////////////// Frase motivacional 

async function carregarFrases() {
  try {
    const response = await fetch("http://127.0.0.1:5000/motivacional"); // troque pela URL da sua API se for hospedada
    const data = await response.json();

    const frasesDiv = document.getElementById("frases");
    frasesDiv.innerHTML = ""; // Limpa frases anteriores

    data.frases.forEach((frase) => {
      const p = document.createElement("p");
      p.className = "frase";
      p.textContent = frase;
      frasesDiv.appendChild(p);
    });
  } catch (error) {
    console.error("Erro ao carregar frases:", error);
  }
}

// Carrega frases ao abrir e depois a cada 10 segundos
carregarFrases();
setInterval(carregarFrases, 10000);