# dossie-auditoria-sao-martinho-2025
Dossiê de Auditoria Independente da São Martinho S.A. (P2 - Auditoria 1 UnB)

# Dossiê de Auditoria Independente: São Martinho S.A. (Exercício 2025/2026)

**Disciplina:** Auditoria 1 (CCA0024 - Turma 02 - 2026.2) — Universidade de Brasília (UnB)  
**Professor:** Lucas Oliveira Gomes Ferreira  
**Auditor Responsável / Equipe Técnica:** Lorenzo Caetano Lincoln - 202015124 
**Empresa Auditada:** São Martinho S.A. 
**Normas Aplicadas:** Estrutura Conceitual para Relatório Financeiro e NBC TA (Séries 200 a 600).

---

##  1. Apresentação e Escopo do Projeto
Este repositório consolida o trabalho prático (P2) de auditoria técnica independente aplicado sobre as demonstrações financeiras individuais e consolidadas da **São Martinho S.A.**. O trabalho combina dados extraídos de relatórios reais auditados pela KPMG (exercícios de 2025) com simulações computacionais avançadas em Python para testes substantivos em grandes massas de dados.

##  2. Resumo dos Parâmetros Quantitativos (PT 320)
* **Lucro Líquido do Período (Base):** R$ 663.326 mil. *(Realizado com evidência pública)*.
* **Materialidade Global (5% do Lucro Líquido):** R$ 33.166 mil.
* **Materialidade para Execução (Performance Materiality - 75%):** R$ 24.874 mil.
* **Limite para Acumulação de Distorções (LAD - 5% da Global):** R$ 1.658 mil.
* **Conta Focada para Testes Substantivos:** **Ativos Biológicos (Nível 3)** — Saldo de R$ 1.405.729 mil, caracterizada por elevado risco inerente e subjetividade de mensuração.

##  3. Sumário dos 29 Papéis de Trabalho (PTs)
O dossiê encontra-se dividido em dois grandes blocos normativos na pasta `/pts/`:
1. **PTs 01 a 15 (Planejamento, Riscos e Respostas):** Aborda a Estrutura Conceitual, NBC TA 200, 210, 220, 230, 240, 250, 260, 265, 300, 315, 320, 330, 402 e 450.
2. **PTs 16 a 29 (Evidências, Amostragem e Conclusão):** Cobre as NBC TA 500, 501, 505, 510, 520, 530, 540, 550, 560, 570, 580, 600, além dos Programas de Auditoria por Conta e da Conclusão Integrada.

##  4. Automação e Amostragem (Scripts Python)
Na pasta `/src/`, disponibilizamos o script `gerar_base_ativos_biologicos.py` que gera sinteticamente uma base de **500.000 linhas** conciliando exatamente com o saldo divulgado nas notas explicativas, além de injetar propositalmente anomalias controladas (áreas negativas e taxas de desconto incorretas) para testar a eficácia da amostragem estatística automatizada no script `amostragem_estatistica.py`.

---
*Dossiê elaborado em estrita conformidade com as normas profissionais de auditoria independente.*
