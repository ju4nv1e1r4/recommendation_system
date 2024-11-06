#!/bin/bash

set -e

echo -e "Preparando os dados..."
python3 src/data_eng/prepare_data.py

echo -e "Pipeline executado com sucesso!"