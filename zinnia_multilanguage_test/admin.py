# -*- coding: utf-8 -*-
from django.contrib import admin
from zinnia import models as zinnia_models
from zinnia import admin as zinnia_admin
from modeltranslation.admin import TranslationAdmin

class ZinniaEntryTranslatedAdmin(
  zinnia_admin.EntryAdmin,
  TranslationAdmin
):

  list_display = ('title',)

  def formfield_for_dbfield(self, db_field, **kwargs):
    field = super(
      ZinniaEntryTranslatedAdmin, self
    ).formfield_for_dbfield(
      db_field, **kwargs
    )

    self.patch_translation_field( db_field, field, **kwargs )

    return field


class ZinniaCategoryTranslatedAdmin(
  zinnia_admin.CategoryAdmin,
  TranslationAdmin
):

  list_display = ('title',)

  def formfield_for_dbfield(self, db_field, **kwargs):
    field = super(
      ZinniaCategoryTranslatedAdmin, self
    ).formfield_for_dbfield(
        db_field, **kwargs
      )

    self.patch_translation_field( db_field, field, **kwargs )

    return field

admin.site.unregister( zinnia_models.Entry )
admin.site.unregister( zinnia_models.Category )
admin.site.register( zinnia_models.Entry, ZinniaEntryTranslatedAdmin )
admin.site.register( zinnia_models.Category, ZinniaCategoryTranslatedAdmin )
