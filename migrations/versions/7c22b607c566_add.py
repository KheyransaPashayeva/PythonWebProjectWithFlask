"""add

Revision ID: 7c22b607c566
Revises: 79e347b02fcf
Create Date: 2022-09-25 23:44:12.167880

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c22b607c566'
down_revision = '79e347b02fcf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('faqs',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('faq_question', sa.String(length=220), nullable=True),
    sa.Column('faq_answer', sa.String(length=220), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('faqs')
    # ### end Alembic commands ###
