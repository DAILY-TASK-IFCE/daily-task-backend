"""empty message

Revision ID: 938820fd6cf8
Revises: 78d7612a36ee
Create Date: 2024-09-27 14:29:32.470974

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '938820fd6cf8'
down_revision = '78d7612a36ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('daily_limit_time',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time_limit', sa.Time(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('dailies', schema=None) as batch_op:
        batch_op.add_column(sa.Column('daily_limit_time_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'daily_limit_time', ['daily_limit_time_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('dailies', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('daily_limit_time_id')

    op.drop_table('daily_limit_time')
    # ### end Alembic commands ###
