from pydantic import BaseModel, ConfigDict

from shared.enums import CategoryZaapiPosition

from .map import MapSchema


class ZaapiSchema(BaseModel):
    model_config = ConfigDict(frozen=True)

    category: CategoryZaapiPosition
    text: str
    map: MapSchema

    def __hash__(self) -> int:
        return self.text.__hash__()
