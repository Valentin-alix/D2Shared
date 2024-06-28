from pydantic import BaseModel, ConfigDict, Field

from ..schemas.region import RegionSchema


class CacheInfo(BaseModel):
    min_parsed_count_on_map: int | None = (
        None  # if objet is not specific to map set to None
    )
    max_placement: int | None = 1  # max placement per map or at all


class ObjectSearchConfig(BaseModel):
    model_config = ConfigDict(frozen=True, arbitrary_types_allowed=True)

    name: str | None = None
    grey_scale: bool = True
    threshold: float = 0.85
    lookup_region: RegionSchema | None = None
    ref: str
    cache_info: CacheInfo | None = Field(default=CacheInfo())

    @property
    def id(self) -> str:
        return self.name or self.ref

    def __str__(self) -> str:
        return self.id

    def __repr__(self) -> str:
        return self.__str__()

    def __hash__(self) -> int:
        return self.id.__hash__()
