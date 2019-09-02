"""empty message

Revision ID: 6f1ead15dcdd
Revises: 
Create Date: 2019-08-31 03:16:56.161547

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f1ead15dcdd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cart',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('is_empty', sa.BOOLEAN(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('discount', sa.Float(), nullable=False),
    sa.Column('delivery_fee', sa.Float(), nullable=False),
    sa.Column('total_price', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('description', sa.String(length=60), nullable=False),
    sa.Column('thumb_urls', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=30), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('description', sa.String(length=60), nullable=False),
    sa.Column('cat_id', sa.Integer(), nullable=True),
    sa.Column('thumb_urls', sa.String(length=80), nullable=False),
    sa.ForeignKeyConstraint(['cat_id'], ['category.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cart_id', sa.Integer(), nullable=True),
    sa.Column('Address', sa.String(length=1024), nullable=False),
    sa.Column('geo_lat', sa.Float(), nullable=False),
    sa.Column('geo_long', sa.Float(), nullable=False),
    sa.Column('phone_no', sa.String(length=20), nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.Column('placed_on', sa.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['cart_id'], ['cart.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cart_item',
    sa.Column('cart_id', sa.Integer(), nullable=False),
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cart_id'], ['cart.id'], ),
    sa.ForeignKeyConstraint(['item_id'], ['item.id'], ),
    sa.PrimaryKeyConstraint('cart_id', 'item_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cart_item')
    op.drop_table('order')
    op.drop_table('item')
    op.drop_table('category')
    op.drop_table('cart')
    # ### end Alembic commands ###