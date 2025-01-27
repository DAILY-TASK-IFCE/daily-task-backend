"""empty message

Revision ID: adfe0fb3cae5
Revises: 
Create Date: 2024-11-13 04:27:20.069363

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'adfe0fb3cae5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('difficulties',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('priorities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('statuses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('task_types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teams',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('types',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('photo', sa.String(length=255), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('daily_limit_time',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time_limit', sa.Time(), nullable=False),
    sa.Column('team_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['team_id'], ['teams.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('form_items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('team_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['team_id'], ['teams.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('team_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['team_id'], ['teams.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('invites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('team_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['team_id'], ['teams.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tasks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('status_id', sa.Integer(), nullable=False),
    sa.Column('priority_id', sa.Integer(), nullable=False),
    sa.Column('difficulty_id', sa.Integer(), nullable=False),
    sa.Column('task_type_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['difficulty_id'], ['difficulties.id'], ),
    sa.ForeignKeyConstraint(['priority_id'], ['priorities.id'], ),
    sa.ForeignKeyConstraint(['status_id'], ['statuses.id'], ),
    sa.ForeignKeyConstraint(['task_type_id'], ['task_types.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('team_users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('team_id', sa.Integer(), nullable=False),
    sa.Column('type_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['team_id'], ['teams.id'], ),
    sa.ForeignKeyConstraint(['type_id'], ['types.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dailies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('team_user_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('daily_limit_time_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['daily_limit_time_id'], ['daily_limit_time.id'], ),
    sa.ForeignKeyConstraint(['team_user_id'], ['team_users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('task_groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('task_id', sa.Integer(), nullable=False),
    sa.Column('group_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_form_items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('team_user_id', sa.Integer(), nullable=False),
    sa.Column('form_item_id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['form_item_id'], ['form_items.id'], ),
    sa.ForeignKeyConstraint(['team_user_id'], ['team_users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('team_user_id', sa.Integer(), nullable=False),
    sa.Column('group_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ),
    sa.ForeignKeyConstraint(['team_user_id'], ['team_users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_tasks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('task_id', sa.Integer(), nullable=False),
    sa.Column('team_user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], ),
    sa.ForeignKeyConstraint(['team_user_id'], ['team_users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('task_id', sa.Integer(), nullable=True),
    sa.Column('daily_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['daily_id'], ['dailies.id'], ),
    sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('items')
    op.drop_table('user_tasks')
    op.drop_table('user_groups')
    op.drop_table('user_form_items')
    op.drop_table('task_groups')
    op.drop_table('dailies')
    op.drop_table('team_users')
    op.drop_table('tasks')
    op.drop_table('invites')
    op.drop_table('groups')
    op.drop_table('form_items')
    op.drop_table('daily_limit_time')
    op.drop_table('users')
    op.drop_table('types')
    op.drop_table('teams')
    op.drop_table('task_types')
    op.drop_table('statuses')
    op.drop_table('priorities')
    op.drop_table('difficulties')
    # ### end Alembic commands ###
