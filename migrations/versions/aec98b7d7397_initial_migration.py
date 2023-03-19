"""Initial migration.

Revision ID: aec98b7d7397
Revises: 9f92bab260e5
Create Date: 2023-03-18 21:49:57.346849

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aec98b7d7397'
down_revision = '9f92bab260e5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=60),
               type_=sa.String(length=600),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.String(length=600),
               type_=sa.VARCHAR(length=60),
               existing_nullable=True)

    # ### end Alembic commands ###
