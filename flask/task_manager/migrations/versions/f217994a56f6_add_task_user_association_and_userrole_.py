"""Add task_user_association and UserRole model

Revision ID: f217994a56f6
Revises: 0b9b856e3ad0
Create Date: 2024-04-08 09:37:07.491125

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f217994a56f6'
down_revision = '0b9b856e3ad0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('task_user_association',
    sa.Column('task_id', sa.String(length=36), nullable=True),
    sa.Column('user_id', sa.String(length=36), nullable=True),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], )
    )
    with op.batch_alter_table('blacklist_tokens', schema=None) as batch_op:
        batch_op.drop_index('token')

    op.drop_table('blacklist_tokens')
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('role', sa.Enum('ADMIN', 'USER', 'DEVELOPER', name='userrole'), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('role')

    op.create_table('blacklist_tokens',
    sa.Column('token', mysql.VARCHAR(length=500), nullable=False),
    sa.Column('id', mysql.VARCHAR(length=36), nullable=False),
    sa.Column('created_at', mysql.DATETIME(), nullable=True),
    sa.Column('updated_at', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_unicode_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    with op.batch_alter_table('blacklist_tokens', schema=None) as batch_op:
        batch_op.create_index('token', ['token'], unique=True)

    op.drop_table('task_user_association')
    # ### end Alembic commands ###