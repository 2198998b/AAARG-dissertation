from django.db import models


class Topics(models.Model):
    topic_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=1000, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    start = models.IntegerField(blank=True, null=True)
    end = models.IntegerField(blank=True, null=True)
    query = models.TextField(blank=True, null=True)
    topic_type = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'topics'


class Techniques(models.Model):
    name = models.CharField(primary_key=True, max_length=500)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'techniques'


class Instances(models.Model):
    instance = models.IntegerField(primary_key=True)
    technique = models.ForeignKey('Techniques', models.DO_NOTHING, db_column='technique', blank=True, null=True)
    temporal = models.IntegerField(blank=True, null=True)
    start_exec = models.DateTimeField(blank=True, null=True)
    end_exec = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instances'


class InstanceMeta(models.Model):
    topic = models.ForeignKey('Topics', db_column='id', models.DO_NOTHING, primary_key=True)
    instance = models.ForeignKey('Instances', models.DO_NOTHING, db_column='instance')
    summary = models.TextField(blank=True, null=True)
    streamids = models.TextField(blank=True, null=True)
    epoch_start = models.IntegerField(blank=True, null=True)
    epoch_end = models.IntegerField(blank=True, null=True)
    importance_score = models.IntegerField(blank=True, null=True)
    total_importance = models.IntegerField(blank=True, null=True)
    r1_precision = models.FloatField(blank=True, null=True)
    r1_recall = models.FloatField(blank=True, null=True)
    r1_fmeasure = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instance_meta'
        unique_together = (('topic', 'instance'),)


class Nuggets(models.Model):
    nugget_id = models.CharField(primary_key=True, max_length=200)
    topic = models.ForeignKey('Topics', db_column='id', models.DO_NOTHING)
    importance = models.IntegerField(blank=True, null=True)
    nugget_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nuggets'
        unique_together = (('nugget_id', 'topic'),)


class NuggetInstances(models.Model):
    nugget = models.ForeignKey('Nuggets', models.DO_NOTHING, blank=True, null=True)
    topic = models.ForeignKey('Nuggets', db_column='id', models.DO_NOTHING, blank=True, null=True)
    instance = models.ForeignKey(Instances, models.DO_NOTHING, db_column='instance', blank=True, null=True)
    technique = models.ForeignKey('Techniques', models.DO_NOTHING, db_column='technique', blank=True, null=True)
    is_complete_summary = models.IntegerField(blank=True, null=True)
    found = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nugget_instances'





