# Case Técnico Dadosfera — AdventureWorks 
**Maria Clara**

Bem-vindo ao Case Técnico Dadosfera   
Este projeto tem como objetivo demonstrar, de forma prática, as capacidades da plataforma Dadosfera
ao longo de todo o ciclo de dados — da ingestão à análise e consumo — utilizando como base o dataset
**Microsoft AdventureWorks**.

Este README serve como guia principal do projeto, apresentando os itens do case, o status de cada etapa
e os links para as evidências desenvolvidas.

---

## 🎯 Objetivo do Case

Demonstrar um fluxo **end-to-end de dados**, contemplando:

- Integração e organização dos dados
- Exploração, qualidade e governança
- Modelagem analítica
- Análises de negócio
- Uso de GenAI e Data Apps
- Observabilidade e organização na Dadosfera

---

## 🧭 Estrutura Geral do Projeto

- 📓 **Notebook (Colab):** Integração, exploração, qualidade, modelagem e análises  
- 🌐 **Dadosfera:** Governança, catálogo, GenAI, pipelines e observabilidade  
- 📊 **Streamlit:** Aplicação interativa para consumo dos dados analíticos  

---

# 📌 Execução do Case por Item

---

## Item 0 — Agilidade e Planejamento ✅

**Atividades realizadas:**
- Planejamento do projeto utilizando Kanban
- Definição das etapas, dependências e status das atividades

🔗 **Kanban Board:**  
<https://github.com/users/Mariacfagundes/projects/4>
<img width="1450" height="695" alt="image" src="https://github.com/user-attachments/assets/d0e0b1a2-d24b-41c3-9a07-f93f2373d7f7" />


📎 **Evidência:**  
Planejamento organizado por status: Backlog, Em andamento, Bloqueado e Concluído.

---

## Item 1 — Base de Dados ✅

**Atividades realizadas:**
- Pesquisa e seleção de uma base de dados para execução do case end-to-end
- Escolha da base **Microsoft AdventureWorks**

**Justificativa:**
A base AdventureWorks é amplamente utilizada em cenários analíticos e permite explorar
modelagem dimensional, métricas de negócio e análises temporais.

🔗 Documentação oficial:  
https://learn.microsoft.com/en-us/sql/samples/adventureworks-install-configure

---

## Item 2 — Dadosfera | Integrar 🟡

**Atividades realizadas:**
- Upload inicial dos arquivos na plataforma Dadosfera
- Organização básica dos datasets

⚠️ **Observação:**  
A integração foi realizada de forma simplificada, sem automação.

**Próximos passos (bônus):**
- Automatizar ingestão via S3 ou base SQL transacional
- Aplicar microtransformações dentro da plataforma

📎 **Evidência:**  
<!-- prints da base carregada na Dadosfera -->

---

## Item 3 — Dadosfera | Explorar 🟡

**Atividades realizadas:**
- Catalogação dos datasets principais
- Construção de dicionário de dados
- Organização lógica dos dados seguindo conceito de Data Lake (raw, staging, analytics)

🔗 **Catálogo de dados:**  
<!-- link ou prints -->

📎 **Evidência:**  
Dicionário de dados documentado no notebook.

---

## Item 4 — Data Quality ✅

**Atividades realizadas:**
- Identificação de valores nulos e inconsistências
- Tratamento de tipos e padronização de colunas
- Registro das decisões de qualidade aplicadas

📎 **Relatório de Qualidade:**  
<!-- link markdown ou seção do notebook -->

🎯 **Resposta ao item 4:**  
Os principais problemas encontrados foram tratados na camada de staging.

---

## Item 5 — GenAI e LLMs 🟡

**Atividades planejadas:**
- Exploração de uso de IA sobre dados catalogados
- Aplicação de GenAI para sumarização ou geração de insights

⚠️ Item em desenvolvimento.

---

## Item 6 — Modelagem de Dados ✅

**Atividades realizadas:**
- Modelagem dimensional baseada na metodologia Kimball
- Definição de tabelas fato e dimensões

📎 **Evidência:**
- Dicionário de dados
- Explicação da modelagem no notebook

🎁 **Bônus planejado:**
- Diagrama visual do modelo dimensional

---

## Item 7 — Análise de Dados — Analisar 🟡

**Atividades realizadas:**
- Análises por categoria de produto
- Análises temporais de vendas
- Construção de métricas de negócio (receita, margem, lucro)

📎 **Evidência:**  
Consultas e visualizações disponíveis no notebook.

🎯 **Próximo passo:**
- Criar dashboards externos (ex: Metabase)

---

## Item 8 — Pipelines 🔴

**Status:** Não iniciado  
**Planejado:**  
- Construção de pipeline de processamento
- Catalogação do pipeline na Dadosfera

---

## Item 9 — Data Apps 🔴

**Status:** Não iniciado  
**Planejado:**  
- Desenvolvimento de aplicação em Streamlit
- Exploração interativa da camada analytics

---

## Item 10 — Apresentação do Case 🔴

**Planejado:**
- Gravação da apresentação do case
- Upload no YouTube
- Demonstração da solução end-to-end

---

## 🚀 Considerações Finais

Este projeto demonstra a aplicação prática da plataforma Dadosfera como solução central
para governança, análise, observabilidade e consumo de dados, evidenciando um fluxo completo
de dados alinhado a boas práticas de engenharia e analytics.
