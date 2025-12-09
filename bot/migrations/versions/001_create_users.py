from alembic import op
import sqlalchemy as sa

revision = '001'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('users',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.Column('active', sa.Boolean(), default=False),
        sa.Column('start_date', sa.Date(), nullable=True),
        sa.Column('best_streak', sa.Integer(), default=0),
        sa.Column('hold_count_today', sa.Integer(), default=0),
        sa.Column('last_hold_date', sa.Date(), nullable=True),
        sa.Column('last_hold_time', sa.DateTime(), nullable=True),
        sa.Column('achievements', sa.JSON(), default=list),
        sa.Column('mood_history', sa.JSON(), default=list),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('users')
