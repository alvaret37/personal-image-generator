
# 🎨 Personal Image Generator 🧑‍🎨🦿

Este é um projeto de estudo que permite **gerar imagens personalizadas** (ex: com rosto do usuário ou prótese estética) a partir de **fotos reais fornecidas pelo próprio usuário**, utilizando **APIs gratuitas de inteligência artificial** para geração de imagens realistas.

---

## 🧠 O que o projeto faz?

Permite que o usuário envie uma ou mais fotos pessoais e gere variações dessas imagens (ex: vestindo roupas específicas, adicionando próteses, estilos etc), usando **modelos de AI da Replicate**, tudo de forma simples e gratuita.

---

## ✅ Funcionalidades

- Upload de imagens pessoais (por exemplo, rosto ou perna)
- Geração de variações realistas com base em prompts personalizados
- Integração com API gratuita da **Replicate**
- Interface via terminal
- Criação automática de imagem gerada (salva em disco)

---

## 🧰 Requisitos

- Python 3.8+
- Conta na Replicate (gratuita)
- Pip + ambiente virtual (recomendado)

---

## 🔐 Configurando a chave da Replicate

1. Crie um arquivo `.env` na raiz do projeto:

```
REPLICATE_API_TOKEN=sua-chave-aqui
```

2. Obtenha sua chave em:  
👉 https://replicate.com/account/api-tokens

---

## 🚀 Como usar

1. Clone o projeto ou baixe o ZIP  
2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Coloque suas imagens na pasta `data/input/`  
   (por exemplo: `minha_perna.jpg`, `meu_rosto.png`)

4. Rode o app:

```bash
python app/main.py
```

5. Digite o prompt desejado (ex: “me mostre com uma prótese moderna de perna”).  
   A imagem gerada será salva na pasta `data/output/`.

---

## 📁 Estrutura

```
personal-image-generator/
│
├── app/
│   ├── main.py
│   ├── replicate_client.py
│   └── utils.py
│
├── data/
│   ├── input/     ← coloque suas imagens aqui
│   └── output/    ← imagem gerada será salva aqui
│
├── .env
├── requirements.txt
└── README.md
```

---

## 🧑‍💻 Feito por

Álvaro (projeto de estudo usando OpenAI + Replicate)  
📧 alvaro.emmanoel@gmail.com
