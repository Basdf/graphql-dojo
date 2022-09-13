from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.author_x_gender import AuthorXGender


class CRUDAuthorXGender(CRUDBase[AuthorXGender]):
    ...


crud_author_x_gender = CRUDAuthorXGender(model=AuthorXGender)
