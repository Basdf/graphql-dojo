import strawberry

from app.schemas.pydantic.book import CreateBook, SearchBook, UpdateBook
from app.schemas.strawberry.editorial import EditorialType
from app.schemas.strawberry.gender import GenderType


@strawberry.type(name="Book")
class BookType:
    id: int
    name: str
    editorial: EditorialType
    genders: list[GenderType]


@strawberry.experimental.pydantic.input(
    model=CreateBook, all_fields=True, name="CreateBook"
)
class CreateBookType:
    ...


@strawberry.experimental.pydantic.input(
    model=SearchBook, all_fields=True, name="SearchBook"
)
class SearchBookType:
    ...


@strawberry.experimental.pydantic.input(
    model=UpdateBook, all_fields=True, name="UpdateBook"
)
class UpdateBookType:
    ...
