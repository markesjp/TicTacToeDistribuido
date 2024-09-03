
# Jogo da Velha Distribuído

Este projeto implementa uma versão do clássico jogo da velha (Tic Tac Toe) em Python que utiliza sockets para comunicação em rede, permitindo que dois jogadores se enfrentem de diferentes máquinas.

## Funcionamento

- Jogo da velha entre dois jogadores em diferentes máquinas.
- Comunicação em tempo real através de sockets.
- Interface gráfica intuitiva feita com Tkinter.
- Controle de turnos e validação de movimentos.
- Detecção de vitória, derrota ou empate.

## Pré-requisitos

Antes de iniciar, certifique-se de ter o Python instalado em sua máquina. Este projeto foi desenvolvido usando Python 3.8 ou superior. Você pode baixar a versão mais recente do Python [aqui](https://www.python.org/downloads/).

## Configuração e Execução

Clone o repositório para a sua máquina local usando:

```bash
git clone https://github.com/markesjp/TicTacToeDistribuido.git
cd jogo-da-velha-distribuido
```

### Servidor

1. Abra um terminal.
2. Navegue até o diretório do projeto.
3. Execute o seguinte comando para iniciar o servidor:
   ```bash
   python server.py
   ```
   O servidor agora estará aguardando conexões dos clientes.

### Clientes

Para iniciar os clientes que se conectarão ao servidor:

1. **Primeiro Cliente**:
   - Abra um novo terminal.
   - Navegue até o diretório do projeto, caso já não esteja nele.
   - Execute o seguinte comando para iniciar o primeiro cliente:
     ```bash
     python client.py
     ```
   - Este cliente se conectará ao servidor e aguardará o segundo jogador.

2. **Segundo Cliente**:
   - Abra um terceiro terminal.
   - Assim como os anteriores, navegue até o diretório do projeto.
   - Execute o seguinte comando para iniciar o segundo cliente:
     ```bash
     python client.py
     ```
   - Este cliente também se conectará ao servidor. Após a conexão dos dois clientes, o jogo começará.

### Jogando

- Os jogadores alternam turnos, cada um fazendo uma jogada por vez.
- As jogadas são feitas clicando nas células vazias da interface gráfica.
- O jogo verifica automaticamente condições de vitória, derrota ou empate após cada jogada.

## Contribuição

Contribuições para o projeto são bem-vindas! Se você tiver uma ideia ou correção, por favor:
1. Faça um Fork do repositório.
2. Crie uma Branch para suas modificações (`git checkout -b feature/YourFeature`).
3. Faça commit de suas mudanças (`git commit -am 'Add some feature'`).
4. Faça push para a Branch (`git push origin feature/YourFeature`).
5. Abra um Pull Request.

## Licença

Este projeto é distribuído sob a licença MIT, o que permite que seja utilizado de forma livre, inclusive para fins comerciais.

## Contato

- João Pedro de Oliveira Marques - [GitHub](https://github.com/markesjp)
