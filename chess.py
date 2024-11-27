from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        """
        Inicializuje šachovou figurku.
        
        :param color: Barva figurky ('white' nebo 'black').
        :param position: Aktuální pozice na šachovnici jako tuple (row, col).
        """
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self):
        """
        Vrací všechny možné pohyby figurky.
        Musí být implementováno v podtřídách.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        pass

    @staticmethod
    def is_position_on_board(position):
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_postion):
        self.__position = new_postion

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'


class Pawn(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy pěšáka.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        final_moves = []

        if self.color == "white":
            forward = (row + 1, col)
        elif self.color == "black":
            forward = (row - 1, col)
        else:
            return final_moves

        # Kontrola, zda je pozice na šachovnici
        if self.is_position_on_board(forward):
            final_moves.append(forward)

        return final_moves

    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'


class Knight(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy jezdce.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        # Filtruje tahy, které jsou mimo šachovnici
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves

    def __str__(self):
        return f'Knight({self.color}) at position {self.position}'


class Bishop(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy střelce.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        final_moves = []

        # Filtruje tahy, které jsou mimo šachovnici
        for i in range(1, 8):
            moves = [
                (row + i, col + i), (row + i, col - i),
                (row - i, col + i), (row - i, col - i)
            ]
            for move in moves:
                if self.is_position_on_board(move):
                    final_moves.append(move)

        return final_moves

    def __str__(self):
        return f'Bishop({self.color}) at position {self.position}'


class Rook(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy věže.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        final_moves = []

        # Filtruje tahy, které jsou mimo šachovnici
        for i in range(1, 8):
            moves = [
                (row + i, col), (row - i, col),
                (row, col + i), (row, col - i)
            ]
            for move in moves:
                if self.is_position_on_board(move):
                    final_moves.append(move)

        return final_moves

    def __str__(self):
        return f'Rook({self.color}) at position {self.position}'


class Queen(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy dámy (kombinace věže a střelce).
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        final_moves = []

        # Filtruje tahy, které jsou mimo šachovnici
        for i in range(1, 8):
            moves = [
                # jako střelec
                (row + i, col + i), (row + i, col - i),
                (row - i, col + i), (row - i, col - i),
                # jako věž
                (row + i, col), (row - i, col),
                (row, col + i), (row, col - i)
            ]
            for move in moves:
                if self.is_position_on_board(move):
                    final_moves.append(move)

        return final_moves

    def __str__(self):
        return f'Queen({self.color}) at position {self.position}'


class King(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy krále.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = [
            (row + 1, col), (row - 1, col),
            (row, col + 1), (row, col - 1),
            (row + 1, col + 1), (row - 1, col - 1),
            (row - 1, col + 1), (row + 1, col - 1)
        ]
        # Filtruje tahy, které jsou mimo šachovnici
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)

        return final_moves

    def __str__(self):
        return f'King({self.color}) at position {self.position}'


if __name__ == "__main__":
    pieces = [
        Pawn("white", (3, 2)),
        Pawn("black", (7, 2)),
        Pawn("white", (3, 5)),
        Knight("black", (1, 2)),
        Bishop("white", (4, 4)),
        Bishop("black", (3, 5)),
        Rook("black", (1, 1)),
        Queen("white", (3, 3)),
        King("black", (5, 5))
    ]

    for piece in pieces:
        print(piece)
        print(f"Možné pohyby s {piece}: {piece.possible_moves()}")
        
        # print(f"{"\033[0m"}Možné pohyby s {piece}:{"\033[34m"} {piece.possible_moves()}")