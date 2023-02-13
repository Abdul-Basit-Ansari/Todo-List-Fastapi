from pydantic import BaseModel , constr

class TodoBase(BaseModel):
    title: constr(strip_whitespace=True)
    complete: bool = False
    class Config:
        orm_mode = True

class TodoCreate(TodoBase):
    pass

class TodoUpdate(TodoBase):
    pass