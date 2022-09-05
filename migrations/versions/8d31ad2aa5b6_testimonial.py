"""testimonial

Revision ID: 8d31ad2aa5b6
Revises: 
Create Date: 2022-09-05 21:41:03.526648

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d31ad2aa5b6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('testimonials',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('profession', sa.String(length=80), nullable=True),
    sa.Column('info', sa.Text(), nullable=True),
    sa.Column('img', sa.String(length=80), nullable=True),
    sa.Column('order', sa.Integer(), nullable=True),
    sa.Column('isActive', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('testimonials')
    # ### end Alembic commands ###