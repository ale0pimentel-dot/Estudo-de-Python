📄 README
Gerenciador de Pagamentos

Programa desenvolvido em Python que simula um sistema de pagamento de uma loja, calculando descontos ou juros conforme a forma de pagamento escolhida pelo cliente.

📋 Descrição

O programa solicita o valor total da compra e apresenta diferentes opções de pagamento.

Cada opção possui uma regra específica:

À vista (dinheiro ou cheque): 10% de desconto.
À vista no cartão: 5% de desconto.
Em até 2x no cartão: sem juros.
3x ou mais no cartão: acréscimo de 2% por parcela.

Ao final, o programa informa o valor total a pagar e, quando necessário, o valor de cada parcela.

🚀 Funcionalidades
Cálculo automático de descontos.
Parcelamento em duas vezes sem juros.
Parcelamento com juros para três ou mais parcelas.
Aceita valores monetários com vírgula.
Validação da opção escolhida.
🛠️ Tecnologias utilizadas
Python 3
▶️ Como executar
Clone este repositório.
Execute o programa:
python Gerenciador_Pagamentos.py
Informe:
Valor da compra;
Forma de pagamento;
Quantidade de parcelas (quando necessário).
📚 Conceitos praticados
Estruturas condicionais (if, elif e else)
Operadores aritméticos
Cálculo de porcentagens
Manipulação de strings (replace)
Entrada e saída de dados
Lógica de negócios
💡 Possíveis melhorias
 Validar valores negativos.
 Permitir repetir uma operação sem reiniciar o programa.
 Exibir um resumo da compra.
 Calcular juros compostos em vez de juros simples (caso a regra do negócio exija).
👨‍💻 Autor

Desenvolvido por Alejandro Pimentel durante os estudos de Python no Curso em Vídeo.
