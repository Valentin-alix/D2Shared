from pydantic import BaseModel, ConfigDict


class RegionSchema(BaseModel):
    model_config = ConfigDict(frozen=True, from_attributes=True)

    left: int
    top: int
    right: int
    bot: int

    def is_crossing_region(self, other: "RegionSchema") -> bool:
        if self.right < other.left or other.right < self.left:
            return False
        if self.bot < other.top or other.bot < self.top:
            return False
        return True
