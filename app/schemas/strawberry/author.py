import strawberry

from app.schemas.pydantic.author import CreateAuthor, SearchAuthor, UpdateAuthor
from app.schemas.strawberry.gender import GenderType


@strawberry.type
class AuthorType:
    id: int
    name: str
    genders: list[GenderType]


@strawberry.experimental.pydantic.input(
    model=CreateAuthor, all_fields=True, name="CreateAuthor"
)
class CreateAuthorType:
    ...


@strawberry.experimental.pydantic.input(
    model=SearchAuthor, all_fields=True, name="SearchAuthor"
)
class SearchAuthorType:
    ...


@strawberry.experimental.pydantic.input(
    model=UpdateAuthor, all_fields=True, name="UpdateAuthor"
)
class UpdateAuthorType:
    ...
