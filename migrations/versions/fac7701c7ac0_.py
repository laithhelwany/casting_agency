"""empty message

Revision ID: fac7701c7ac0
Revises: 131e7e19060f
Create Date: 2020-05-15 19:26:57.096364

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fac7701c7ac0'
down_revision = '131e7e19060f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('actors', 'age',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('actors', 'gender',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('actors', 'gender',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('actors', 'age',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###