from datetime import datetime, timedelta
from database import Base
from sqlalchemy.orm import Mapped, mapped_column

class BaseModel(Base):
    __abstract__ = True

    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow())
    updated_at: Mapped[datetime] = mapped_column(onupdate=datetime.utcnow())

    @property
    def get_created_at(self):
        return self.created_at + timedelta(hours=5)
    
    @property
    def get_updated_at(self):
        return self.updated_at + timedelta(hours=5)
    
