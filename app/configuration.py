import os
import redis


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://collins:password@localhost:5432/eventsdb')
    ENVIRONMENT = os.getenv('APP_ENV', 'development')
    SESSION_TYPE = "redis"
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True
    SESSION_REDIS = redis.from_url("redis://127.0.0.1:6379")
    SECRET_KEY = os.getenv('SECRET_KEY', 'fe5de265219454f2c749e4e37cd22f2369ceee6765ce0f834305c3cd4bd21537')
