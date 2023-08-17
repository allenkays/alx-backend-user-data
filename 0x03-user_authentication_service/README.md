# 0x03. User authentication service

## Tasks

### 0. User model 
SQLAlchemy model named User for a database table named users (uses the mapping declaration of SQLAlchemy).
The model has the following attributes:

    - id, the integer primary key
    - email, a non-nullable string
    - hashed_password, a non-nullable string
    - session_id, a nullable string
    - reset_token, a nullable string

