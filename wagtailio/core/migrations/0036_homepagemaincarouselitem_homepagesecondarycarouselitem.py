# Generated by Django 2.0.6 on 2018-06-04 15:59

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ("images", "0008_upgrade_to_wagtail19"),
        ("wagtailcore", "0040_page_draft_title"),
        ("core", "0035_remove_carousels_and_secondary_carousel_introduction"),
    ]

    operations = [
        migrations.CreateModel(
            name="HomePageMainCarouselItem",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                ("title", models.CharField(max_length=255)),
                ("summary", models.CharField(max_length=511)),
                ("video", models.URLField()),
                (
                    "call_to_action_external_link",
                    models.URLField(blank=True, verbose_name="Call to action URL"),
                ),
                (
                    "call_to_action_caption",
                    models.CharField(blank=True, max_length=255),
                ),
                (
                    "call_to_action_internal_link",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailcore.Page",
                    ),
                ),
                (
                    "image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="images.WagtailIOImage",
                    ),
                ),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="main_carousel_items",
                        to="core.HomePage",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="HomePageSecondaryCarouselItem",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                ("title", models.CharField(max_length=255)),
                ("blockquote", models.TextField()),
                ("author_name", models.CharField(max_length=255)),
                ("author_job", models.CharField(max_length=255)),
                ("website", models.URLField(blank=True)),
                (
                    "author_image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="images.WagtailIOImage",
                    ),
                ),
                (
                    "desktop_image",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="images.WagtailIOImage",
                    ),
                ),
                (
                    "mobile_image",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="images.WagtailIOImage",
                    ),
                ),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="secondary_carousel_items",
                        to="core.HomePage",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
    ]
