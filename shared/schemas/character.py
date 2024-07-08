from D2Shared.shared.enums import BreedEnum, ElemEnum
from D2Shared.shared.schemas.base import BaseSchemaOrm
from D2Shared.shared.schemas.job import JobSchema


class CharacterJobInfoSchema(BaseSchemaOrm):
    character_id: str
    job_id: int
    job: JobSchema
    lvl: int
    weight: float

    def __hash__(self) -> int:
        return (self.character_id, self.job_id).__hash__()


class CharacterSchema(BaseSchemaOrm):
    id: str
    lvl: int = 1
    po_bonus: int = 0
    is_sub: bool = True
    time_spent: float = 0
    breed_id: int = BreedEnum.ENI
    elem: ElemEnum = ElemEnum.ELEMENT_WATER
    server_id: int
    # character_job_info: list[CharacterJobInfoSchema]
    # max_pods: int

    def __hash__(self) -> int:
        return self.id.__hash__()

    def __str__(self) -> str:
        return self.id
