import strawberry

from app.schemas.pydantic.gender import (
    CreateGender,
    GenderBase,
    SearchGender,
    UpdateGender,
)


@strawberry.type(name="Gender")
class GenderType:
    id: int
    name: str


@strawberry.experimental.pydantic.input(
    model=CreateGender, all_fields=True, name="CreateGender"
)
class CreateGenderType:
    ...


@strawberry.experimental.pydantic.input(
    model=SearchGender, all_fields=True, name="SearchGender"
)
class SearchGenderType:
    ...


@strawberry.experimental.pydantic.input(
    model=UpdateGender, all_fields=True, name="UpdateGender"
)
class UpdateGenderType:
    ...
