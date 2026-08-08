"""add content column to posts table

Revision ID: bb95a6f5f8f8
Revises: 12d198e0931e
Create Date: 2026-08-08 20:15:55.395143

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bb95a6f5f8f8'
down_revision: Union[str, Sequence[str], None] = 'a8cb2a9ff343'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
