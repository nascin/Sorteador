import flet
from flet import Page
from sorteador.views import view_sorteador

def main(page: Page):
    ''' Main function '''
    page.title = 'Sorteador'
    page.views.append(
        view_sorteador,
    )
    page.update()

flet.app(target=main, view=flet.WEB_BROWSER, port=8080)