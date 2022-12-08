"""ADD shell autograde

Revision ID: f9815c2de14e
Revises: 2b1fe6792b7a
Create Date: 2022-12-07 19:27:04.721457

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = "f9815c2de14e"
down_revision = "2b1fe6792b7a"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "assignment",
        sa.Column("shell_autograde_enabled", sa.Boolean(), nullable=True),
    )
    op.add_column(
        "assignment",
        sa.Column(
            "shell_autograde_repo",
            mysql.TEXT(collation="utf8mb4_general_ci", length=512),
            nullable=True,
        ),
    )
    op.add_column(
        "assignment",
        sa.Column(
            "shell_autograde_exercise_path",
            mysql.TEXT(collation="utf8mb4_general_ci", length=512),
            nullable=True,
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("assignment", "shell_autograde_exercise_path")
    op.drop_column("assignment", "shell_autograde_repo")
    op.drop_column("assignment", "shell_autograde_enabled")
    # ### end Alembic commands ###
