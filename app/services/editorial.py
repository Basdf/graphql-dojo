from typing import Optional

import strawberry

from app.infra.postgres.crud.editorial import crud_editorial
from app.schemas.strawberry.editorial import (
    CreateEditorialType,
    EditorialType,
    SearchEditorialType,
    UpdateEditorialType,
)


@strawberry.type
class EditorialQuery:
    @strawberry.field
    async def get_all_editorial(
        self,
        skip: int = 0,
        limit: int = 10,
        search: Optional[SearchEditorialType] = None,
    ) -> list[EditorialType]:
        payload = search.to_pydantic() if search else None
        return await crud_editorial.get_editorials(
            limit=limit, skip=skip, payload=payload
        )


@strawberry.type
class EditorialMutation:
    @strawberry.mutation
    async def create_editorial(self, entity: CreateEditorialType) -> EditorialType:
        return await crud_editorial.create_editorial(entity=entity.to_pydantic())

    @strawberry.mutation
    async def update_editorial(
        self, payload: UpdateEditorialType, id: int
    ) -> EditorialType:
        return await crud_editorial.update_editorial(
            payload=payload.to_pydantic(), id=id
        )

    @strawberry.mutation
    async def delete_editorial(self, id: int) -> None:
        return await crud_editorial.delete_editorial(id=id)
