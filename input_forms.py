from webdriver_manager.chrome import ChromeDriverManager
from botcity.web.browsers.chrome import default_options
from botcity.web import WebBot, By
import pastas_arquivos
import pandas as pd
import config


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

        bot.download_folder_path = config.diretorio_download

        # Seleciona o caminho default da pasta de download do arquivo
        def_options = default_options(download_folder_path=config.diretorio_download)
        bot.options = def_options

        # Abre o navegador e acessa o Tasy
        bot.browse("https://rpachallenge.com/")

        # Navegador em tela cheia
        bot.maximize_window()

    except Exception as error:
        raise ValueError(error)


def preencher_formularios(bot: WebBot,
                          first_name: str,
                          last_name: str,
                          company_name: str,
                          role_in_company: str,
                          address: str,
                          email: str,
                          phone: str):
    try:

        # Nome
        if not bot.find_element(selector="//div[label[text()='First Name']]//input",  by=By.XPATH, ensure_visible=True):
            raise Exception("Label para preenchimento do nome não encontrado na tela")

        bot.find_element(selector="//div[label[text()='First Name']]//input",  by=By.XPATH,
                         ensure_visible=True).send_keys(first_name)

        # Sobrenome
        if not bot.find_element(selector="//div[label[text()='Last Name']]//input", by=By.XPATH, ensure_visible=True):
            raise Exception("Label para preenchimento do Sobrenome não encontrado na tela")

        bot.find_element(selector="//div[label[text()='Last Name']]//input", by=By.XPATH,
                         ensure_visible=True).send_keys(last_name)

        # Nome da empresa
        if not bot.find_element(selector="//div[label[text()='Company Name']]//input", by=By.XPATH,
                                ensure_visible=True):
            raise Exception("Label para preenchimento do Nome da empresa não encontrado na tela")

        bot.find_element(selector="//div[label[text()='Company Name']]//input", by=By.XPATH,
                         ensure_visible=True).send_keys(company_name)

        # Cargo na empresa
        if not bot.find_element(selector="//div[label[text()='Role in Company']]//input", by=By.XPATH,
                                ensure_visible=True):
            raise Exception("Label para preenchimento do Cargo na empresa não encontrado na tela")

        bot.find_element(selector="//div[label[text()='Role in Company']]//input", by=By.XPATH,
                         ensure_visible=True).send_keys(role_in_company)

        # Endereço
        if not bot.find_element(selector="//div[label[text()='Address']]//input", by=By.XPATH, ensure_visible=True):
            raise Exception("Label para preenchimento do Endereço não encontrado na tela")

        bot.find_element(selector="//div[label[text()='Address']]//input", by=By.XPATH,
                         ensure_visible=True).send_keys(address)

        # Email
        if not bot.find_element(selector="//div[label[text()='Email']]//input", by=By.XPATH, ensure_visible=True):
            raise Exception("Label para preenchimento do Email não encontrado na tela")

        bot.find_element(selector="//div[label[text()='Email']]//input", by=By.XPATH,
                         ensure_visible=True).send_keys(email)

        # Telefone
        if not bot.find_element(selector="//div[label[text()='Phone Number']]//input", by=By.XPATH, ensure_visible=True):
            raise Exception("Label para preenchimento do Telefone não encontrado na tela")

        bot.find_element(selector="//div[label[text()='Phone Number']]//input", by=By.XPATH,
                         ensure_visible=True).send_keys(phone)

        # Clicar no botão Submit
        if not bot.find_element(selector="//input[@value='Submit']", by=By.XPATH, ensure_visible=True):
            raise Exception("botão Submit não encontrado na tela")

        bot.find_element(selector="//input[@value='Submit']", by=By.XPATH, ensure_visible=True).click()

    except Exception as error:
        print(error)
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
        if not bot.find_element(selector="//div[a[contains(text(),'Download Excel')]]",
                                by=By.XPATH,
                                ensure_visible=True,
                                ensure_clickable=True):

            raise Exception("botão de download do arquivo não encontrado na tela")

        bot.find_element(selector="//div[a[contains(text(),'Download Excel')]]", by=By.XPATH, ensure_visible=True,
                         ensure_clickable=True).click()

        arquivo = pastas_arquivos.aguardar_conclusao_download(bot=bot, extensao_arquivo='.xlsx')

        return arquivo

    except Exception as error:
        raise ValueError(error)


def iniciar_desafio(bot: WebBot):
    try:
        # verificar se a pagina está carregada
        if not bot.find_element("//button[text()='Start']", By.XPATH, ensure_visible=True):
            raise Exception("Botão Start não localizado")

        bot.find_element("//button[text()='Start']", By.XPATH, ensure_visible=True).click()

        # Valida se o desafio iniciou
        if not bot.find_element("//button[text()='Round 1']", By.XPATH, ensure_visible=True):
            raise Exception("Desafio não iniciado")

    except Exception as error:
        print(error)
        raise ValueError(error)
