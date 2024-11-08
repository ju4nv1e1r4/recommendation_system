### Manual de Instruções e Boas Práticas

1. Você pode criar suas próprias pastas, mas já tomei a liberdade de criar algumas que vejo que são necessárias. Repositório organizado orienta escalabilidade ao projeto.

2. Na pasta 'data' teremos uma pasta para armazerar dados coletados em 'external' e dados já processados em 'processed'.

3. 'docs' é uma pasta para seu uso livre. Geralmente uso para guardar testes e etc.

4. Na pasta 'reports' você encontra um lugar ideal para guardar seus relatórios de acurácia, assertividade, avaliações de modelos e etc.

5. Em 'src' temos duas pastas. 'notebooks' para que você desenvolva o modelo, se preferir, em um notebook e separe ele de forma organizada. Na pastas 'models' é onde você transforma seu notebook em script, antes de colocá-lo em produção.

6. Deixei um pipeline CRISP-DM no repositório, mas fique a vontade para seguir a metodologia que preferir.

7. Deixei um Dockerfile mas fique a vontade para apaga-lo se não for usar.

8. Crie seu ambiente virtual e, como boas práticas, sempre alimente o 'requirements.txt' com as versões de frameworks utilizadas no seu projeto.

9. Have fun! Se divirta enquanto trabalha, afinal, se estamos aqui, estamos fazendo o que gostamos, não é mesmo?!

### Commits Padrões

feat: Usado para novas funcionalidades, especialmente para adicionar componentes de pipeline ou modelos.

    Exemplo: feat(model): add XGBoost model for user classification
    Exemplo: feat(data-ingestion): implement data ingestion pipeline

fix: Para correções de bugs, especialmente em scripts de treinamento, preprocessamento de dados ou passos do pipeline.

    Exemplo: fix(preprocessing): handle null values in feature engineering
    Exemplo: fix(model-serving): correct response format in API

chore: Para tarefas de manutenção e ajustes que não afetam diretamente o pipeline ou o modelo, como mudanças em configurações de infraestrutura.

    Exemplo: chore: update Dockerfile to use latest Python version
    Exemplo: chore: clean up unused notebooks

docs: Para atualizações de documentação, especialmente importante em MLOps onde os pipelines e experimentos são complexos.

    Exemplo: docs: add readme for model training workflow
    Exemplo: docs: update usage instructions for CI/CD pipeline

style: Para ajustes de estilo de código que não alteram a lógica, mantendo a consistência em scripts e notebooks.

    Exemplo: style: format code using black
    Exemplo: style: apply PEP8 guidelines to feature engineering script

refactor: Para refatoração de código, como a melhoria de funções de preprocessamento ou organização de pipelines.

    Exemplo: refactor(data-pipeline): modularize feature engineering
    Exemplo: refactor(model): optimize training loop for efficiency

test: Para adicionar ou modificar testes, especialmente testes de validação do pipeline e unitários para scripts.

    Exemplo: test: add unit tests for data ingestion function
    Exemplo: test(model-serving): add integration tests for prediction API

perf: Usado para otimizações de performance, como melhorias em pipelines de dados ou aumento de eficiência em modelos.

    Exemplo: perf(data-processing): optimize data loading with Dask
    Exemplo: perf(model): reduce inference time with batch predictions

ci: Para mudanças no pipeline de CI/CD, comum em MLOps para automatizar testes e deployments de modelos.

    Exemplo: ci: add GitHub Actions workflow for model deployment
    Exemplo: ci: integrate MLflow tracking with CI pipeline

build: Para modificações na configuração de build, como ajustes no Docker ou dependências do ambiente.

    Exemplo: build: update Dockerfile for GPU support
    Exemplo: build: add dependencies in requirements.txt for data processing

infra (padrão adicional comumente usado em MLOps): Para mudanças de infraestrutura, como configurações em nuvem, permissões e recursos.

    Exemplo: infra: setup Cloud Storage bucket for raw data
    Exemplo: infra: configure IAM roles for model deployment

data: Para mudanças específicas relacionadas ao dataset, como atualizações, amostras de dados ou mudanças em dados de treinamento.

    Exemplo: data: update training dataset with recent records
    Exemplo: data: add data augmentation for improved model performance

pipeline: Para ajustes ou novas funcionalidades em pipelines de ETL, pipelines de treinamento ou pipelines de deploy.

    Exemplo: pipeline: update preprocessing steps in training pipeline
    Exemplo: pipeline: add model validation step before deployment

exp (experimento): Para marcar commits que estão relacionados a experimentos, como testes de hiperparâmetros ou novos algoritmos.

    Exemplo: exp: test new features in SVM model
    Exemplo: exp: run hyperparameter tuning for Random Forest model
    