import time
import random
import threading
from collections import deque

class Processo:
    def __init__(self, pid, tamanho):
        self.pid = pid
        self.tamanho = tamanho
        self.tempo_cpu = random.randint(5, 15)

    def __str__(self):
        return f"P{self.pid}"

class SimuladorThrashing:
    def __init__(self, tamanho_memoria=100):
        self.tamanho_memoria = tamanho_memoria
        self.memoria_disponivel = tamanho_memoria
        self.processos_memoria = []
        self.fila_swapping = deque()
        self.contador_swapping = 0
        self.executando = True
        self.proximo_pid = 1

    def calcular_memoria_usada(self):
        return sum(p.tamanho for p in self.processos_memoria)

    def adicionar_processo(self, tamanho=None):
        if tamanho is None:
            tamanho = random.randint(10, 30)

        novo_processo = Processo(self.proximo_pid, tamanho)
        self.proximo_pid += 1

        # Verifica se há espaço na memória
        if self.calcular_memoria_usada() + tamanho <= self.tamanho_memoria:
            self.processos_memoria.append(novo_processo)
            print(f"\n✓ Processo {novo_processo} adicionado à memória (tamanho: {tamanho}MB)")
        else:
            # Adiciona à fila de swapping
            self.fila_swapping.append(novo_processo)
            print(f"\n⚠ Memória cheia! Processo {novo_processo} adicionado à fila de swapping")

    def realizar_swapping(self):
        if not self.fila_swapping or not self.processos_memoria:
            return

        # Simula swap-out (remove processo da memória)
        processo_removido = self.processos_memoria.pop(0)
        self.fila_swapping.append(processo_removido)

        # Simula swap-in (adiciona processo da fila)
        if self.fila_swapping:
            processo_adicionado = self.fila_swapping.popleft()
            self.processos_memoria.append(processo_adicionado)

        self.contador_swapping += 1

    def exibir_estado(self):
        print("\n" + "="*60)
        print("ESTADO DO SISTEMA")
        print("="*60)

        # Memória principal
        print(f"Memória Principal ({self.calcular_memoria_usada()}/{self.tamanho_memoria}MB):")
        print(f"Processos: {[str(p) for p in self.processos_memoria]}")

        # Fila de swapping
        print(f"\nFila de Swapping ({len(self.fila_swapping)} processos):")
        print(f"Processos: {[str(p) for p in list(self.fila_swapping)[:5]]}{'...' if len(self.fila_swapping) > 5 else ''}")

        # Estatísticas
        print(f"\nOperações de Swapping: {self.contador_swapping}")

        # Nível de thrashing
        if len(self.fila_swapping) > 0:
            nivel_thrashing = len(self.fila_swapping) / (len(self.processos_memoria) + len(self.fila_swapping))
            if nivel_thrashing > 0.7:
                print("\n🚨 ALERTA: NÍVEL CRÍTICO DE THRASHING DETECTADO! 🚨")
            elif nivel_thrashing > 0.5:
                print("\n⚠ AVISO: Thrashing moderado detectado")
            elif nivel_thrashing > 0.3:
                print("\n📊 INFO: Swapping ativo")

    def executar_simulacao(self):
        while self.executando:
            # Realiza swapping se necessário
            if self.fila_swapping:
                self.realizar_swapping()

            # Exibe estado
            self.exibir_estado()

            # Aguarda um pouco
            time.sleep(2)

    def parar_simulacao(self):
        self.executando = False

def menu_principal():
    print("\n🖥️  SIMULADOR DE THRASHING DE SISTEMA 🖥️")
    print("="*60)
    print("Comandos:")
    print("  1 - Adicionar processo pequeno (10-20MB)")
    print("  2 - Adicionar processo médio (20-30MB)")
    print("  3 - Adicionar processo grande (25-30MB)")
    print("  4 - Adicionar múltiplos processos")
    print("  5 - Sair")
    print("="*60)

    simulador = SimuladorThrashing(tamanho_memoria=100)

    # Adiciona alguns processos iniciais
    for i in range(3):
        simulador.adicionar_processo(random.randint(20, 30))

    # Inicia thread de simulação
    thread_simulacao = threading.Thread(target=simulador.executar_simulacao)
    thread_simulacao.daemon = True
    thread_simulacao.start()

    while True:
        try:
            comando = input("\n> Digite o comando (1-5): ")

            if comando == '1':
                simulador.adicionar_processo(random.randint(10, 20))
            elif comando == '2':
                simulador.adicionar_processo(random.randint(20, 30))
            elif comando == '3':
                simulador.adicionar_processo(random.randint(25, 30))
            elif comando == '4':
                qtd = int(input("Quantos processos adicionar? "))
                for _ in range(qtd):
                    simulador.adicionar_processo()
                    time.sleep(0.5)
            elif comando == '5':
                print("\nEncerrando simulador...")
                simulador.parar_simulacao()
                break
            else:
                print("Comando inválido!")

        except KeyboardInterrupt:
            print("\n\nSimulação interrompida!")
            simulador.parar_simulacao()
            break
        except Exception as e:
            print(f"Erro: {e}")

if __name__ == "__main__":
    menu_principal()