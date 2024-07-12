from pydantic import BaseModel, ConfigDict

from D2Shared.shared.enums import CategoryZaapiEnum
from D2Shared.shared.schemas.map import CoordinatesMapSchema


class ZaapiSchema(BaseModel):
    model_config = ConfigDict(frozen=True)

    category: CategoryZaapiEnum
    text: str
    map_coordinates: CoordinatesMapSchema

    def __hash__(self) -> int:
        return self.text.__hash__()
