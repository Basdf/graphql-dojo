from typing import Optional

import strawberry

from app.infra.postgres.crud.gender import crud_gender
from app.schemas.strawberry.gender import (
    CreateGenderType,
    GenderType,
    SearchGenderType,
    UpdateGenderType,
)


@strawberry.type
class GenderQuery:
    @strawberry.field
    async def get_all_gender(
        self,
        skip: int = 0,
        limit: int = 10,
        search: Optional[SearchGenderType] = None,
    ) -> list[GenderType]:
        payload = search.to_pydantic() if search else None
        return await crud_gender.get_genders(limit=limit, skip=skip, payload=payload)


@strawberry.type
class GenderMutation:
    @strawberry.mutation
    async def create_gender(self, entity: CreateGenderType) -> GenderType:
        return await crud_gender.create_gender(entity=entity.to_pydantic())

    @strawberry.mutation
    async def update_gender(self, payload: UpdateGenderType, id: int) -> GenderType:
        return await crud_gender.update_gender(payload=payload.to_pydantic(), id=id)

    @strawberry.mutation
    async def delete_gender(self, id: int) -> None:
        return await crud_gender.delete_gender(id=id)

    async def get_or_create_gender(self, name: str) -> GenderType:
        return await crud_gender.get_or_create(name=name)
