from abc import ABC, abstractmethod


class RaspSubProcess(ABC):

    @abstractmethod
    def initialize():
        pass

    @abstractmethod
    def run():
        pass

    @abstractmethod
    def stop():
        pass

    @abstractmethod
    def deinitialize():
        pass

    @abstractmethod
    def is_running() -> bool:
        pass
