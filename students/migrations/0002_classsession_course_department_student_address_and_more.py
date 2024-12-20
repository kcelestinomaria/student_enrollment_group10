# Generated by Django 5.1.3 on 2024-12-20 13:59

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('location', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=20, unique=True)),
                ('course_name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('credits', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_code', models.CharField(max_length=20, unique=True)),
                ('department_name', models.CharField(max_length=200)),
                ('head_of_department', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='student',
            name='date_enrolled',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='student',
            name='phone_number',
            field=models.CharField(default=django.utils.timezone.now, max_length=15),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance_status', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent')], max_length=10)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student')),
                ('class_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.classsession')),
            ],
        ),
        migrations.AddField(
            model_name='classsession',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.course'),
        ),
        migrations.AddField(
            model_name='course',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='students.department'),
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment_date', models.DateTimeField(auto_now_add=True)),
                ('grade', models.CharField(blank=True, max_length=5, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student')),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instructor_id', models.CharField(max_length=100, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='students.department')),
            ],
        ),
        migrations.AddField(
            model_name='classsession',
            name='instructor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='students.instructor'),
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_code', models.CharField(max_length=20, unique=True)),
                ('program_name', models.CharField(max_length=200)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.department')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='students.program'),
        ),
    ]
