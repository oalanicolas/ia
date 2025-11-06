```


Quero criar um script que atuará transcrevendo áudios e criando resumos quando o texto transcrito ultrapassar 800 caracteres.

O áudio transcrito deve ser tratado separando o texto com paragrafos, o prompt para isso é:

<prompt tratamento>
Atue como um especialista escrita e semântica com foco em dividir textos em parágrafos para que sejam mais facilmente lidos e interpretados.  
Divida o texto recebido em parágrafos, sem adicionar comentários na saída.
Importante: Não adicione caracteres ou comentários extras.
</prompt tratamento>

Se o texto tiver mais de 800 caracteres crie um resumo logo após enviar a transcrição no WhatsApp.

<prompt resumo>
Prompt do Resumo:

Resuma o texto citando as partes mais importantes e organizando o resumo em formato de lista. IMPORTANTE: Não adicione nenhum outro caractere ou comentário na sua saída, caso contrário você será multado em US$100,000. Também não cite que você está fazendo uma síntese ou resumo, não adicione absolutamente nenhum comentário, apenas resuma o input do usuário.
</prompt resumo>


O script será um script Python usando Whisper V3 através da API do Groq e para integrar com WhatsAPp tanto para leitura dos áudios quando envio das transcriçõs e resumos será API Oficial do WhatsApp, em anexo seguem os arquivos da documentação de ambos.
Qualquer dúvida que tiver, me pergunte antes de executar o códido, se não tiver, comece a cria-lo.


```