"""install

Revision ID: c1869c59e58e
Revises: 
Create Date: 2022-09-13 18:09:28.226375

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1869c59e58e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('transport', sa.Column('transport_url', sa.String(length=120), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('transport', 'transport_url')
    # ### end Alembic commands ###
