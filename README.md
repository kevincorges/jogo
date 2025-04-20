# 🟡 **Pacman Lite Edition**

**Pacman Lite Edition** é uma versão simplificada do clássico jogo Pac-Man, desenvolvida usando [PgZero](https://pygame-zero.readthedocs.io/en/stable/), uma biblioteca Python voltada para programação de jogos de forma fácil e educativa.

---

## ✨ **Funcionalidades**

- 🎮 Interface de menu com botões interativos:
  - ▶️ Iniciar jogo
  - 🔊 Ativar/Desativar som
  - ❌ Sair do jogo
- 🧱 Mapa fixo com paredes, pontos e inimigos
- 🚶‍♂️ Movimento suave e animado do jogador e dos inimigos
- ☠️ Derrota ao colidir com um inimigo
- 🏆 Vitória ao coletar todos os pontos
- 🎵 Música de fundo (opcional)
- 🔁 Reinício automático após vitória ou derrota

---

## ⚙️ **Requisitos**

- 🐍 Python 3.6 ou superior
- 🎮 [PgZero](https://pygame-zero.readthedocs.io/en/stable/)
- 
## ▶️ **Como Jogar**

Digite no terminal "pgzrun pacman.py" para poder executar o código do jogo

🎯 Controles:

Use as setas do teclado para mover o personagem

No menu, clique com o mouse nos botões:

▶️ Start Game

🔊 Sound: On/Off

❌ Exit

## 🧱 **Estrutura do Jogo**
Mapa: grade de 18x7 com os seguintes símbolos:

W = parede

. = ponto

P = jogador

E = inimigo

Estados do jogo:

menu, playing, win, game_over

Sprites:

Jogador e inimigos com animação alternada de dois frames

## 🗂️ **Recursos Esperados**
📁 Pasta images/:

hero_walk1.png

hero_walk2.png

enemy_walk1.png

enemy_walk2.png

wall.png

dot.png

📁 Pasta sounds/:

background.wav (ou .mp3, .ogg)

## 🧠 **Lógica Básica**
O jogador se move por células de grade se não houver uma parede.

Inimigos se movem aleatoriamente e mudam de direção ao bater em uma parede.

O jogador vence ao coletar todos os pontos.

O jogo termina em derrota se houver colisão com um inimigo.

## 📄 **Licença**
Este projeto é livre para fins educacionais.
Sinta-se à vontade para modificar, melhorar e compartilhar!


Instale pgzero com:

pip install pgzero



