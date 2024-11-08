## Visão Geral do Pipeline

O pipeline segue as etapas do ciclo de vida de um modelo de Machine Learning: **Preparação dos Dados**, **Treinamento do Modelo**, **Implantação** e **Monitoramento**. Abaixo estão as ferramentas e as etapas implementadas em cada fase do pipeline.

![alt text](docs/mlops.png)
---

## Tecnologias Utilizadas

- **Cloud**: Google Cloud Platform (GCP)
- **Containerização**: Docker
- **CI/CD**: Github Actions
- **Gerenciamento de Ciclo de Vida do Modelo**: MLflow
- **API**: Flask para servir o modelo
- **Monitoramento**: Google Cloud Observability Monitoring
- **Linguagens**: Python, SQL e YAML
- **Banco de Dados**: Cloud SQL (GCP)
- **Implantação**: Cloud Run (GCP)

---

## Estrutura do Pipeline de MLOps

### 1. **Preparação dos Dados**

   - **Armazenamento de Dados**: Os dados brutos e transformados serão armazenados no Cloud Storage (GCP).
   - **Banco de Dados**: Utilizaremos o **Cloud SQL** para armazenar dados organizados, incluindo features de treinamento e logs de inferências.
   - **Scripts de ETL**: Scripts em **Python** e **SQL** para a transformação e engenharia de features.

### 2. **Treinamento do Modelo**

   - **Definição do Modelo**: Os modelos serão definidos em Python e treinados localmente, com pipelines automatizados no ambiente de desenvolvimento usando MLflow.
   - **Gerenciamento com MLflow**:
      - **Experimentos e Versionamento**: Utilizaremos o MLflow para rastrear experimentos e resultados, além de versionar o modelo com métricas de avaliação.
      - **Salvamento e Rastreabilidade**: Cada modelo será salvo com artefatos completos para garantir reprodutibilidade.
   - **Armazenamento de Modelos**: Modelos treinados serão salvos no MLflow e no Cloud Storage para serem usados no deploy.

### 3. **Pipeline de CI/CD com Github Actions**

   - **Configuração do Github Actions**:
      - **Etapas do Pipeline**: O Github Actions executará pipelines em cada novo commit (default: branch main), validando mudanças no código com o modelo em produção.
      - **Deploy Contínuo (cd4ml)**: O deploy contínuo garantirá que os modelos aprovados sejam implantados no ambiente de produção no Cloud Run.

### 4. **Serviço de API com Flask**

   - **Implementação**: Desenvolveremos uma API usando **Flask** para expor o modelo treinado e possibilitar previsões em tempo real.
   - **Endpoints**: O modelo será exposto em um endpoint que receberá os dados, que serão processados e executarão a inferência, para retornar em seguida os resultados.
   - **Containerização**: A API será empacotada em um container Docker para garantir a portabilidade.
   - **Deploy no Cloud Run**: O container Docker com a API Flask será implantado no Cloud Run, permitindo escalabilidade automática.

### 5. **Monitoramento e Observabilidade**

   - **Google Cloud Monitoring**:
      - **Logs e Métricas**: o Google Cloud Monitoring será estará configurado para coletar logs, métricas e dados de uso da API em tempo real.
      - **Alertas (opcional)**: Configurar alertas automáticos para detectar anomalias ou falhas de desempenho.
   - **Monitoramento de Métricas do Modelo**:
      - Usaremos o MLflow para rastrear métricas contínuas de desempenho do modelo. Essas métricas serão armazenadas e monitoradas para identificar a degradação do modelo.

---

## Notas Finais

Este pipeline de MLOps, com automação e monitoramento em tempo real, permite que o time acompanhe o desempenho dos modelos de maneira mais confiável e escalável.

Para mais detalhes sobre cada etapa, consulte a documentação de cada ferramenta.