"""teamsocial model ad

Revision ID: 028448d52e6f
Revises: 5030e7a4e889
Create Date: 2022-09-29 11:37:09.192089

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '028448d52e6f'
down_revision = '5030e7a4e889'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('team_social',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('social_name', sa.String(length=180), nullable=True),
    sa.Column('social_icon', sa.String(length=120), nullable=True),
    sa.Column('social_url', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('team_social')
    # ### end Alembic commands ###
