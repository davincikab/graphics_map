from modeltranslation.translator import register, TranslationOptions
from .models import Pins, PinCategory, PinSubCategory, Project

@register(PinCategory)
class PinCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(PinSubCategory)
class PinSubCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Project)
class PinSubCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(Pins)
class PinsTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle', 'description', 'category', 'subcategory')