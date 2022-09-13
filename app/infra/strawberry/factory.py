from typing import Callable, Optional, Type

from strawberry.types import Info

from app.infra.strawberry.helper import get_only_selected_fields
from app.schemas.general import (
    CreateSchemaType,
    CrudType,
    GraphQLModelType,
    SearchSchemaType,
)


def create_factory(
    crud: Type[CrudType],
    create_schema: Type[CreateSchemaType],
    type_: Type[GraphQLModelType],
) -> Callable[[], GraphQLModelType]:
    async def create(entity: create_schema) -> type_:
        return await crud.create(entity=entity.to_pydantic().dict(exclude_none=True))

    return create


def create_all_factory(
    crud: Type[CrudType],
    create_schema: Type[CreateSchemaType],
    type_: Type[GraphQLModelType],
) -> Callable[[], list[GraphQLModelType]]:
    async def create_all(entities: list[create_schema]) -> list[type_]:
        return await crud.create_all(
            entities=[
                entity.to_pydantic().dict(exclude_none=True) for entity in entities
            ]
        )

    return create_all


def get_all_factory(
    crud: Type[CrudType],
    type_: Type[GraphQLModelType],
    search_schema: Type[SearchSchemaType],
) -> Callable[[], list[GraphQLModelType]]:
    async def get_all(
        info: Info,
        skip: int = 0,
        limit: int = 10,
        search: Optional[search_schema] = None,
    ) -> list[type_]:
        selected_fields = get_only_selected_fields(crud.model, info)
        payload = search.to_pydantic().dict(exclude_none=True) if search else {}
        return await crud.get_all(
            selected_fields=selected_fields, payload=payload, limit=limit, skip=skip
        )

    return get_all
