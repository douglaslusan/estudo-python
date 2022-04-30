class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._like = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def dar_nome(self, novo_nome):
        self._nome = novo_nome.title()

    @property
    def like(self):
        return self._like

    def dar_likes(self):
        self._like += 1

    def __str__(self):
        return f'{self._nome} - {self.ano} - LIKES: {self._like}\n'