"""empty message

Revision ID: ebf5659bc87e
Revises: 5a9efb991e35
Create Date: 2023-12-11 13:04:02.197155

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ebf5659bc87e'
down_revision = '5a9efb991e35'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.alter_column('gender',
               existing_type=sa.VARCHAR(length=6),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.alter_column('gender',
               existing_type=sa.VARCHAR(length=6),
               nullable=False)

    # ### end Alembic commands ###
