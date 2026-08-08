"""add user table

Revision ID: d1dba5b05ee6
Revises: bb95a6f5f8f8
Create Date: 2026-08-08 22:07:36.498991

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd1dba5b05ee6'
down_revision: Union[str, Sequence[str], None] = 'bb95a6f5f8f8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable = False),
                    sa.Column('email', sa.String(), nullable = False),
                    sa.Column('password',sa.String(), nullable = False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),server_default = sa.text('now()'),nullable = False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    




    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
