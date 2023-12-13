from fastapi import FastAPI, Depends, status, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/posts/', response_model=list[schemas.PostSchema])
async def read_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    posts = crud.get_posts(db, skip=skip, limit=limit)
    return posts

@app.post('/posts/', response_model=list[schemas.PostSchema], status_code=status.HTTP_201_CREATED)
async def create_posts(posts: schemas.PostListCreateSchema, db: Session = Depends(get_db)):
    return crud.create_posts(db, posts)

@app.put('/posts/{post_id}', response_model=schemas.PostSchema)
async def update_post(post_id: int, post: schemas.PostCreateSchema, db: Session = Depends(get_db)):
    db_post = crud.get_post(db, post_id=post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post não encontrado")
    return crud.update_post(db, post, post_id=post_id)

@app.delete('/posts/{post_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post_id: int, db: Session = Depends(get_db)):
    db_post = crud.get_post(db, post_id=post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post não encontrado")
    crud.delete_post(db, post_id=post_id)
    # return {"message": "Post deletado com sucesso!"}

@app.get('/posts/search/{name}', response_model=list[schemas.PostSchema])
async def search_posts(name: str, db: Session = Depends(get_db)):
    posts = crud.get_posts_by_name(db, name)
    return posts

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='0.0.0.0', port=8008, reload=True)
