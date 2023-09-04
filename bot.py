from input_forms import *


# DOCUMENTAÇÃO:
    # ABRIR O SITE  - FUNC
    # CLICAR EM START
    # AGUARDAR O BOTÃO ROUND 1
    # loop dentro do dataset para preencher os formulários:
    # PREENCHER O FORMULARIO DENTRO DO SITE
    # CLICAR SUBMIT
    # AO FINAL DE 10 CADASTROS FINALIZAR O ROBO


def main():

    # set variaveis
    bot = WebBot()
    nome_desafio = "Input Forms"

    try:

        # LER ARQUIVO EXCEL
        tabela = ler_arquivo("caminho do arquivo")

        # PASSO 1 - abrir o site
        abrir_site_rpa_challenge(bot)

        # TODO: ESCOLHER O DESEAFIO:
        escolher_desafio(bot, nome_desafio)

        # TODO: CLICAR EM START
        # TODO: AGUARDAR O BOTÃO ROUND 1

        # TODO: PREENCHER OS 10 FOMS

    except Exception as error:

        print(error)


    finally:
        # Fecha o navegador
        bot.stop_browser()


if __name__ == '__main__':
    main()
