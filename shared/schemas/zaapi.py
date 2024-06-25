from pydantic import BaseModel, ConfigDict

from EzreD2Shared.shared.enums import CategoryZaapiEnum

from .map import MapSchema


class ZaapiSchema(BaseModel):
    model_config = ConfigDict(frozen=True)

    category: CategoryZaapiEnum
    text: str
    map: MapSchema

    def __hash__(self) -> int:
        return self.text.__hash__()
