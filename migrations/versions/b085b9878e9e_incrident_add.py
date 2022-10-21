"""incrident add

Revision ID: b085b9878e9e
Revises: 7e37729b2215
Create Date: 2022-10-12 19:41:58.460634

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b085b9878e9e'
down_revision = '7e37729b2215'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pricing_incridents',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('pricing_incrident_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pricing_incrident_id'], ['pricing.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_column('pricing', 'incridents')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pricing', sa.Column('incridents', sa.TEXT(), nullable=True))
    op.drop_table('pricing_incridents')
    # ### end Alembic commands ###
