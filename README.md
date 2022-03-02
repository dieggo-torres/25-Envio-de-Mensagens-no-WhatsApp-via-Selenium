# [Avançado] Envio de Mensagens no WhatsApp via Selenium
Este programa faz o envio de mensagens no WhatsApp para os contatos listado numa planilha.

## Como Usar este Código
Primeiro, você deve criar uma planilha no Excel e renomeá-la para __Enviar.xlsx__. A estrutura dessa planilha deve ser esta:

<table>
  <thead>
    <tr>
      <td>Pessoa</td>
      <td>Número</td>
      <td>Mensagem</td>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Diego</td>
      <td>557929872475</td>
      <td>Feliz aniversário</td>
    </tr>
    <tr>
      <td>Joana</td>
      <td>559226107372</td>
      <td>Feliz aniversário</td>
    </tr>
    <tr>
      <td>Sandra</td>
      <td>554123025859</td>
      <td>Feliz aniversário</td>
    </tr>
  </tbody>
</table>

Em segundo lugar, você deve aguardar até que a automação crie uma instância do Google Chrome e abra a página do WhatsApp Web. Assim que a página do app carregar um QR Code, você deverá escaneá-lo para fazer login.

Feito isso, aguarde para que a automação envie todas as mensagens para os contatos que você definiu.

## Observações
### Números de Telefone
Os números de telefone exemplificados foram gerados aleatoriamente no site com um [Gerador de Número de Telefone](https://geradornv.com.br/gerador-telefone/) para que eu pudesse explicar como usar este código. Quando criei o código, usei meus próprios contatos.

### Aviso: Não Execute este Código para Muitos Contatos
O ideal é que as automações para WhatsApp sejam feitas através de sua API. Se você excutar este código para diversos contatos, você estará correndo o risco de ter seu número bloqueado. Além disso, cuidado para não enviar mensagens com intervalos de tempo muito curtos, pois isso indica claramente que você está rodando uma automação em seu WhatsApp. Por isso, estipulei um tempo entre mensagens de 10s.


