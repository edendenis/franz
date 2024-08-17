#!/usr/bin/env python
# coding: utf-8

# # Como instalar/configurar/usar o `franz` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para instalar/configurar/usar o `franz` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _This document contains the main commands and settings to install/configure/use the `franz` on `Linux Ubuntu`._

# ## Descrição [2]
# 
# ### `franz`
# 
# O `Franz` é uma aplicação de mensagens unificada que integra múltiplos serviços de comunicação em uma única interface. Ele permite a adição e o gerenciamento de várias contas de diferentes plataformas de mensagens, como WhatsApp, Facebook Messenger, Slack, Telegram e outros, facilitando a comunicação em um só lugar. Com uma interface intuitiva e organizada, o `Franz` melhora a produtividade ao centralizar conversas e notificações, permitindo uma experiência mais eficiente e simplificada na gestão de mensagens e comunicação.
# 

# ## 1. Configurar/Instalar/Usar o `franz` no `Linux Ubuntu` [1]
# 
# Para configurar/instalar/usar o `franz` no `Linux Ubuntu`, você pode usar o gerenciador de pacotes apt. Siga os passos abaixo:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update`
# 
#     2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes: `sudo apt --fix-broken install`
# 
#     2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
#     

# Para instalar o `Franz` no `Linux Ubuntu` usando o `Terminal Emulator`, você pode seguir os seguintes passos:
# 
# 1. **Baixar o `Franz`**: Primeiro, baixe o `Franz` através do `Terminal Emulator` utilizando o comando `wget`: `wget https://github.com/meetfranz/franz/releases/download/v5.9.2/franz_5.9.2_amd64.deb`
# 
# 2. **Instalar o `Franz`**: Após o _download_, instale o `Franz` usando o `dpkg`: `sudo dpkg -i franz_5.9.2_amd64.deb`
# 
# 3. **Resolver dependências (se necessário)**: Se houver dependências faltantes, você pode corrigi-las com o comando: `sudo apt-get install -f`
# 
#     Isso vai instalar as dependências necessárias e finalizar a instalação do `Franz`.
# 
# 4. **Executar o `Franz`**: Após a instalação, você pode iniciar o `Franz` diretamente pelo `Terminal Emulator` com o comando: `franz`
# 
# Ou, se preferir, pode encontrar o `Franz` no menu de aplicativos do seu sistema e executá-lo a partir de lá.

# ## 1.1 Código completo para configurar/instalar/usar
# 
# Para configurar/instalar/usar o `inkscape` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     sudo apt clean
#     sudo apt autoclean
#     sudo apt autoremove
#     sudo apt update -y
#     sudo apt autoremove
#     sudo apt autoclean
#     sudo apt list --upgradable
#     sudo apt full-upgrade -y
#     wget https://github.com/meetfranz/franz/releases/download/v5.9.2/franz_5.9.2_amd64.deb
#     sudo dpkg -i franz_5.9.2_amd64.deb
#     sudo apt-get install -f
#     franz
#     ```

# ## Referências
# 
# [1] OPENAI. ***Instalação do franz ubuntu.*** Disponível em: <https://chatgpt.com/c/e2c99d33-7704-4f5a-ab9e-f164e356e14a> (texto adaptado). ChatGPT. Acessado em: 17/08/2024 14:23.
# 
# [2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). ChatGPT. Acessado em: 17/08/2024 14:23.
# 
