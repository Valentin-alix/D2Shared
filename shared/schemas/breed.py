from D2Shared.shared.schemas.base import BaseSchemaOrm


class BreedSchema(BaseSchemaOrm):
    id: int
    name: str
    # spell_variants: list["SpellVariantSchema"]

    def __hash__(self) -> int:
        return self.id.__hash__()
