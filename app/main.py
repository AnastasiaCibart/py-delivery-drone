class Cargo:
    def __init__(self, weight: int) -> None:
        self.weight = weight


class BaseRobot:
    def __init__(
            self,
            name: str,
            weight: int,
            coords: list[int, int] = [0, 0]
    ) -> None:
        self.name = name
        self.weight = weight
        self.x, self.y, *_ = coords
        self.coords = [self.x, self.y]

    # @property
    # def coords(self) -> list[int, int]:
    #     return [self.x, self.y]

    def go_forward(self, step: int = 1) -> None:
        self.y += step
        self.coords[1] = self.y

    def go_back(self, step: int = 1) -> None:
        self.y -= step
        self.coords[1] = self.y

    def go_right(self, step: int = 1) -> None:
        self.x += step
        self.coords[0] = self.x

    def go_left(self, step: int = 1) -> None:
        self.x -= step
        self.coords[0] = self.x

    def get_info(self) -> str:
        return f"Robot: {self.name}, Weight: {self.weight}"


class FlyingRobot(BaseRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        coords: list[int, int, int] = [0, 0, 0],
    ) -> None:
        x, y, self.z, *_ = coords
        super().__init__(
            name,
            weight,
            [x, y],
        )
        self.coords = [self.x, self.y, self.z]

    # @property
    # def coords(self) -> list[int, int, int]:
    #     return [self.x, self.y, self.z]

    def go_up(self, step: int = 1) -> None:
        self.z += step
        self.coords = [self.x, self.y, self.z]

    def go_down(self, step: int = 1) -> None:
        self.z -= step
        self.coords = [self.x, self.y, self.z]


class DeliveryDrone(FlyingRobot):
    def __init__(
        self,
        name: str,
        weight: int,
        coords: list[int] = [0, 0, 0],
        max_load_weight: int = 0,
        current_load: int = None,
    ) -> None:
        super().__init__(name, weight, coords)
        self.max_load_weight = max_load_weight
        self.current_load = current_load

    def hook_load(self, cargo: int) -> None:
        if self.current_load is None and cargo.weight <= self.max_load_weight:
            self.current_load = cargo

    def unhook_load(self) -> None:
        self.current_load = None
