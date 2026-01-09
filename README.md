# 📄 Análise de Cartão de Fraude com Python e Azure

Este projeto foi desenvolvido como parte de um **desafio prático da plataforma DIO**, com o objetivo de criar uma aplicação em **Python** capaz de realizar **upload de arquivos**, armazená-los no **Azure Blob Storage** e realizar **análise/validação de documentos** utilizando serviços de **Inteligência Artificial do Azure**, com interface web construída em **Streamlit**.

---

## 🚀 Tecnologias Utilizadas

- **Python 3**
- **Streamlit** – Interface web interativa
- **Azure Blob Storage** – Armazenamento de arquivos
- **Azure Document Intelligence** – Análise inteligente de documentos
- **python-dotenv** – Gerenciamento de variáveis de ambiente
- **Git & GitHub** – Versionamento de código

---

## 🧠 Funcionalidades

- 📤 Upload de arquivos (PDF, PNG, JPG, JPEG)
- ☁️ Armazenamento seguro no Azure Blob Storage
- 🔍 Preparação para análise de documentos via Azure Document Intelligence
- 🖥️ Interface web simples e intuitiva
- 🔐 Uso de variáveis de ambiente para proteger credenciais

---

## 📂 Estrutura do Projeto

```text
src/
│
├── app.py                  # Aplicação principal em Streamlit
├── requirements.txt        # Dependências do projeto
├── service/
│   └── blob_service.py     # Serviço de upload para Azure Blob Storage
│
├── .env.example            # Exemplo de variáveis de ambiente
└── .gitignore              # Arquivos ignorados pelo Git

⚙️ Configuração do Ambiente
1️⃣ Clone o repositório
git clone https://github.com/Joaombcoelho/Analise_de_Cartao_Fraude_Python.git
cd Analise_de_Cartao_Fraude_Python/src

2️⃣ Crie e ative um ambiente virtual (opcional, recomendado)
python -m venv .venv
source .venv/Scripts/activate  # Windows (Git Bash)

3️⃣ Instale as dependências
python -m pip install -r requirements.txt

4️⃣ Configure as variáveis de ambiente

Crie um arquivo .env na raiz do projeto com o seguinte conteúdo:

ENDPOINT=https://SEU-ENDPOINT.cognitiveservices.azure.com/
AZURE_STORAGE_CONNECTION_STRING=DefaultEndpointsProtocol=https;AccountName=SEU_ACCOUNT;AccountKey=SUA_KEY;EndpointSuffix=core.windows.net
SUBSCRIPTION_KEY=SUA_SUBSCRIPTION_KEY
CONTAINER_NAME=cartoes


⚠️ Importante:
Nunca versionar o arquivo .env. Ele já está listado no .gitignore.

▶️ Como Executar a Aplicação

No terminal, dentro da pasta src, execute:

python -m streamlit run app.py


A aplicação estará disponível em:

http://localhost:8501

🧪 Status do Projeto

✅ Upload de arquivos funcional

✅ Integração com Azure Blob Storage

🔄 Integração com Azure Document Intelligence em desenvolvimento

🔄 Validação de dados de cartão (simulação de fraude)

📌 Observações Importantes

Este projeto tem fins educacionais

Nenhuma credencial sensível deve ser exposta

Ideal para estudos de Cloud Computing, IA aplicada e Python

🎓 Contexto Educacional

Projeto desenvolvido como parte de um desafio prático da DIO (Digital Innovation One), com foco em:

Computação em Nuvem

Inteligência Artificial

Boas práticas de desenvolvimento

👨‍💻 Autor

João Manoel
Estudante de Engenharia de Software
Apaixonado por tecnologia, cloud e desenvolvimento backend 🚀

🔗 GitHub: https://github.com/Joaombcoelho

📄 Licença

Este projeto está sob a licença MIT.
Sinta-se à vontade para estudar, modificar e evoluir 🚀
