from pydantic import BaseModel, ConfigDict

from D2Shared.shared.enums import CategoryZaapiEnum


class ZaapiSchema(BaseModel):
    model_config = ConfigDict(frozen=True)

    category: CategoryZaapiEnum
    text: str
    map_id: int

    def __hash__(self) -> int:
        return self.text.__hash__()
