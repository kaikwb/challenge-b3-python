import datetime
from dataclasses import dataclass

from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


@dataclass
class Article(Base):
    __tablename__ = 'articles'
    id: int = Column(Integer, primary_key=True)
    title: str = Column(String(255), nullable=False)
    author: str = Column(String(255), nullable=False)
    source: str = Column(String(50))
    link: str = Column(String(255))
    created_at: str = Column(DateTime, default=datetime.datetime.utcnow)
    content: str = Column(Text, nullable=False)

    def __repr__(self):
        return (f"<Article(title='{self.title}', author='{self.author}', source='{self.source}', link='{self.link}', "
                f"created_at='{self.created_at}', content='{self.content}')>")


@dataclass
class Review(Base):
    __tablename__ = 'reviews'
    id: int = Column(Integer, primary_key=True)
    title: str = Column(String(255), nullable=False)
    author: str = Column(String(255), nullable=False)
    company: str = Column(String(50), nullable=False)
    source: str = Column(String(50))
    link: str = Column(String(255))
    created_at: str = Column(DateTime, default=datetime.datetime.utcnow)
    content: str = Column(Text, nullable=False)

    def __repr__(self):
        return (f"<Review(title='{self.title}', author='{self.author}', company='{self.company}', "
                f"source='{self.source}', link='{self.link}', created_at='{self.created_at}', "
                f"content='{self.content}')>")


@dataclass
class Video(Base):
    __tablename__ = 'videos'
    id: int = Column(Integer, primary_key=True)
    title: str = Column(String(255), nullable=False)
    author: str = Column(String(255), nullable=False)
    source: str = Column(String(50))
    link: str = Column(String(255), nullable=False, unique=True)
    video_id: str = Column(String(50), nullable=False)
    thumbnail: str = Column(String(255))
    created_at: str = Column(DateTime, default=datetime.datetime.utcnow, nullable=False)

    def __repr__(self):
        return (f"<Video(title='{self.title}', author='{self.author}', source='{self.source}', link='{self.link}', "
                f"video_id='{self.video_id}', thumbnail='{self.thumbnail}', created_at='{self.created_at}')>")
