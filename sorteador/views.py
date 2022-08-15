from flet import View
from sorteador.controls import Sorteador

sorteador = Sorteador()
view_sorteador = View(
    route='/',
    scroll='auto',
    controls=[
        sorteador,
    ],
    horizontal_alignment='center',
)
