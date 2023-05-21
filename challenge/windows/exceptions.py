class MethodMustBeImplemented(Exception):
    def __init__(self, cls: object, method: str):
        super().__init__(f"Method [{method}] must be implemented on child classs [{cls.__name__}].")
