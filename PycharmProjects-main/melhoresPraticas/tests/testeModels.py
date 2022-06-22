import sys
sys.path.append(".")
from ..src.models import pessoa

def testeConcatenarNomeSobrenome():
	p1 = pessoa.Pessoa('douglas', 'luiz', 42, 123124154)
	assert p1.nome_completo() == 'douglas luiz'
