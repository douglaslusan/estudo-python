from gatos import Gato
from superclasse import Dog
from classes import *
from hotel import Hotel


cao1 = Dog('garu', 4, 26)
cao2 = ServiceDog('gohan', 8, 100, 'Raziel')
cao3 = FrisbeeDog('pastor', 4, 85)
miau = Gato('meow', 2, 15)



print()


hot = Hotel('Dog Hotel')
hot.check_in(cao1)

hot.check_out(cao1)


