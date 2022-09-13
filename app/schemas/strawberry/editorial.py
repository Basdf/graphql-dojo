import strawberry

from app.schemas.pydantic.editorial import (
    CreateEditorial,
    SearchEditorial,
    UpdateEditorial,
)


@strawberry.type(name="Editorial")
class EditorialType:
    id: int
    name: str


@strawberry.experimental.pydantic.input(
    model=CreateEditorial, all_fields=True, name="CreateEditorial"
)
class CreateEditorialType:
    ...


@strawberry.experimental.pydantic.input(
    model=SearchEditorial, all_fields=True, name="SearchEditorial"
)
class SearchEditorialType:
    ...


@strawberry.experimental.pydantic.input(
    model=UpdateEditorial, all_fields=True, name="UpdateEditorial"
)
class UpdateEditorialType:
    ...
