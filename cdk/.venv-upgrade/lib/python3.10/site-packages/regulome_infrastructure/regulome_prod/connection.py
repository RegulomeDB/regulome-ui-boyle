from constructs import Construct

from typing import Any


class CodeStarConnection(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs: Any) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.arn = (
            'arn:aws:codeconnections:'
            'us-east-2:178707647236:'
            'connection/458f17ad-4142-4c3c-908b-4179ab258f11'
        )
