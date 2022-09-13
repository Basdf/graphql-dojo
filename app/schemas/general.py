from typing import TYPE_CHECKING, TypeVar

from strawberry.type import StrawberryTypeVar

from app.core.db import Base

if TYPE_CHECKING:
    from app.infra.postgres.crud.base import CRUDBase

DBModelType = TypeVar("DBModelType", bound=Base)

CrudType = TypeVar("CrudType", bound="CRUDBase")

GraphQLModelType = TypeVar("GraphQLModelType", bound=StrawberryTypeVar)
CreateSchemaType = TypeVar("CreateSchemaType", bound=StrawberryTypeVar)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=StrawberryTypeVar)
SearchSchemaType = TypeVar("SearchSchemaType", bound=StrawberryTypeVar)
