# Keylogger com envio de logs para o Telegram

Este é um script em Python que implementa um keylogger simples, capaz de gravar as teclas pressionadas pelo usuário e enviar os logs para um chat do Telegram. Antes de executar o código, é importante entender que o uso de keyloggers em sistemas ou dispositivos alheios sem o consentimento explícito do usuário é ilegal e antiético. O objetivo deste script é apenas para fins educacionais e de aprendizado. Não o utilize de forma indevida.

## Instruções

1. **Instale as bibliotecas necessárias:**

```bash
pip install pynput requests
```
2. pip install pynput requests

3. Substitua 'YOUR_TOKEN_HERE' pela sua chave de API do bot do Telegram.

4. Certifique-se de que o arquivo assets/receptor.txt contenha o ID do chat do Telegram para onde deseja enviar os logs.

5. Defina o intervalo de tempo (em minutos) para envio dos logs para o Telegram no arquivo .timer.

6. Cole o código abaixo em um arquivo chamado keylogger.py:

## Funcionamento

O script inicia um listener para monitorar as teclas pressionadas pelo usuário. Cada tecla pressionada é armazenada em um arquivo de log (assets/.log). Quando o tempo definido em set_timer é atingido, o conteúdo do arquivo de log é lido, codificado e enviado para o chat do Telegram especificado pelo ID no arquivo assets/receptor.txt. Após o envio, o arquivo de log é limpo para começar a gravar novas teclas.

O script continuará em execução indefinidamente, repetindo o processo de envio dos logs de acordo com o intervalo de tempo especificado.

## Aviso Legal

**É extremamente importante lembrar que o uso de keyloggers sem o consentimento explícito do usuário é ilegal e viola a privacidade de terceiros. Este script deve ser usado apenas para fins educacionais e de aprendizado, ou com permissão explícita do proprietário do sistema em questão. O autor não se responsabiliza por nenhum uso indevido ou ilegal deste código.**
