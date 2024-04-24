from botcity.web.bot import WebBot
import input_forms as forms

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

        # PASSO 1 - abrir o site
        forms.abrir_site_rpa_challenge(bot)

        forms.escolher_desafio(bot, nome_desafio)

        print('pausar')

        # TODO: FAZER DOWNLOAD DA PLANILHA

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
