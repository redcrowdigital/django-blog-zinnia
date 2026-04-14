"""
Migration to transition from auto-named index_together indexes to explicitly
named indexes. Required when upgrading databases that were created with
Django < 5.1 where AlterIndexTogether was used.

For fresh installations (using the rewritten migration 0001 and 0003), the
named indexes already exist and this migration is a no-op.
"""
from django.db import migrations


def fix_indexes_forward(apps, schema_editor):
    """
    Detect whether this database was created by the old AlterIndexTogether
    migrations (with auto-generated index names) or the new AddIndex migrations
    (with explicit names). If the old auto-named indexes exist, replace them
    with the expected named indexes.
    """
    from django.db import connection

    expected_indexes = {
        'zinnia_entry_slug_pubdate_idx': ['slug', 'publication_date'],
        'zinnia_entry_stat_pubdate_idx': [
            'status', 'publication_date', 'start_publication', 'end_publication',
        ],
    }

    with connection.cursor() as cursor:
        constraints = connection.introspection.get_constraints(cursor, 'zinnia_entry')

    for target_name, target_cols in expected_indexes.items():
        if target_name in constraints:
            # Named index already exists (fresh install with rewritten migrations).
            continue

        # Find an existing index covering exactly these columns (old auto-named).
        old_name = None
        for cname, cinfo in constraints.items():
            if not cinfo.get('index') or cinfo.get('unique') or cinfo.get('primary_key'):
                continue
            if sorted(cinfo.get('columns', [])) == sorted(target_cols):
                old_name = cname
                break

        if old_name:
            # Drop the old auto-named index.
            if connection.vendor == 'mysql':
                schema_editor.execute(
                    f'DROP INDEX `{old_name}` ON `zinnia_entry`'
                )
            else:
                schema_editor.execute(f'DROP INDEX "{old_name}"')

        # Create the new explicitly named index.
        if connection.vendor == 'mysql':
            col_sql = ', '.join(f'`{col}`' for col in target_cols)
            schema_editor.execute(
                f'CREATE INDEX `{target_name}` ON `zinnia_entry` ({col_sql})'
            )
        else:
            col_sql = ', '.join(f'"{col}"' for col in target_cols)
            schema_editor.execute(
                f'CREATE INDEX "{target_name}" ON "zinnia_entry" ({col_sql})'
            )


class Migration(migrations.Migration):

    dependencies = [
        ('zinnia', '0005_category_mptt_update'),
    ]

    operations = [
        migrations.RunPython(
            fix_indexes_forward,
            migrations.RunPython.noop,
        ),
    ]
