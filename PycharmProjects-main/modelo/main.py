from Programa import Programa

class Playlist:
    def __init__(self, nome, programa):
        self.nome = nome
        self._programa = programa

    def __getitem__(self, item):
        return self._programa[item]

    @property
    def listagem(self):
        return self._programa

    def __len__(self):
        return len(self._programa)


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} minutos - LIKES: {self._like}\n'

class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporada} temporadas - LIKES: {self._like}\n'


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
tmp = Filme('todo mundo em panico', 1999, 100)
demolidor = Serie('demolidor', 2016, 5)
atlanta = Serie('atlanta', 2020, 3)

vingadores.dar_likes()
tmp.dar_likes()
atlanta.dar_likes()
demolidor.dar_likes()
vingadores.dar_likes()


filme_serie = [vingadores, atlanta, demolidor, tmp]
playlist_fds = Playlist('fim_de_semana', filme_serie)

print(f'listagem {len(playlist_fds)}')

for programa in playlist_fds:
    print(programa)
