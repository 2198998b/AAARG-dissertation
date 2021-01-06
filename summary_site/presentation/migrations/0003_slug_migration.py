from django.db import migrations, models
import django.db.models.deletion
from autoslug.fields import AutoSlugField
from summary_site.utils import unique_slug_generator

def migrate_data_forward(apps, schema_editor):
    # model_fields = {"Techniques":"name", "Topics":"title"}
    model_fields = {"Techniques":"name"}
    for name, col in model_fields.items():
        model = apps.get_model("presentation", name)
        for instance in model.objects.all():
            if not instance.slug:
                print("Generating slug for %s", instance)
                instance.slug = unique_slug_generator(instance, getattr(instance, col))
                instance.save() # Will trigger slug update

class Migration(migrations.Migration):
    dependencies = [
        ('presentation', '0002_auto_20210106_1841'),
    ]

    operations = [
        migrations.RunPython(migrate_data_forward, reverse_code=migrations.RunPython.noop)
    ]