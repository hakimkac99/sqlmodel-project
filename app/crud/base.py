from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from sqlmodel import Session, SQLModel, select

TableModelType = TypeVar("TableModelType", bound=SQLModel)
ReadSchemaType = TypeVar("ReadSchemaType", bound=SQLModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=SQLModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=SQLModel)


class CRUDBase(Generic[TableModelType, ReadSchemaType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[TableModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).
        """
        self.model = model

    def read_by_id(self, session: Session, id: Any) -> Optional[ReadSchemaType]:
        return session.get(self.model, id)

    def read_multi(self, session: Session, *, offset: int = 0, limit: int = 100) -> List[ReadSchemaType]:
        statement = select(self.model).offset(offset).limit(limit)
        return session.exec(statement).all()

    def create(self, session: Session, *, obj_in: CreateSchemaType) -> ReadSchemaType:
        print(obj_in)
        db_obj = self.model.from_orm(obj_in)
        session.add(db_obj)
        session.commit()
        session.refresh(db_obj)
        return db_obj

    def update(
        self, session: Session, *, db_obj: ReadSchemaType, obj_in: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ReadSchemaType:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_obj, key, value)

        session.add(db_obj)
        session.commit()
        session.refresh(db_obj)
        return db_obj

    def delete(self, session: Session, *, id: int) -> ReadSchemaType:
        db_obj = session.get(self.model, id)
        session.delete(db_obj)
        session.commit()
        return db_obj
