"""empty message

Revision ID: 9dbca1cefd35
Revises: 7fbe7589156d
Create Date: 2019-08-31 12:49:10.645725

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9dbca1cefd35'
down_revision = '7fbe7589156d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('cart', 'is_empty',
               existing_type=mysql.TINYINT(display_width=1),
               type_=sa.BOOLEAN(),
               existing_nullable=False)
    op.drop_column('cart', 'price')
    op.drop_column('cart', 'total_price')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cart', sa.Column('total_price', mysql.FLOAT(), nullable=False))
    op.add_column('cart', sa.Column('price', mysql.FLOAT(), nullable=False))
    op.alter_column('cart', 'is_empty',
               existing_type=sa.BOOLEAN(),
               type_=mysql.TINYINT(display_width=1),
               existing_nullable=False)
    # ### end Alembic commands ###
