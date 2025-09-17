# 🚀 Mood Script

Bem-vindo ao repositório do Mood Script!  
Este projeto utiliza **Python** e **Streamlit** para rodar uma aplicação com integração à a API do **Gemini (Google AI)**.  

📌 **Me siga e acompanhe meus conteúdos:**  
- [💼 LinkedIn](https://www.linkedin.com/in/jeanldcarneiro/)  
- [📺 YouTube](https://www.youtube.com/@JeanLucasSoftwareDev)  

---

## ☕ Me pague um cafézinho ☕️
Se este projeto te ajudou e você gostaria de apoiar:  

**PIX:** `01708003266`  

---

## 🛠️ Pré-requisitos

- **Python 3.10+** (recomendado **Python 3.12**)
- Conta no [Google AI Studio](https://ai.google.dev/) para obter sua **API Key do Gemini**

---

## 📦 Instalação

### 1️⃣ Clone o repositório
```bash
git clone git@github.com:carneirojeanl/mood-script.git
cd mood-script
```

### 2️⃣ Crie um ambiente virtual
```bash
python3.12 -m venv .venv
```

### 3️⃣ Ative o ambiente virtual
- **Windows (PowerShell):**
  ```bash
  .venv\Scripts\Activate
  ```
- **Mac/Linux (bash/zsh):**
  ```bash
  source .venv/bin/activate
  ```

### 4️⃣ Instale as dependências
```bash
pip install -r requirements.txt
```

### 5️⃣ Configure variáveis de ambiente
Crie um arquivo `.env` na raiz do projeto com sua chave da API do Gemini:

```env
GOOGLE_API_KEY=coloque_sua_chave_aqui
```

### 6️⃣ Rode a aplicação
```bash
streamlit run main.py
```

---

## ⚠️ Observações importantes
- Caso esteja utilizando o **Gemini gratuito**, haverá **limitação no número de chamadas** para a API.  
- Se quiser sugerir melhorias ou reportar bugs, basta abrir uma **[Issue](../../issues)**.  

---
