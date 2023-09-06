"""add content column to post table

Revision ID: c8df2c068a8a
Revises: 98788c821ea6
Create Date: 2023-09-05 20:35:56.931687

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c8df2c068a8a'
down_revision: Union[str, None] = '98788c821ea6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
