from typing import Optional

import strawberry

from app.infra.postgres.crud.author import crud_author
from app.schemas.strawberry.author import (
    AuthorType,
    CreateAuthorType,
    SearchAuthorType,
    UpdateAuthorType,
)


@strawberry.type
class AuthorQuery:
    @strawberry.field
    async def get_all_author(
        self,
        skip: int = 0,
        limit: int = 10,
        search: Optional[SearchAuthorType] = None,
    ) -> list[AuthorType]:
        payload = search.to_pydantic() if search else None
        return await crud_author.get_authors(limit=limit, skip=skip, payload=payload)


@strawberry.type
class AuthorMutation:
    @strawberry.mutation
    async def create_author(self, entity: CreateAuthorType) -> AuthorType:
        return await crud_author.create_author(entity=entity.to_pydantic())

    @strawberry.mutation
    async def update_author(self, payload: UpdateAuthorType, id: int) -> AuthorType:
        return await crud_author.update_author(payload=payload.to_pydantic(), id=id)

    @strawberry.mutation
    async def delete_author(self, id: int) -> None:
        return await crud_author.delete_author(id=id)
