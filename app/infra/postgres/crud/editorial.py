from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models.editorial import Editorial


class CRUDEditorial(CRUDBase[Editorial]):
    ...


crud_editorial = CRUDEditorial(model=Editorial)
