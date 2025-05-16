# 🗓️ Conversor de Datas ISO ↔ BR

Um projeto web moderno e minimalista para conversão de datas entre os formatos americano e brasileiro.

---

## 🚀 Tecnologias Utilizadas

- 🐍 Python 3.11+
- ⚙️ Flask
- ✳️ Expressões Regulares (módulo `re`)
- 🔫 Gunicorn (produção WSGI)
- 🌐 HTML + CSS + JavaScript (front-end)
- ☁️ Railway (deploy)

---

## 📁 Estrutura do Projeto

📦 PROJETO_DATA
├── app.py # Aplicação Flask com lógica e rotas
├── Procfile # Comando de inicialização (para deploy)
├── requirements.txt # Dependências do projeto
├── README.md # Este arquivo
└── static/ # HTML, CSS e JavaScript


---

## ✅ Funcionalidades

- ✔️ Conversão de datas ISO (YYYY-MM-DD) para BR (DD/MM/YYYY)
- ✔️ Conversão de datas BR (DD/MM/YYYY) para ISO (YYYY-MM-DD)
- 🧠 Validação inteligente com expressões regulares
- 🔁 Suporte a anos bissextos (ex: 29/02/2020)
- 🧩 API RESTful com JSON
- 🎯 Interface simples, responsiva e direta ao ponto

---

## 💻 Como Rodar Localmente

```bash
# Clone o repositório
git clone https://github.com/Saraystein/PROJETO_DATA.git
cd PROJETO_DATA

# Crie e ative o ambiente virtual
# Para Windows
python -m venv venv
.\\venv\\Scripts\\Activate.ps1

# Para Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt

# Inicie o servidor
python app.py

# Acesse com seu navegador
http://127.0.0.1:5000


🔌 API - Endpoints
Método	Endpoint	JSON de Entrada	Resposta Esperada
POST	/convert/iso-to-br	{ "date": "2025-05-03" }	{ "converted": "03/05/2025" }
POST	/convert/br-to-iso	{ "date": "03/05/2025" }	{ "converted": "2025-05-03" }


☁️ Deploy Online
Acesse a aplicação hospedada na Railway:

🔗 https://projetodata.up.railway.app


👨‍💻 Autor
Gustavo Silvério Saray
📚 Projeto acadêmico – Cruzeiro do Sul Virtual
📧 Contato
[Gustavosaray2@gmail.com]