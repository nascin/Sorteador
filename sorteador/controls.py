from flet import (
    UserControl, 
    TextField, 
    Column, 
    Row, 
    FloatingActionButton, 
    Ref, 
    Text, 
    icons
)
from random import randint


class Sorteador(UserControl):
    def build(self):
        self.numero_inicial = TextField(
            value='1', 
            width=100, 
            text_align='center', 
            text_size=20, 
            border_color='#ed90e1', 
            keyboard_type='number', 
            max_lines=1,
        )
        self.qtd_numeros = TextField(
            value='1', 
            width=100, 
            text_align='center', 
            text_size=20, 
            border_color='#ed90e1', 
            keyboard_type='number', 
            max_lines=1,
        )
        self.numero_final = TextField(
            value='100', 
            width=100, 
            text_align='center', 
            text_size=20, 
            border_color='#ed90e1', 
            keyboard_type='number', 
            max_lines=1,
        )
        self.sortear_text = Ref[Text]()
        self.numero_entre_text = Ref[Text]()
        self.e_text = Ref[Text]()
        self.numeros_sorteados_column = Column()
        self.numeros_sorteados_text = Text(size=20)
        self.novo_sorteio_button = FloatingActionButton(
            visible=False, 
            icon=icons.ADD, 
            text='Novo sorteio',
            on_click=self.novo_sorteio,
            bgcolor='#ed90e1',
        )
        self.conteudo_sorteio_row = Row(
            wrap=True,
            controls=[
                Text(ref=self.sortear_text, value='Sortear', size=20),
                self.qtd_numeros,
                Text(ref=self.numero_entre_text, value='número entre', size=20),
                self.numero_inicial,
                Text(ref=self.e_text, value='e', size=20),
                self.numero_final,
                FloatingActionButton(
                    text='Sortear', 
                    icon=icons.CHECK, 
                    on_click=self.resultado, 
                    bgcolor='#ed90e1',
                    height=70,
                ),
            ],
        )

        return Column(
            width=700,
            controls=[
                self.conteudo_sorteio_row,
                Row(
                    alignment='center',
                    controls=[
                        self.novo_sorteio_button,
                    ],
                ),
                Row(
                    controls=[
                        self.numeros_sorteados_text,
                    ]
                ),
                self.numeros_sorteados_column,
            ]
        )
    
    def resultado(self, e):
        ''' Sortear '''
        self.numeros_sorteados_column.controls.clear()
        self.numeros_sorteados_text.value = 'Números sorteados:'
        self.numeros_sorteados: list = []

        while self.numeros_sorteados.__len__() < int(self.qtd_numeros.value):
            numero = randint(int(self.numero_inicial.value), int(self.numero_final.value))
            if numero not in self.numeros_sorteados:
                self.numeros_sorteados.append(numero)
        
        self.numeros_sorteados_column.controls.append(
            Text(
                value=self.numeros_sorteados, 
                size=20, 
                color='#008080'
            )
        )
        self.conteudo_sorteio_row.visible = False
        self.novo_sorteio_button.visible = True
        self.update()

        return self.numeros_sorteados

    def novo_sorteio(self, e):
        ''' Novo sorteio '''
        self.conteudo_sorteio_row.visible = True
        self.novo_sorteio_button.visible = False
        self.numeros_sorteados_column.controls.clear()
        self.numeros_sorteados_text.value = ''
        self.update()