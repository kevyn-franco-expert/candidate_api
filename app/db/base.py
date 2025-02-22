from sqlalchemy.orm import registry
from sqlalchemy.ext.declarative import declarative_base

mapper_registry = registry()
Base = declarative_base()
