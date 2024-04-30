"""modifying Enum and cascading for many-to-many relationship

Revision ID: a4efa4f431ae
Revises: e54aa231260e
Create Date: 2024-04-10 14:21:09.087269

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a4efa4f431ae'
down_revision = 'e54aa231260e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tasks', schema=None) as batch_op:
        batch_op.add_column(sa.Column('status', sa.Enum('START', 'PAUSE', 'IN_PROGRESS', 'DONE', 'CLOSE', name='taskstatus'), nullable=False))
        batch_op.drop_column('done')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tasks', schema=None) as batch_op:
        batch_op.add_column(sa.Column('done', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True))
        batch_op.drop_column('status')

    # ### end Alembic commands ###