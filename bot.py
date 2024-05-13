from botcity.web.bot import WebBot

import input_forms
import input_forms as forms

import pastas_arquivos


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

        ##########################
        # PASSO 1 - abrir o site #
        ##########################

        # Criando a pasta de Downloads
        pastas_arquivos.nova_pasta(caminho_pasta=fr'Downloads', substituir_pasta=True)

        # iniciamos o site do RPA challenge
        forms.abrir_site_rpa_challenge(bot)

        # Escolhemos o desafio
        forms.escolher_desafio(bot, nome_desafio)

        ########################################
        # PASSO 2 - FAZER DOWNLOAD DA PLANILHA #
        ########################################

        path_arquivo = forms.fazer_download_forms(bot)

        tabela_forms = forms.ler_arquivo(caminho_arquivo=path_arquivo)

        # Inicia o desafio
        input_forms.iniciar_desafio(bot)

        for indice, item in tabela_forms.iterrows():

            # TODO: PREENCHER OS 10 FOMS
            first_name = item[0]
            last_name = item[1]
            company_name = item[2]
            role_in_company = item[3]
            address = item[4]
            email = item[5]
            phone = item[6]

            input_forms.preencher_formularios(bot=bot,
                                              first_name=first_name,
                                              last_name=last_name,
                                              company_name=company_name,
                                              role_in_company=role_in_company,
                                              address=address, email=email,
                                              phone=phone)
        print('pausar')

    except Exception as error:

        print(error)


    finally:
        # Fecha o navegador
        bot.stop_browser()


if __name__ == '__main__':
    main()
