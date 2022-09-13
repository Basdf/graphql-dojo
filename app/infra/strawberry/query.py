import asyncio
from typing import AsyncGenerator

import strawberry
from strawberry.fastapi import GraphQLRouter
from strawberry.schema.config import StrawberryConfig
from strawberry.subscriptions import GRAPHQL_TRANSPORT_WS_PROTOCOL, GRAPHQL_WS_PROTOCOL

from app.services import (
    AuthorMutation,
    AuthorQuery,
    BookMutation,
    BookQuery,
    EditorialMutation,
    EditorialQuery,
    GenderMutation,
    GenderQuery,
)


@strawberry.type
class Query(BookQuery, AuthorQuery, EditorialQuery, GenderQuery):
    ...


@strawberry.type
class Mutation(BookMutation, AuthorMutation, EditorialMutation, GenderMutation):
    ...


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
