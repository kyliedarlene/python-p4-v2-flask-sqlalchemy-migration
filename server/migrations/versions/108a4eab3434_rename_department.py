"""rename department

Revision ID: 108a4eab3434
Revises: fdf152b6b1e8
Create Date: 2024-02-22 19:06:24.965242

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '108a4eab3434'
down_revision = 'fdf152b6b1e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments', 'department')
    # ### end Alembic commands ###
