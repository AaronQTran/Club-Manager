# Generated by Django 4.2.16 on 2024-10-04 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("clubs", "0004_club_logo"),
    ]

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=128)),
                ("description", models.TextField(blank=True, null=True)),
                ("location", models.CharField(blank=True, max_length=255, null=True)),
                ("starts", models.DateTimeField(blank=True, null=True)),
                ("ends", models.DateTimeField(blank=True, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="EventAttendance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="RecurringEvent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=128)),
                ("description", models.TextField(blank=True, null=True)),
                ("location", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "day",
                    models.CharField(
                        choices=[
                            ("M", "Monday"),
                            ("T", "Tuesday"),
                            ("W", "Wednesday"),
                            ("R", "Thursday"),
                            ("F", "Friday"),
                            ("SA", "Saturday"),
                            ("SU", "Sunday"),
                        ],
                        max_length=2,
                    ),
                ),
                ("start_time", models.TimeField(blank=True, null=True)),
                ("end_time", models.TimeField(blank=True, null=True)),
                (
                    "start_date",
                    models.DateField(
                        help_text="Date of the first occurance of this event"
                    ),
                ),
                (
                    "end_date",
                    models.DateField(
                        blank=True,
                        help_text="Date of the last occurance of this event",
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.RemoveConstraint(
            model_name="clubmembership",
            name="Only one club owner per club.",
        ),
        migrations.AddField(
            model_name="clubmembership",
            name="points",
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddConstraint(
            model_name="clubmembership",
            constraint=models.UniqueConstraint(
                condition=models.Q(("owner", True)),
                fields=("club", "owner"),
                name="only_one_owner_per_club",
            ),
        ),
        migrations.AddField(
            model_name="eventattendance",
            name="event",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="member_attendance",
                to="clubs.event",
            ),
        ),
        migrations.AddField(
            model_name="eventattendance",
            name="member",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="event_attendance",
                to="clubs.clubmembership",
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="club",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="events",
                to="clubs.club",
            ),
        ),
        migrations.AddField(
            model_name="event",
            name="recurring_event",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="clubs.recurringevent",
            ),
        ),
        migrations.AddConstraint(
            model_name="eventattendance",
            constraint=models.UniqueConstraint(
                fields=("event", "member"),
                name="record_attendance_once_per_member_per_event",
            ),
        ),
    ]
