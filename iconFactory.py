from abc import ABC, abstractmethod


class AbstractIconFactory(ABC):

    @abstractmethod
    def create_container_icon(self):
        pass

    @abstractmethod
    def create_leaf_icon(self):
        pass


class PokerIconFactory(AbstractIconFactory):

    def create_container_icon(self):
        return "♦"

    def create_leaf_icon(self):
        return "♠"


class ChessIconFactory(AbstractIconFactory):

    def create_container_icon(self):
        return "♜"

    def create_leaf_icon(self):
        return "♞"
