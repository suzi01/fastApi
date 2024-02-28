"""add content column to posts table

Revision ID: 6f62e679d406
Revises: a88fd6433b53
Create Date: 2024-02-27 23:10:26.871023

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6f62e679d406'
down_revision: Union[str, None] = 'a88fd6433b53'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
