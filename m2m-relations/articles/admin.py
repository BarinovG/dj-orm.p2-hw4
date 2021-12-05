from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, ArticleToTag, Tag


class ArticleToTagInlineFormset(BaseInlineFormSet):
    def clean(self):
        if sum([int(form.cleaned_data.get('is_main', False)) for form in self.forms]) != True:
            raise ValidationError('Должен быть 1 основной тэг')
        return super().clean()


class ArticleToTagInline(admin.TabularInline):
    model = ArticleToTag
    formset = ArticleToTagInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleToTagInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [ArticleToTagInline]