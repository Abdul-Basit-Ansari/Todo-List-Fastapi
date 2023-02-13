from fastapi import FastAPI, Depends, Request, Form, status , APIRouter
from starlette.responses import RedirectResponse
from deps import get_db
from sqlalchemy.orm import Session
from schemas import TodoCreate , TodoUpdate
import models

router = APIRouter()

@router.get("/")
async def get_todos(db: Session = Depends(get_db)):
    todos = db.query(models.Todo).all()
    return todos

@router.post("/todo" ,response_model=TodoCreate)
def add_todo(todo : TodoCreate , db: Session = Depends(get_db)):
    new_todo = models.Todo(title=todo.title , complete = todo.complete)
    try:
        db.add(new_todo)
        db.commit()
        db.refresh(new_todo)
        return new_todo
    except Exception as err:
        return err
@router.patch("/todo/{todo_id}" ,response_model=TodoUpdate)
def update_todo(todo_id: int,update_todo : TodoUpdate ,  db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    todo.title = update_todo.title
    todo.complete = update_todo.complete
    db.commit()
    return todo


@router.delete("/delete/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    db.delete(todo)
    db.commit()
    return f"{todo.id} Id Is Deleted"

