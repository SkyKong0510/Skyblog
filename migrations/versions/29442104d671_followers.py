"""followers

Revision ID: 29442104d671
Revises: 3f72dcdc5616
Create Date: 2019-08-30 10:26:49.383364

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29442104d671'
down_revision = '3f72dcdc5616'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
