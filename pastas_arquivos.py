
# CLASSE DEDICADA AO TRATAMENTO DE PASTAS E ARQUIVOS


import config


def aguardar_conclusao_download(bot, extensao_arquivo: str = '.pdf', timeout: int = 30000) -> str:
    """
    Função que aguarda o download do arquivo para ser concluído na pasta desejada, e retorna o path do arquivo.

    :param bot: Objeto do navegador
    :param extensao_arquivo: Extensão do arquivo que será baixado
    :param timeout: Timeout em milisegundos
    :return: Path do arquivo baixado
    """
    try:
        # Conta a quantidade de arquivos na pasta de downloads com a mesma extensão do arquivo que será baixado
        qt_arquivos_antes = bot.get_file_count(file_extension=extensao_arquivo)

        # Espera a conclusão do download por até timeout segundos
        qt_arquivos_apos = 0
        for i in range(int(timeout / 500)):
            qt_arquivos_apos = bot.get_file_count(file_extension=extensao_arquivo)
            if qt_arquivos_apos > qt_arquivos_antes:
                break
            bot.wait(500)

        if qt_arquivos_apos <= qt_arquivos_antes:
            raise Exception('Timeout ao esperar a conclusão do download.')

        # Pega o diretório completo do arquivo baixado
        dir_arquivo = bot.get_last_created_file(path=config.diretorio_download)

        return dir_arquivo  # Retorna o caminho completo do arquivo.

    except Exception as error:
        print(error)
        raise ValueError(error)
