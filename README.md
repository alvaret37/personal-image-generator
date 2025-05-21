# personal-image-generator

Geração de imagens personalizadas com seu próprio rosto utilizando APIs gratuitas de IA (como Replicate). Ideal para gerar avatares, montagens realistas ou simulações estéticas. Desenvolvido com foco em aprendizado e open source.

## 📦 Tecnologias usadas
- Python 3.10+
- API da Replicate
- IP-Adapter ou modelos de face swap
- dotenv

## ▶️ Como usar
1. Clone este repositório
2. Instale as dependências
3. Crie um `.env` com sua chave da API Replicate
4. Coloque a imagem base como `./input/input.jpg`
5. Execute:

```bash
python app/main.py --prompt "uma perna mecânica estilosa com meu rosto"
```

