from abc import ABC, abstractmethod


class ErrosAbs(ABC):

    @abstractmethod
    def erro100(self) -> None: pass

    @abstractmethod
    def erro200(self) -> None: pass

    @abstractmethod
    def erro300(self) -> None: pass

    @abstractmethod
    def erro400(self) -> None: pass


class Erros(ErrosAbs, ABC):

    def erro100(self) -> None:
        print('Erro 100, entre em contato com o adm')

    def erro200(self) -> None:
        print('Erro de conexão')

    def erro300(self) -> None:
        print('Erro desconhecido')

    def erro400(self) -> None:
        print('Erro de conexão')


if __name__ == "__main__":
    erro = Erros()
    erro.erro100()
    erro.erro200()
    erro.erro300()
    erro.erro400()
