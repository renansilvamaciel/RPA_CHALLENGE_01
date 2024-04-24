from webdriver_manager.chrome import ChromeDriverManager
from botcity.web import WebBot, By
import pandas as pd


def escolher_desafio(bot: WebBot, nome_desafio):
    try:
        # verificar se a pagina está carregada
        if not bot.find_element("brand-logo", By.CLASS_NAME, ensure_visible=True):
            raise Exception("pagina do desafio não encontrado na tela")

        # Selecionar o desafio
        bot.find_element(f"//a[text()='{nome_desafio}']", By.XPATH).click()

    except Exception as error:
        raise ValueError(error)


def abrir_site_rpa_challenge(bot: WebBot):

    try:
        # instala a versão do software mais recente
        bot.driver_path = ChromeDriverManager().install()

        # Seleciona o camin
        bot.download_folder_path = 'Downloads'

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


def fazer_download_forms(bot: WebBot):
    """
    Função que faz download do fomulario para preencher as informações no site do RPA challenge
    :param bot: Objeto do navegador
    :return: Path do arquivo baixado
    """

    try:

        # Clicar no botão download
        if not bot.find_element(selector="//a[contains(text(),'Download Excel')]",
                                by=By.XPATH,
                                ensure_visible=True,
                                ensure_clickable=True):

            raise Exception("botão de download do arquivo não encontrado na tela")

        # Aguardar download do arquivo
        bot.wait_for_downloads()

        # retornar o caminho do arquivo

    except Exception as error:
        raise ValueError(error)
