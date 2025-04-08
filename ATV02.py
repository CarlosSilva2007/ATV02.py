#1. Gerenciador de Tarefas Melhorado
import json
from datetime import datetime

class GerenciadorDeTarefas:
    def __init__(self, arquivo="tarefas.json"):
        self.arquivo = arquivo
        self.tarefas = self.carregar_tarefas()

    def carregar_tarefas(self):
        try:
            with open(self.arquivo, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def salvar_tarefas(self):
        with open(self.arquivo, "w") as f:
            json.dump(self.tarefas, f, indent=4)

    def adicionar_tarefa(self, descricao, prazo):
        tarefa = {
            "descricao": descricao,
            "prazo": prazo,
            "concluida": False
        }
        self.tarefas.append(tarefa)
        self.salvar_tarefas()

    def listar_tarefas(self):
        tarefas_ordenadas = sorted(self.tarefas, key=lambda x: datetime.strptime(x["prazo"], "%Y-%m-%d"))
        return tarefas_ordenadas

    def marcar_como_concluida(self, descricao):
        for tarefa in self.tarefas:
            if tarefa["descricao"] == descricao:
                tarefa["concluida"] = True
                self.salvar_tarefas()
                return True
        return False
      
gerenciador = GerenciadorDeTarefas()
gerenciador.adicionar_tarefa("Estudar Python", "2025-04-10")
gerenciador.adicionar_tarefa("Comprar leite", "2025-04-08")
gerenciador.marcar_como_concluida("Estudar Python")
tarefas = gerenciador.listar_tarefas()
for tarefa in tarefas:
    print(tarefa)



#2. Controle de Estoque Inteligente
import json

class Estoque:
    def __init__(self, arquivo="estoque.json"):
        self.arquivo = arquivo
        self.produtos = self.carregar_produtos()

    def carregar_produtos(self):
        try:
            with open(self.arquivo, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def salvar_produtos(self):
        with open(self.arquivo, "w") as f:
            json.dump(self.produtos, f, indent=4)

    def adicionar_produto(self, nome, quantidade, preco):
        produto = {
            "nome": nome,
            "quantidade": quantidade,
            "preco": preco
        }
        self.produtos.append(produto)
        self.salvar_produtos()

    def exibir_produtos(self):
        for produto in self.produtos:
            print(f"{produto['nome']} - Quantidade: {produto['quantidade']} - Preço: R${produto['preco']}")
        valor_total = sum(p["quantidade"] * p["preco"] for p in self.produtos)
        print(f"Valor total do estoque: R${valor_total:.2f}")

estoque = Estoque()
estoque.adicionar_produto("Produto A", 10, 25.50)
estoque.adicionar_produto("Produto B", 5, 12.00)
estoque.exibir_produtos()


#3. Sistema de Reservas de Eventos
class SistemaDeReservas:
    def __init__(self, num_assentos=10):
        self.num_assentos = num_assentos
        self.assentos = [False] * num_assentos 

    def visualizar_assentos(self):
        for i, reservado in enumerate(self.assentos):
            status = "Reservado" if reservado else "Disponível"
            print(f"Assento {i+1}: {status}")

    def reservar_assento(self, numero_assento):
        if 1 <= numero_assento <= self.num_assentos:
            if not self.assentos[numero_assento - 1]:
                self.assentos[numero_assento - 1] = True
                print(f"Assento {numero_assento} reservado com sucesso!")
            else:
                print(f"Assento {numero_assento} já está reservado.")
        else:
            print("Número de assento inválido.")

    def cancelar_reserva(self, numero_assento):
        if 1 <= numero_assento <= self.num_assentos:
            if self.assentos[numero_assento - 1]:
                self.assentos[numero_assento - 1] = False
                print(f"Reserva do assento {numero_assento} cancelada com sucesso!")
            else:
                print(f"Assento {numero_assento} não está reservado.")
        else:
            print("Número de assento inválido.")
          
reservas = SistemaDeReservas()
reservas.visualizar_assentos()
reservas.reservar_assento(3)
reservas.visualizar_assentos()
reservas.cancelar_reserva(3)
reservas.visualizar_assentos()



#4. Sistema Bancário com Login
import json

class SistemaBancario:
    def __init__(self, arquivo_usuarios="usuarios.json"):
        self.arquivo_usuarios = arquivo_usuarios
        self.usuarios = self.carregar_usuarios()
        self.usuario_logado = None

    def carregar_usuarios(self):
        try:
            with open(self.arquivo_usuarios, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def salvar_usuarios(self):
        with open(self.arquivo_usuarios, "w") as f:
            json.dump(self.usuarios, f, indent=4)

    def login(self, usuario, senha):
        for user in self.usuarios:
            if user["usuario"] == usuario and user["senha"] == senha:
                self.usuario_logado = user
                print(f"Bem-vindo, {usuario}!")
                return True
        print("Usuário ou senha incorretos.")
        return False

    def deposito(self, valor):
        if self.usuario_logado:
            self.usuario_logado["saldo"] += valor
            self.salvar_usuarios()
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Você precisa estar logado para realizar um depósito.")

    def saque(self, valor):
        if self.usuario_logado:
            if self.usuario_logado["saldo"] >= valor:
                self.usuario_logado["saldo"] -= valor
                self.salvar_usuarios()
                print(f"Saque de R${valor:.2f} realizado com sucesso!")
            else:
                print("Saldo insuficiente.")
        else:
            print("Você precisa estar logado para realizar um saque.")

banco = SistemaBancario()
banco.login("usuario1", "senha123")
banco.deposito(1000)
banco.saque(500)



#5. Gerenciador de Contatos
import json

class GerenciadorDeContatos:
    def __init__(self, arquivo="contatos.json"):
        self.arquivo = arquivo
        self.contatos = self.carregar_contatos()

    def carregar_contatos(self):
        try:
            with open(self.arquivo, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def salvar_contatos(self):
        with open(self.arquivo, "w") as f:
            json.dump(self.contatos, f, indent=4)

    def adicionar_contato(self, nome, telefone, email):
        contato = {
            "nome": nome,
            "telefone": telefone,
            "email": email
        }
        self.contatos.append(contato)
        self.salvar_contatos()

    def buscar_contato(self, nome):
        return [contato for contato in self.contatos if nome.lower() in contato["nome"].lower()]

contatos = GerenciadorDeContatos()
contatos.adicionar_contato("João Silva", "1234-5678", "joao@exemplo.com")
contatos.adicionar_contato("Maria Oliveira", "9876-5432", "maria@exemplo.com")
resultados = contatos.buscar_contato("João")
for contato in resultados:
    print(contato)

