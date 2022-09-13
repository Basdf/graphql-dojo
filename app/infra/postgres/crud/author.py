from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.author import Author


class CRUDAuthor(CRUDBase[Author]):
    async def create_author():
        ...

    async def create_all_author():
        ...


crud_author = CRUDAuthor(model=Author)
