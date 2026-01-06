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

## Item 2 — Dadosfera | Integrar ✅

**Atividades realizadas:**
- Upload dos arquivos da base AdventureWorks na plataforma Dadosfera
- Criação do dataset `casetecnico_mariaclara`
- Disponibilização das tabelas para exploração e análise

**Estratégia adotada:**
A integração inicial foi realizada de forma simplificada, priorizando agilidade no setup do case.
Em um cenário produtivo, essa ingestão poderia ser automatizada via S3 ou conexão com base transacional,
com aplicação de microtransformações na camada de ingestão.

📎 **Evidências:**
- Print do dataset na Dadosfera
- Print de algumas das tabelas carregadas

📎 **Evidência:**  
<img width="1477" height="660" alt="image" src="https://github.com/user-attachments/assets/57fc98f4-ca8b-42f9-ae4b-e4469bb7122e" />

https://app.dadosfera.ai/pt-BR/collect/pipelines/aec2673c-8f97-47e8-ba72-f2dc18e898d8

<<img width="1513" height="706" alt="image" src="https://github.com/user-attachments/assets/e5a0bac3-169a-4fe7-9bc2-5aa7d88ecd4f" />

https://app.dadosfera.ai/pt-BR/catalog/data-assets/3de32759-694d-47f6-8583-5906f511c379

<<img width="1505" height="701" alt="image" src="https://github.com/user-attachments/assets/e91ee844-cfbd-48ea-b5cd-1ecd71d693a7" />

https://app.dadosfera.ai/pt-BR/catalog/data-assets/23c16621-4138-4447-9f62-acbf1473fc17


>

---

## Item 3 — Dadosfera | Explorar ✅

**Atividades realizadas:**
- Catalogação das tabelas carregadas na plataforma Dadosfera
- Descrição funcional de cada dataset diretamente no catálogo
- Exploração inicial dos dados para entendimento de schema, tipos e granularidade
- Criação de dicionário de dados documentado no notebook do projeto

**Observações:**
- A descrição detalhada das colunas foi documentada externamente no notebook, servindo como dicionário de dados oficial do projeto
- A organização dos dados segue o conceito de Data Lake, documentado de forma conceitual

**Organização conceitual do Data Lake:**
- **Raw:** arquivos CSV originais, sem tratamento
- **Staging:** dados tratados, padronizados e com tipos ajustados
- **Analytics:** camada destinada à modelagem dimensional e consumo analítico

📎 **Evidências:**
- Print do catálogo de datasets na Dadosfera com descrições preenchidas
- Dicionário de dados disponível no notebook do projeto

https://app.dadosfera.ai/pt-BR/catalog/data-assets?pipeline_id=aec2673c-8f97-47e8-ba72-f2dc18e898d8&pipeline_name=casetecnico_mariaclara&tags=&asset_types=&page=1&sort=az
<img width="1226" height="667" alt="image" src="https://github.com/user-attachments/assets/3ff55402-c317-4f2d-addd-8672241b5fb6" />

https://app.dadosfera.ai/pt-BR/catalog/data-assets/80e4a7dd-2120-4a47-bf8d-2eaadbad1b10
<img width="1529" height="688" alt="image" src="https://github.com/user-attachments/assets/1821fbfb-d592-4ed0-8acc-38a74ebb55b0" />

https://app.dadosfera.ai/pt-BR/catalog/data-assets/23c16621-4138-4447-9f62-acbf1473fc17
<img width="1524" height="663" alt="image" src="https://github.com/user-attachments/assets/2f4e18ed-1a07-4a92-9d72-24ddc1fc389c" />

https://app.dadosfera.ai/pt-BR/catalog/data-assets/bc9a9d26-23d9-4d0c-af21-dbc7efbd034c
<img width="1513" height="668" alt="image" src="https://github.com/user-attachments/assets/6a87d324-b2d9-4215-a798-2a0256cbc525" />

https://app.dadosfera.ai/pt-BR/catalog/data-assets/3de32759-694d-47f6-8583-5906f511c379
<img width="1519" height="675" alt="image" src="https://github.com/user-attachments/assets/5b266459-12ed-42b4-80df-4a798de15a72" />

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
