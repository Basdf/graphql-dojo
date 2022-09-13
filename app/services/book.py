from typing import Optional

import strawberry

from app.infra.postgres.crud.book import crud_book
from app.schemas.strawberry.book import (
    BookType,
    CreateBookType,
    SearchBookType,
    UpdateBookType,
)


@strawberry.type
class BookQuery:
    @strawberry.field
    async def get_all_book(
        self,
        skip: int = 0,
        limit: int = 10,
        search: Optional[SearchBookType] = None,
    ) -> list[BookType]:
        payload = search.to_pydantic() if search else None
        return await crud_book.get_books(limit=limit, skip=skip, payload=payload)


@strawberry.type
class BookMutation:
    @strawberry.mutation
    async def create_book(self, entity: CreateBookType) -> BookType:
        return await crud_book.create_book(entity=entity.to_pydantic())

    @strawberry.mutation
    async def update_book(self, payload: UpdateBookType, id: int) -> BookType:
        return await crud_book.update_book(payload=payload.to_pydantic(), id=id)

    @strawberry.mutation
    async def delete_book(self, id: int) -> None:
        return await crud_book.delete_book(id=id)
