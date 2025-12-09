# bot/migrations/versions/001_create_users.py
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import JSONB

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
        
        # Наши поля (совместимость с JSON файлом)
        sa.Column('used_tips', JSONB(), default=list),
        sa.Column('used_triggers', JSONB(), default=list),
        sa.Column('used_distortions', JSONB(), default=list),
        sa.Column('used_facts', JSONB(), default=list),
        sa.Column('used_rage', JSONB(), default=list),
        sa.Column('used_anhedonia', JSONB(), default=list),
        sa.Column('achievements_received', JSONB(), default=list),
        
        # Поля от Грока (оставляем для совместимости)
        sa.Column('achievements', JSONB(), default=list),
        sa.Column('mood_history', JSONB(), default=list),
        
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('users')
