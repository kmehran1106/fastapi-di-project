"""create users table

Revision ID: f028066ea7cc
Revises:
Create Date: 2023-05-22 19:41:30.923885

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f028066ea7cc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(
        """
            CREATE TABLE users (
                id SERIAL PRIMARY KEY,
                name VARCHAR,
                email VARCHAR UNIQUE NOT NULL,
                is_active BOOLEAN DEFAULT TRUE,
                is_superuser BOOLEAN DEFAULT FALSE,
                hashed_password VARCHAR NOT NULL
            );
        """
    )
    op.execute("CREATE INDEX idx_users_name ON users (name);")
    op.execute("CREATE UNIQUE INDEX idx_users_email ON users (email);")


def downgrade() -> None:
    op.execute("DROP TABLE users;")
