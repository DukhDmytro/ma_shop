"""empty message
Revision ID: 573814232571
Revises: f5dabcc9e35f
Create Date: 2020-01-14 00:54:44.128554
"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '573814232571'
down_revision = 'f5dabcc9e35f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orders', sa.Column('status', sa.String(length=35), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orders', 'status')
    # ### end Alembic commands ###
