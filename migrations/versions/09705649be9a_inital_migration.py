"""inital migration

Revision ID: 09705649be9a
Revises: 
Create Date: 2025-01-12 21:00:27.720529

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09705649be9a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('quotes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quote', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('quotes')
    # ### end Alembic commands ###
