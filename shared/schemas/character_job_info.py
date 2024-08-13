from D2Shared.shared.schemas.base import BaseSchemaOrm
from D2Shared.shared.schemas.job import JobSchema


from pydantic import conint


from typing import Annotated


class CharacterJobInfoSchema(BaseSchemaOrm):
    character_id: str
    job_id: int
    job: JobSchema
    lvl: Annotated[int, conint(ge=1, le=200)]
    weight: float

    def __hash__(self) -> int:
        return (self.character_id, self.job_id).__hash__()
