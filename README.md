# 🧩 Slime Escape

Um mini jogo em **Python + Pygame Zero**, onde você controla um **slime aventureiro** que precisa escapar pulando sobre plataformas e evitando inimigos até alcançar o **portal mágico da vitória!** 🟩✨  

---

## 🎮 Recursos do jogo
- Herói animado com sprites
- Movimento lateral e pulo com física de gravidade
- Inimigos patrulhando o mapa
- Portal de vitória com transição
- Menu principal com botões:
  - 🕹️ **Start Game**
  - 🎵 **Toggle Music**
  - ❌ **Exit Game**
- Sons e música de fundo

---

## 🕹️ Controles

| Tecla | Ação |
|-------|------|
| ← / → | Move o slime |
| Espaço | Pula |

---

## ⚙️ Instalação e execução

### 1️⃣ Clonar ou baixar o projeto
Baixe este repositório ou clone via terminal:

```bash
git clone https://github.com/SEU-USUARIO/SlimeEscape.git
cd SlimeEscape
(ou simplesmente extraia o arquivo ZIP em uma pasta, por exemplo C:\Users\acer\Downloads\Game)

2️⃣ Criar o ambiente virtual
Crie o ambiente dentro da pasta do jogo:

bash

python -m venv venv
3️⃣ Ativar o ambiente virtual
No Windows (cmd):

bash

venv\Scripts\activate
No PowerShell:

bash
Copiar código
.\venv\Scripts\Activate.ps1
Após ativar, você verá algo como:

(venv) C:\Users\Downloads\Game>
4️⃣ Instalar as dependências
Com o venv ativo, instale os pacotes necessários:

bash

pip install pgzero pillow
🔹 A biblioteca Pillow só é necessária se você for gerar ou editar as imagens do jogo.

5️⃣ Executar o jogo
Entre na pasta do jogo:

bash

cd slime_escape
E execute o jogo com:

bash

python -m pgzero game.py
Se tudo estiver certo, a janela do jogo se abrirá com o menu principal 🎉
