"""Initial migration

Revision ID: 001
Revises: 
Create Date: 2024-01-01 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '001'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Create integrations table
    op.create_table('integration',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('merchant_id', sa.String(length=100), nullable=False),
        sa.Column('integration_type', sa.String(length=50), nullable=False),
        sa.Column('status', sa.String(length=20), nullable=True),
        sa.Column('request_payload', sa.Text(), nullable=True),
        sa.Column('response_data', sa.Text(), nullable=True),
        sa.Column('error_message', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    
    # Create code_snippets table
    op.create_table('code_snippet',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('language', sa.String(length=20), nullable=False),
        sa.Column('integration_type', sa.String(length=50), nullable=False),
        sa.Column('code', sa.Text(), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

def downgrade():
    op.drop_table('code_snippet')
    op.drop_table('integration') 