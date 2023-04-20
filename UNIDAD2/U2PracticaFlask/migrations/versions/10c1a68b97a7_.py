"""empty message

Revision ID: 10c1a68b97a7
Revises: 99a774ef656e
Create Date: 2023-04-19 20:29:46.842717

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10c1a68b97a7'
down_revision = '99a774ef656e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('paqueteria', schema=None) as batch_op:
        batch_op.add_column(sa.Column('direccion', sa.String(length=50), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('paqueteria', schema=None) as batch_op:
        batch_op.drop_column('direccion')

    # ### end Alembic commands ###