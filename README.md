# 🖥️ Simulador de Thrashing de Sistema

## 📋 Descrição

Este é um simulador educacional desenvolvido em Python que demonstra o fenômeno de **Thrashing** em sistemas operacionais. O thrashing ocorre quando o sistema passa mais tempo realizando operações de swapping (troca de processos entre memória RAM e disco) do que executando os processos efetivamente.

## 🎯 Objetivo

Permitir que estudantes e professores visualizem em tempo real como a sobrecarga de memória leva ao thrashing, demonstrando:
- Gerenciamento de memória limitada
- Swapping contínuo de processos
- Degradação de performance do sistema
- Alertas de thrashing crítico

## 📚 Conceitos Demonstrados

- **Memória Principal (RAM)**: Limitada a 100MB no simulador
- **Swapping**: Troca de processos entre memória e disco
- **Fila de Swapping**: Processos aguardando para entrar na memória
- **Thrashing**: Estado onde o sistema gasta mais tempo trocando processos do que executando

## 🛠️ Requisitos

- Python 3.6 ou superior
- Bibliotecas padrão do Python (threading, time, random, collections)

## 🚀 Como Executar

1. Salve o código em um arquivo chamado `simulador_thrashing.py`
2. Abra o terminal na pasta do arquivo
3. Execute o comando:
```bash
python simulador_thrashing.py
```

## 📖 Manual de Uso

### Comandos Disponíveis

1. **Adicionar processo pequeno (10-20MB)** - Digite `1`
2. **Adicionar processo médio (20-30MB)** - Digite `2`
3. **Adicionar processo grande (25-30MB)** - Digite `3`
4. **Adicionar múltiplos processos** - Digite `4`
5. **Sair do simulador** - Digite `5`

### Interface do Sistema

O simulador exibe em tempo real:
```
======================================================
ESTADO DO SISTEMA
======================================================
Memória Principal (85/100MB):
Processos: ['P1', 'P2', 'P3']

Fila de Swapping (2 processos):
Processos: ['P4', 'P5']

Operações de Swapping: 15
```

### Indicadores Visuais

- ✅ **Processo adicionado com sucesso** - Havia espaço na memória
- ⚠️ **Memória cheia** - Processo foi para fila de swapping
- 📊 **Swapping ativo** - Sistema realizando trocas normais
- ⚠️ **Thrashing moderado** - Performance começando a degradar
- 🚨 **NÍVEL CRÍTICO DE THRASHING** - Sistema severamente impactado

## 🧪 Roteiro de Teste Recomendado

### Teste 1: Operação Normal
1. Inicie o programa (3 processos iniciais)
2. Adicione 1 processo pequeno (comando `1`)
3. Observe que entra direto na memória

### Teste 2: Início do Swapping
1. Continue do teste anterior
2. Adicione 1 processo grande (comando `3`)
3. Observe o início do swapping

### Teste 3: Thrashing Moderado
1. Use o comando `4` para adicionar múltiplos processos
2. Digite `5` quando perguntado a quantidade
3. Observe o alerta de thrashing moderado
4. Note como o contador de swapping aumenta rapidamente

### Teste 4: Thrashing Severo
1. Use o comando `4` para adicionar múltiplos processos
2. Digite `10` quando perguntado a quantidade
3. Observe o alerta de thrashing crítico
4. Note como o contador de swapping aumenta rapidamente

## 📊 Comportamento Esperado

### Estado Inicial
```
Memória: [P1, P2, P3] - ~85MB usados
Fila: Vazia
```

### Após Adicionar P4
```
Memória: [P2, P3, P4] - Swapping iniciado
Fila: [P1]
Sistema começa a trocar processos
```

### Após Adicionar Vários Processos
```
Memória: [P7, P8, P9] - Thrashing severo
Fila: [P1, P2, P3, P4, P5, P6, ...]
🚨 ALERTA: NÍVEL CRÍTICO DE THRASHING DETECTADO!
```

## 🔍 Como Funciona o Código

### Estrutura Principal

1. **Classe Processo**
    - Armazena PID e tamanho
    - Simula tempo de CPU necessário

2. **Classe SimuladorThrashing**
    - Gerencia memória principal (lista)
    - Mantém fila de swapping (deque)
    - Executa swapping automático
    - Calcula níveis de thrashing

3. **Thread de Simulação**
    - Executa em background
    - Atualiza estado a cada 2 segundos
    - Realiza swapping quando necessário

### Algoritmo de Swapping

```python
1. Se fila_swapping não está vazia:
   - Remove primeiro processo da memória (FIFO)
   - Adiciona ao final da fila
   - Pega primeiro da fila e coloca na memória
   - Incrementa contador
```

## 📈 Métricas de Performance

O simulador monitora:
- **Taxa de ocupação da memória**: (MB usados / MB total)
- **Nível de thrashing**: (processos na fila / total de processos)
- **Contador de swapping**: Total de operações realizadas

### Níveis de Alerta

- **Normal**: < 30% dos processos em swapping
- **Moderado**: 30-50% dos processos em swapping
- **Severo**: 50-70% dos processos em swapping
- **Crítico**: > 70% dos processos em swapping

## ⚠️ Limitações do Simulador

Este é um modelo simplificado para fins educacionais:
- Usa algoritmo FIFO simples (sistemas reais usam algoritmos mais complexos)
- Não simula prioridades de processos
- Não considera localidade de referência
- Tamanhos de processo fixos (real seria páginas de memória)

## 🔧 Possíveis Extensões

- Implementar diferentes algoritmos de substituição (LRU, Clock)
- Adicionar prioridades aos processos
- Simular diferentes tamanhos de memória
- Incluir estatísticas detalhadas
- Criar interface gráfica

Desenvolvido para a disciplina de Sistemas Operacionais - Engenharia de Software

