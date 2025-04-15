
#  Sistema de Gestão Acadêmica – CLI em Python

# sistema-gestao-academica
Este projeto consiste em uma aplicação de linha de comando (CLI) desenvolvida em Python para simular um sistema de gestão acadêmica com persistência de dados utilizando arquivos .json. O sistema permite o gerenciamento completo de cinco entidades fundamentais de uma instituição de ensino: estudantes, professores, disciplinas, turmas e matrículas.

# Funcionalidades Implementadas

Menu interativo com navegação estruturada para cada módulo.
Operações CRUD (Create, Read, Update, Delete) completas para todas as entidades.
Validação de dados para garantir a unicidade dos códigos de identificação.
Separação de lógica por tipo de entidade (pessoas vs. estruturas acadêmicas).
Persistência de dados com leitura e escrita em arquivos JSON.
Manipulação de listas e dicionários para estruturação dos dados.


# Competências Técnicas Demonstradas

Programação estruturada com Python.
Manipulação de arquivos (I/O) e serialização com JSON.
Estruturas de controle, listas, dicionários e modularização de código.
Implementação de lógica de negócios para simular um sistema real de cadastro acadêmico.
Boas práticas de codificação com funções bem nomeadas e reutilização de código.

---

##  Funcionalidades

-  **Cadastro de Estudantes, Professores e Disciplinas**
-  **Atribuição de Professores e Estudantes a Turmas**
-  **Gerenciamento de Matrículas**
-  **Operações completas de CRUD** (Criar, Listar, Atualizar, Excluir)
-  **Persistência de dados** utilizando arquivos JSON
-  **Interface interativa no terminal**, com menus e entradas de dados
-  **Validação de códigos duplicados** para evitar registros redundantes

---

##  Tecnologias Utilizadas

- **Python 3.10+**
- Módulos nativos: `json`, `input`, `print`, `open()`

---

##  Estrutura do Projeto

```
sistema-gestao-academica/
├── src/
│   └── sistema.py             # Script principal com a lógica do programa
├── data/
│   ├── estudantes.json
│   ├── professores.json
│   ├── disciplinas.json
│   ├── turmas.json
│   └── matriculas.json
└── README.md                  # Documentação do projeto
```

---

##  Como Executar o Projeto

1. Certifique-se de ter o **Python 3.10+** instalado.
2. Clone o repositório:

```bash
git clone https://github.com/seuusuario/sistema-gestao-academica.git
```

3. Acesse a pasta do projeto e execute o programa:

```bash
cd sistema-gestao-academica/src
python sistema.py
```

4. Siga o menu interativo no terminal.

---

##  Autor

**Augusto Jubei Hoshino Rizzo**  
 Estudante de Análise e Desenvolvimento de Sistemas  
 Brasil  
 Conecte-se no [LinkedIn](https://www.linkedin.com/in/augusto-jubei-hoshino-rizzo-79948117b/)
