class FilaNormal:

    codigo:int = 0
    fila = []
    clientesatendido = []
    senhaatual:str = ""

    def gerasenhaatual(self) -> None:
        self.senhaatual = f'NM{self.codigo}'

    def resetafila(self) -> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1

    def atualizafila(self) -> None:
        self.resetafila()
        self.gerasenhaatual()
        self.fila.append(self.senhaatual)

    def chamacliente(self, caixa:int) -> str:
        cliete_atual = self.fila.pop()
        self.clientesatendido.append(cliete_atual)
        return f'Cliente atual: {cliete_atual} dirija-se ao caixa: {caixa}'
