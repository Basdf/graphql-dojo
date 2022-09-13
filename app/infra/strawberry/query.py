import asyncio
from typing import AsyncGenerator, Optional

import strawberry
from strawberry.fastapi import GraphQLRouter
from strawberry.schema.config import StrawberryConfig
from strawberry.subscriptions import GRAPHQL_TRANSPORT_WS_PROTOCOL, GRAPHQL_WS_PROTOCOL

from app.infra.postgres.crud import author, book, editorial, gender
from app.infra.strawberry.factory import (
    create_all_factory,
    create_factory,
    get_all_factory,
)
from app.schemas.pydantic.book import BookBase
from app.schemas.strawberry.author import (
    AuthorType,
    CreateAuthorType,
    SearchAuthorType,
    UpdateAuthorType,
)
from app.schemas.strawberry.book import (
    BookType,
    CreateBookType,
    SearchBookType,
    UpdateBookType,
)
from app.schemas.strawberry.editorial import (
    CreateEditorialType,
    EditorialType,
    SearchEditorialType,
    UpdateEditorialType,
)
from app.schemas.strawberry.gender import (
    CreateGenderType,
    GenderType,
    SearchGenderType,
    UpdateGenderType,
)


@strawberry.type
class Query:
    get_all_author: list[AuthorType] = strawberry.field(
        resolver=get_all_factory(
            crud=author.crud_author,
            search_schema=SearchAuthorType,
            type_=AuthorType,
        )
    )

    @strawberry.mutation
    async def get_all_book(
        skip: int = 0,
        limit: int = 10,
        search: Optional[SearchBookType] = None,
    ) -> list[BookType]:
        payload = search.to_pydantic() if search else None
        return await book.crud_book.get_books(limit=limit, skip=skip, payload=payload)

    # get_all_book: list[BookType] = strawberry.field(
    #     resolver=get_all_factory(
    #         crud=book.crud_book,
    #         search_schema=SearchBookType,
    #         type_=BookType,
    #     )
    # )
    get_all_editorial: list[EditorialType] = strawberry.field(
        resolver=get_all_factory(
            crud=editorial.crud_editorial,
            search_schema=SearchEditorialType,
            type_=EditorialType,
        )
    )
    get_all_gender: list[GenderType] = strawberry.field(
        resolver=get_all_factory(
            crud=gender.crud_gender,
            search_schema=SearchGenderType,
            type_=GenderType,
        )
    )


@strawberry.type
class Mutation:
    create_author: AuthorType = strawberry.field(
        resolver=create_factory(
            crud=author.crud_author,
            create_schema=CreateAuthorType,
            type_=AuthorType,
        )
    )

    @strawberry.mutation
    async def create_book(entity: CreateBookType) -> BookType:
        return await book.crud_book.create_book(entity=entity.to_pydantic())

    @strawberry.mutation
    async def update_book(payload: UpdateBookType, id: int) -> BookType:
        return await book.crud_book.update_book(payload=payload.to_pydantic(), id=id)

    @strawberry.mutation
    async def delete_book(id: int) -> None:
        return await book.crud_book.delete_book(id=id)

    create_editorial: EditorialType = strawberry.field(
        resolver=create_factory(
            crud=editorial.crud_editorial,
            create_schema=CreateEditorialType,
            type_=EditorialType,
        )
    )
    create_gender: GenderType = strawberry.field(
        resolver=create_factory(
            crud=gender.crud_gender,
            create_schema=CreateGenderType,
            type_=GenderType,
        )
    )
    create_all_author: list[AuthorType] = strawberry.field(
        resolver=create_all_factory(
            crud=author.crud_author,
            create_schema=CreateAuthorType,
            type_=AuthorType,
        )
    )

    create_all_book: list[BookType] = strawberry.field(
        resolver=create_all_factory(
            crud=book.crud_book,
            create_schema=CreateBookType,
            type_=BookType,
        )
    )

    create_all_editorial: list[EditorialType] = strawberry.field(
        resolver=create_all_factory(
            crud=editorial.crud_editorial,
            create_schema=CreateEditorialType,
            type_=EditorialType,
        )
    )
    create_all_gender: list[GenderType] = strawberry.field(
        resolver=create_all_factory(
            crud=gender.crud_gender,
            create_schema=CreateGenderType,
            type_=GenderType,
        )
    )


@strawberry.type
class Subscription:
    @strawberry.subscription
    async def count(self, target: int = 100) -> AsyncGenerator[int, None]:
        for i in range(target):
            yield i
            await asyncio.sleep(0.5)


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    subscription=Subscription,
    config=StrawberryConfig(auto_camel_case=False),
)

graphql_app = GraphQLRouter(
    schema=schema,
    subscription_protocols=[GRAPHQL_WS_PROTOCOL, GRAPHQL_TRANSPORT_WS_PROTOCOL],
)
