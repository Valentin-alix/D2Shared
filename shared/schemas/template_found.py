from pydantic import BaseModel

from shared.schemas.base import BaseSchemaOrm

from .region import RegionSchema


class InfoTemplateFoundPlacementSchema(BaseModel):
    filename: str
    region: RegionSchema


class TemplateFoundPlacementSchema(InfoTemplateFoundPlacementSchema, BaseSchemaOrm):
    id: int
    template_found_map_id: int | None = None

    def __hash__(self) -> int:
        return self.id.__hash__()
