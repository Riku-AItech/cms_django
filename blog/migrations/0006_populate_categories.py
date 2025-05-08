from django.db import migrations


def create_categories(apps, schema_editor):
    Category = apps.get_model('blog', 'Category')
    categories = [
        "🌟 お知らせ",
        "🛠 技術・Tips",
        "📚 ナレッジ共有",
        "💬 雑談・コラム",
        "📅 イベント・予定",
        "🔐 社内ルール",
        "✏️ チュートリアル",
        "🧪 実験・検証ログ",
        "その他",
    ]
    for name in categories:
        Category.objects.get_or_create(name=name)


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_category_tag_alter_post_content_post_category_and_more'),
    ]

    operations = [
        migrations.RunPython(create_categories),
    ] 