from webdriver_manager.chrome import ChromeDriverManager
from botcity.web.browsers.chrome import default_options
from botcity.web import WebBot, By
import pandas as pd


def escolher_desafio(bot: WebBot, nome_desafio):
    try:
        # verificar se a pagina está carregada
        if not bot.find_element("brand-logo", By.CLASS_NAME, ensure_visible=True):
            raise Exception("pagina do desafio não encontrado na tela")

        # TODO: Selecionar o desafio
        bot.find_element("", By.XPATH).click()

    except Exception as error:
        raise ValueError(error)


def abrir_site_rpa_challenge(bot: WebBot):

    try:
        # instala a versão do software mais recente
        bot.driver_path = ChromeDriverManager().install()

        # TODO: colocar para poder escolher a pasta onde vai baixar os arquivos.

        # Abre o navegador e acessa o Tasy
        bot.browse("https://rpachallenge.com/")

        # Navegador em tela cheia
        bot.maximize_window()

    except Exception as error:
        raise ValueError(error)


def ler_arquivo(caminho_arquivo: str) -> pd.DataFrame:

    try:
        # LER ARQUIVO EXCEL
        dados_excel = pd.read_excel(caminho_arquivo)

        return dados_excel

    except Exception as error:
        raise ValueError(error)
