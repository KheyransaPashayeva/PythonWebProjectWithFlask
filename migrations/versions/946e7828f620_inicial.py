"""inicial

Revision ID: 946e7828f620
Revises: 
Create Date: 2022-08-30 14:36:58.265291

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '946e7828f620'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('about_icon',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('about_icon_title', sa.String(length=180), nullable=False),
    sa.Column('about_icon_text', sa.String(length=220), nullable=True),
    sa.Column('about_icon_img', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('about_icon_title')
    )
    op.create_table('about_us',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('about_title', sa.String(length=180), nullable=False),
    sa.Column('about_text', sa.String(length=220), nullable=True),
    sa.Column('about_video', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('about_title')
    )
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('subject', sa.String(length=120), nullable=True),
    sa.Column('message', sa.Text(length=220), nullable=True),
    sa.Column('message_date', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('nav_bar',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('navbar_name', sa.String(length=180), nullable=False),
    sa.Column('navbar_url', sa.String(length=180), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('navbar_name'),
    sa.UniqueConstraint('navbar_url')
    )
    op.create_table('services',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('service_title', sa.String(length=180), nullable=False),
    sa.Column('service_text', sa.String(length=220), nullable=True),
    sa.Column('service_img', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('service_title')
    )
    op.create_table('transport',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('transport_title', sa.String(length=180), nullable=False),
    sa.Column('transport_text', sa.String(length=220), nullable=False),
    sa.Column('transport_img', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('transport_title')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_name', sa.String(length=80), nullable=False),
    sa.Column('user_email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=120), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_email'),
    sa.UniqueConstraint('user_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('transport')
    op.drop_table('services')
    op.drop_table('nav_bar')
    op.drop_table('messages')
    op.drop_table('about_us')
    op.drop_table('about_icon')
    # ### end Alembic commands ###
