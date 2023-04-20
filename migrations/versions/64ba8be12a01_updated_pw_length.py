""" updated pw length

Revision ID: 64ba8be12a01
Revises: 7b6c382df04e
Create Date: 2023-04-20 09:50:55.692454

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64ba8be12a01'
down_revision = '7b6c382df04e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=6),
               type_=sa.String(length=1000),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.String(length=1000),
               type_=sa.VARCHAR(length=6),
               existing_nullable=True)

    # ### end Alembic commands ###
