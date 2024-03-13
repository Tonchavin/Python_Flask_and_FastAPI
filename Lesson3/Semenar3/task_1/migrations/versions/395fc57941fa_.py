"""empty message

Revision ID: 395fc57941fa
Revises: 
Create Date: 2023-12-11 09:59:14.070833

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '395fc57941fa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('faculty',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('student',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('surname', sa.String(length=100), nullable=False),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('gender', sa.Enum('male', 'female'), nullable=False),
    sa.Column('group', sa.Enum('A', 'B', 'C'), nullable=True),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('faculty_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['faculty_id'], ['faculty.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('student')
    op.drop_table('faculty')
    # ### end Alembic commands ###
