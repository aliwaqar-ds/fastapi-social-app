"""add foreign key to post table

Revision ID: b42450d9549f
Revises: d1dba5b05ee6
Create Date: 2026-08-08 22:16:18.614073

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b42450d9549f'
down_revision: Union[str, Sequence[str], None] = 'd1dba5b05ee6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable = False))
    op.create_foreign_key("post_users_fkey",source_table='posts', referent_table='users',local_cols=['owner_id'],remote_cols=['id'],ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fkey',table_name='posts')
    op.drop_column(table_name='posts',column_name='owner_id')
    pass
