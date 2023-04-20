"""empty message

Revision ID: d352cf054caa
Revises: 
Create Date: 2023-04-19 07:44:30.186484

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd352cf054caa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('paqueteria',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('producto',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('precio', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usuario')
    op.drop_table('producto')
    op.drop_table('paqueteria')
    # ### end Alembic commands ###