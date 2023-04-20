"""empty message

Revision ID: 99a774ef656e
Revises: d352cf054caa
Create Date: 2023-04-19 08:28:46.674743

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99a774ef656e'
down_revision = 'd352cf054caa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.add_column(sa.Column('apellido', sa.String(length=50), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuario', schema=None) as batch_op:
        batch_op.drop_column('apellido')

    # ### end Alembic commands ###
