from modeltranslation.translator import translator, TranslationOptions
from zinnia import models as zinnia_models

class ZinniaEntryTranslationOptions(TranslationOptions):
  fields = ('title', 'content', 'excerpt')

class ZinniaCategoryTranslationOptions(TranslationOptions):
  fields = ('title', 'description')

translator.register( zinnia_models.Entry, ZinniaEntryTranslationOptions )
translator.register( zinnia_models.Category, ZinniaCategoryTranslationOptions )
