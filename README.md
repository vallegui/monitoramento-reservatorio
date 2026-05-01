# Sistema de Monitoramento de Reservatório 🌊

Este projeto é uma simulação de um sistema de controle de níveis de água, desenvolvido para a atividade de lógica de programação. O objetivo é monitorar o nível de um reservatório e exibir alertas coloridos no terminal conforme o risco.

## 🚀 Funcionalidades
- Monitoramento de 5 níveis de água.
- Alertas visuais utilizando cores (biblioteca `colorama`).
- Mensagens personalizadas para cada nível (Crítico, Baixo, Médio, Alto e Alerta).
- Reset automático da formatação do terminal.

## 🛠️ Tecnologias Utilizadas
- **Python 3**
- **Colorama**: Para estilização de cores no terminal.

## 📋 Níveis do Sistema
| Nível | Situação | Cor |
| :--- | :--- | :--- |
| 1 | Muito baixo (crítico) | Vermelho |
| 2 | Baixo | Amarelo |
| 3 | Médio | Verde |
| 4 | Alto | Ciano |
| 5 | Muito alto (alerta) | Azul |

## 🔧 Como executar
1. Certifique-se de ter o Python instalado.
2. Instale a biblioteca necessária:
   ```bash
   pip install colorama
