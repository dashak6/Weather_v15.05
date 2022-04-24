# Generated by Django 4.0.4 on 2022-04-17 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meteo_app', '0005_alter_meteodata_options_alter_winddata_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meteodata',
            name='DP',
            field=models.CharField(blank=True, default='0', max_length=64, null=True, verbose_name='Точка росы, C'),
        ),
        migrations.AlterField(
            model_name='meteodata',
            name='PA',
            field=models.CharField(blank=True, default='0', max_length=64, null=True, verbose_name='Атмосферное давление, mm Hg'),
        ),
        migrations.AlterField(
            model_name='meteodata',
            name='PR',
            field=models.CharField(blank=True, default='0', max_length=64, null=True, verbose_name='Количество жидких осадков мгновенное значение, мм'),
        ),
        migrations.AlterField(
            model_name='meteodata',
            name='PR1H',
            field=models.CharField(blank=True, default='0', max_length=64, null=True, verbose_name='Количество жидких осадков сумма за 1 час, мм'),
        ),
        migrations.AlterField(
            model_name='meteodata',
            name='PR24H',
            field=models.CharField(blank=True, default='0', max_length=64, null=True, verbose_name='Количество жидких осадков сумма за сутки, мм'),
        ),
        migrations.AlterField(
            model_name='meteodata',
            name='RH',
            field=models.CharField(blank=True, default='0', max_length=64, null=True, verbose_name='Относительная влажность, %'),
        ),
        migrations.AlterField(
            model_name='meteodata',
            name='SD_1D',
            field=models.CharField(blank=True, default='0', max_length=64, null=True, verbose_name='Данные от CMP6 установленного 45 градусов относительно            поверхности земли (Вт/м²) суммарное значение за 24 часа'),
        ),
        migrations.AlterField(
            model_name='meteodata',
            name='SD_1H',
            field=models.CharField(blank=True, default='0', max_length=64, null=True, verbose_name='Данные от CMP6 установленного 45 градусов относительно            поверхности земли (Вт/м²) суммарное значение за 1 час'),
        ),
        migrations.AlterField(
            model_name='meteodata',
            name='SD_45_1D',
            field=models.CharField(blank=True, default='0', max_length=64, null=True, verbose_name='Данные от CMP6 установленного 45 градусов относительно            поверхности земли (Вт/м²) суммарное значение за 24 часа'),
        ),
        migrations.AlterField(
            model_name='meteodata',
            name='SD_45_1H',
            field=models.CharField(blank=True, default='0', max_length=64, null=True, verbose_name='Данные от CMP6 установленного 45 градусов относительно            поверхности земли (Вт/м²) суммарное значение за 1 час'),
        ),
        migrations.AlterField(
            model_name='meteodata',
            name='SR_1D',
            field=models.CharField(blank=True, default='0', max_length=64, null=True, verbose_name='Данные от CMP6 установленного параллельно             относительно поверхности земли (Вт/м²) среднее значение за 24 часа'),
        ),
        migrations.AlterField(
            model_name='meteodata',
            name='SR_1M',
            field=models.CharField(blank=True, default='0', max_length=64, null=True, verbose_name='Данные от CMP6 установленного параллельно             относительно поверхности земли (Вт/м²) среднее значение за 1 минуту'),
        ),
        migrations.AlterField(
            model_name='meteodata',
            name='SR_45_1D',
            field=models.CharField(blank=True, default='0', max_length=64, null=True, verbose_name='Данные от CMP6 установленного 45 градусов            относительно поверхности земли (Вт/м²) среднее значение за 24 часа'),
        ),
        migrations.AlterField(
            model_name='meteodata',
            name='SR_45_1M',
            field=models.CharField(blank=True, default='0', max_length=64, null=True, verbose_name='Данные от CMP6 установленного 45 градусов            относительно поверхности земли (Вт/м²) среднее значение за 1 минуту'),
        ),
        migrations.AlterField(
            model_name='meteodata',
            name='TA',
            field=models.CharField(blank=True, default='0', max_length=64, null=True, verbose_name='Среднее значение температуры за 1 минуту, C'),
        ),
        migrations.AlterField(
            model_name='meteodata',
            name='WC',
            field=models.CharField(blank=True, default='0', max_length=64, null=True, verbose_name='Охлаждение ветром , C'),
        ),
        migrations.AlterField(
            model_name='winddata',
            name='WD1AVG',
            field=models.CharField(blank=True, default='0', max_length=64, null=True, verbose_name='Направление ветра (град) за 3 сек'),
        ),
        migrations.AlterField(
            model_name='winddata',
            name='WD1AVG10',
            field=models.CharField(blank=True, default='0', max_length=64, null=True, verbose_name='Направление ветра (град) среднее значение за 10 минут'),
        ),
        migrations.AlterField(
            model_name='winddata',
            name='WD1AVG2',
            field=models.CharField(blank=True, default='0', max_length=64, null=True, verbose_name='Направление ветра (град) среднее значение за 2 минуты'),
        ),
        migrations.AlterField(
            model_name='winddata',
            name='WD1MAX10',
            field=models.CharField(blank=True, default='0', max_length=64, null=True, verbose_name='Направление ветра (град) максимальное значение за 10 минут'),
        ),
        migrations.AlterField(
            model_name='winddata',
            name='WD1MAX2',
            field=models.CharField(blank=True, default='0', max_length=64, null=True, verbose_name='Направление ветра (град) максимальное значение за 2 минуты'),
        ),
        migrations.AlterField(
            model_name='winddata',
            name='WS1AVG',
            field=models.CharField(blank=True, default='0', max_length=64, null=True, verbose_name='Cкорость ветра (м/с) за 3 сек'),
        ),
        migrations.AlterField(
            model_name='winddata',
            name='WS1AVG10',
            field=models.CharField(blank=True, default='0', max_length=64, null=True, verbose_name='Скорость ветра (м/с) среднее значение за 10 минут'),
        ),
        migrations.AlterField(
            model_name='winddata',
            name='WS1AVG2',
            field=models.CharField(blank=True, default='0', max_length=64, null=True, verbose_name='Cкорость ветра (м/с) среднее значение за 2 минуты'),
        ),
        migrations.AlterField(
            model_name='winddata',
            name='WS1MAX10',
            field=models.CharField(blank=True, default='0', max_length=64, null=True, verbose_name='Скорость ветра (м/с) максимальное значение за 2 минуты'),
        ),
        migrations.AlterField(
            model_name='winddata',
            name='WS1MAX2',
            field=models.CharField(blank=True, default='0', max_length=64, null=True, verbose_name='Cкорость ветра (м/с) максимальное значение за 2 минуты'),
        ),
        migrations.AlterField(
            model_name='winddata',
            name='WS1MIN2',
            field=models.CharField(blank=True, default='0', max_length=64, null=True, verbose_name='Cкорость ветра (м/с) минимальное значение за 2 минуты'),
        ),
    ]