class APICreateError(Exception):
    def __init__(self, url, entity, reason):
        self.reason = reason
        super().__init__(f"Can't get URL=[{url}], entity=[{entity}]: {reason}")


class APIGetError(Exception):
    def __init__(self, url, reason):
        self.reason = reason
        super().__init__(f"Can't get URL=[{url}]: {reason}")


class APIUpdateError(Exception):
    def __init__(self, url, entity, reason):
        self.reason = reason
        super().__init__(f"Can't update URL=[{url}], entity=[{entity}]: {reason}")


class APIDeleteError(Exception):
    def __init__(self, url, reason):
        self.reason = reason
        super().__init__(f"Can't delete URL=[{url}]: {reason}")
