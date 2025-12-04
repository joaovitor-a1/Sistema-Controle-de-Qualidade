class Livro:
    def __init__(self, titulo, autor, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.quantidade = quantidade

class Usuario:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def cadastrar_livro(self, livro):
        self.livros.append(livro)

    def cadastrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def emprestar(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo and livro.quantidade > 0:
                livro.quantidade -= 1
                return "Empréstimo realizado!"
        return "Livro indisponível!"

    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro cadastrado.")
            return
        print("\n--- Livros Cadastrados ---")
        for livro in self.livros:
            print(f"Título: {livro.titulo}, Autor: {livro.autor}, Quantidade: {livro.quantidade}")


# ------------------- MENU INTERATIVO -------------------

biblioteca = Biblioteca()

while True:
    print("\n=== Sistema de Biblioteca ===")
    print("1 - Cadastrar livro")
    print("2 - Cadastrar usuário")
    print("3 - Emprestar livro")
    print("4 - Listar livros")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Título do livro: ")
        autor = input("Autor do livro: ")
        quantidade = int(input("Quantidade: "))
        livro = Livro(titulo, autor, quantidade)
        biblioteca.cadastrar_livro(livro)
        print("Livro cadastrado com sucesso!")

    elif opcao == "2":
        nome = input("Nome do usuário: ")
        cpf = input("CPF do usuário: ")
        usuario = Usuario(nome, cpf)
        biblioteca.cadastrar_usuario(usuario)
        print("Usuário cadastrado com sucesso!")

    elif opcao == "3":
        titulo = input("Título do livro para empréstimo: ")
        resultado = biblioteca.emprestar(titulo)
        print(resultado)

    elif opcao == "4":
        biblioteca.listar_livros()

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida! Tente novamente.")
