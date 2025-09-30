Analisador e Validador de Planilhas 📊
⚡ Um projeto para automatizar a análise e detecção de erros em grandes volumes de dados, transformando dias de trabalho manual em minutos de processamento automático.

🎯 Motivação

O Problema: No meu trabalho atual, uma tarefa rotineira era a análise manual de cadastros de clientes em planilhas com aproximadamente 30.000 linhas cada. Esse processo era lento, exaustivo e altamente suscetível a falhas humanas.

A Solução: Este projeto foi desenvolvido para automatizar essa verificação. A ferramenta valida os dados de forma rápida e precisa, transformando uma tarefa que demandava horas de trabalho em um processo que leva apenas minutos.


O método manual era:

Extremamente demorado, consumindo dias de trabalho da equipe.

Suscetível a falhas humanas, pois a detecção de pequenos erros em meio a milhares de dados é complexa.

Ineficiente, impedindo que a equipe se dedicasse a tarefas de maior valor estratégico.

💡 A Solução
Para resolver esse problema, este projeto oferece uma ferramenta automatizada que executa a validação completa das planilhas. A aplicação foi desenvolvida para:

Processar arquivos de forma rápida e simultânea.

Aplicar regras de validação customizáveis para identificar erros com precisão.

Gerar um relatório detalhado com as inconsistências encontradas, indicando a linha e a coluna do erro.

Salvar o tempo da equipe, reduzindo uma tarefa de dias para apenas alguns minutos.

✨ Principais Funcionalidades
Leitura de arquivos .xlsx: Suporte para os formatos de planilha mais comuns.

Validação de Dados: Verificação de tipos de dados, valores nulos, formatos específicos (CPF, datas), etc.

Relatório de Saída: Exportação de um novo arquivo com os erros claramente destacados para fácil correção.

Interface de Linha de Comando (CLI): Facilidade de uso para execução via terminal.

🛠️ Tecnologias Utilizadas
Linguagem: Python 3

Bibliotecas Principais:

Pandas: Para manipulação e análise de dados de alta performance.

Openpyxl: Para leitura e escrita de arquivos Excel (.xlsx).

🚀 Instalação e Uso
Siga os passos abaixo para executar o projeto em sua máquina local.

Pré-requisitos
Python 3.9 ou superior

Git

Passos
Clone o repositório:

Bash

git clone [URL_DO_SEU_REPOSITORIO_AQUI]
cd [NOME_DA_PASTA_DO_PROJETO]
Crie e ative um ambiente virtual (recomendado):

Bash

# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
Instale as dependências:

Bash

pip install -r requirements.txt
Execute o analisador:

Bash

python main.py
🤝 Como Contribuir
Contribuições são bem-vindas! Se você tiver ideias para melhorias ou encontrar algum problema, sinta-se à vontade para abrir uma issue ou enviar um pull request.

Faça um Fork deste repositório.

Crie uma nova Branch: git checkout -b feature/sua-feature.

Faça suas alterações e Commite: git commit -m "feat: Descrição da sua feature".

Envie para a sua Branch: git push origin feature/sua-feature.

Abra um Pull Request.


👤 Contato
Lucas mitto da costa

LinkedIn: linkedin.com/in/lucas-miotto-da-costa-23b973258

GitHub: https://github.com/euMiotto