"""empty message

Revision ID: 622f3d9f3136
Revises: 
Create Date: 2022-07-09 13:56:55.204819

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '622f3d9f3136'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('URL_map',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('original', sa.Text(), nullable=False),
    sa.Column('short', sa.String(length=16), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('short')
    )
    op.create_index(op.f('ix_URL_map_original'), 'URL_map', ['original'], unique=False)
    op.create_index(op.f('ix_URL_map_timestamp'), 'URL_map', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_URL_map_timestamp'), table_name='URL_map')
    op.drop_index(op.f('ix_URL_map_original'), table_name='URL_map')
    op.drop_table('URL_map')
    # ### end Alembic commands ###