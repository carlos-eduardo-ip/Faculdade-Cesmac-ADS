from sqlalchemy.orm import Session
import models, schemas

def get_post(db: Session, post_id: int):
  return db.query(models.Post).filter(models.Post.id == post_id).first()

def get_posts(db: Session, skip: int = 0, limit: int = 100):
  return db.query(models.Post).offset(skip).limit(limit).all()

def create_posts(db: Session, posts: schemas.PostListCreateSchema):
  db_posts = [models.Post(**post.dict()) for post in posts.posts]
  db.add_all(db_posts)
  db.commit()
  for post in db_posts:
    db.refresh(post)
  return db_posts

def update_post(db: Session, post: schemas.PostCreateSchema, post_id: int):
  db.query(models.Post).filter(models.Post.id == post_id).update(post.dict())
  db.commit()
  return get_post(db, post_id)

def delete_post(db: Session, post_id: int):
  db.query(models.Post).filter(models.Post.id == post_id).delete()
  db.commit()
  # return {"mensagem": "Post deletado com sucesso"}

def get_posts_by_name(db: Session, name: str):
  return db.query(models.Post).filter(models.Post.NOME.like(f"%{name}%")).all()
