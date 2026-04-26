from Entity import Entity

class Player(Entity):
    def move(self) -> None:
        # Lógica de movimento
        print(f"O Jogador {self.name} moveu-se.")