\# HelpDesk TI · Microsserviços



Sistema de chamados de TI (GLPI simplificado) migrado do \*\*monólito\*\* para \*\*microsserviços\*\*.

Atividade individual de \*\*Arquitetura de Software\*\* — Prof. Filipe Cavalcante.



\*\*Aluno:\*\* Valker Soares · \*\*Matrícula:\*\* 01291202 · \*\*Turma:\*\* quarto período A



\*\*Vídeo de demonstração:\*\* \[youtu.be](https://youtu.be/TfMXIS17TMQ)



\---



\## 1. Arquitetura



```mermaid

flowchart TB

&#x20;   Tela\[Tela do HelpDesk] --> Gateway\[API Gateway :8000]

&#x20;   Gateway --> SU\[Serviço de Usuários]

&#x20;   Gateway --> SI\[Serviço de Inventário]

&#x20;   Gateway --> SC\[Serviço de Chamados]

&#x20;   SC -->|HTTP| SU

&#x20;   SC -->|HTTP| SI

&#x20;   SU --> BU\[(Banco de usuários)]

&#x20;   SI --> BI\[(Banco de inventário)]

&#x20;   SC --> BC\[(Banco de chamados)]

&#x20;   SC -. evento ChamadoAberto .-> Fila\[\[Fila de eventos]]

&#x20;   Fila -.-> SN\[Serviço de Notificações]



