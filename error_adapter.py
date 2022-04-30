from abc import ABC, abstractmethod


class ErrosAbs(ABC):

    @abstractmethod
    def erro_acesso(self) -> None: pass

    @abstractmethod
    def erro_dados(self) -> None: pass

    @abstractmethod
    def erro_desc(self) -> None: pass

    @abstractmethod
    def erro_conect(self) -> None: pass


class Error(ErrosAbs, ABC):

    def erro_acesso(self) -> None:
        print('Erro 100, entre em contato com o adm')

    def erro_dados(self) -> None:
        print('Erro de dados')

    def erro_desc(self) -> None:
        print('Erro desconhecido')

    def erro_conect(self) -> None:
        print('Erro de conexão')


class ErrorAdapter(Error):

    def erro100(self) -> None:
        self.erro_acesso()

    def erro200(self) -> None:
        self.erro_dados()

    def erro300(self) -> None:
        self.erro_desc()

    def erro400(self) -> None:
        self.erro_conect()


if __name__ == "__main__":
    erro = ErrorAdapter()
    erro.erro100()
    erro.erro200()
    erro.erro300()
    erro.erro400()
