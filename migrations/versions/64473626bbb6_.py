"""empty message

Revision ID: 64473626bbb6
Revises: a312c18c9938
Create Date: 2022-07-19 01:13:47.684191

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64473626bbb6'
down_revision = 'a312c18c9938'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', sa.VARCHAR(length=10), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
