from django.contrib import admin
from .models import *
from django.utils.html import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

###
admin.site.site_title = "KinoSearch"
admin.site.site_header = "КиноSearch"
###

###ckeditor###

class MovieAdminForm(forms.ModelForm):
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget()) #Название переменной аналогично имени поля модели

    class Meta:
        model = Movie
        fields = '__all__'



##############

class ImageGet():   #класс с общим методом получения миниатюры изображения картинки(для актеров, кадров и тд)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="100">')

    get_image.short_description = "Изображение"


@admin.register(Actor) #Декоратор( тоже самое что admin.site.register(actor) + обёртываемый класс внутри
class ActorAdmin(admin.ModelAdmin, ImageGet):
    list_display = ('name', 'age', 'get_image')
    list_display_links = ('name',) #поле name теперь можно нажать (оно теперь ссылка)
    readonly_fields = ('get_image',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description','url', 'id') #данные поля теперь отображаются колонками
    list_display_links = ('name', )  # поле name теперь можно нажать (оно теперь ссылка)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'url')


class ReviewInLine(admin.TabularInline):
    model = Reviews
    extra = 1 #теперь внизу списка отзывов (в категории фильмы) в конце 1 пустой отзыв для редактирования
    readonly_fields = ('name', 'email')

class MovieShotsInLine(admin.TabularInline, ImageGet):
    model = MovieShots
    extra = 1
    readonly_fields = ('get_image',)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'draft')
    list_filter = ('category', 'year') # по полям год и категория будет фильтрация списка фильмов(выбор фильтра справа)
    search_fields = ('title', 'category__name',)  #category__name = обращение к таблице категорий по колонке имя
    inlines = [ReviewInLine, MovieShotsInLine] # класс ReviewInLine добавляется в список Inlines - при переходе на фильм видны все Reviews связанные с ним полем FK
    save_on_top = True        #меню с кнопкой сохранения теперь и сверху и снизу
    save_as = True
    actions = ['publish', 'unpublish', 'rename',]
    readonly_fields = ('get_poster',)
    forms = MovieAdminForm  #Форма с включенный ckeditor для поля description(Описания фильма)
    list_editable = ('draft',)   #превращает колонку draft(условие черновик или нет) в редактируемый чекбокс, можно выбрать прям из меню черновик или нет несколько фильмов сразу
    fieldsets = (
        (None, {
         'fields': (('title', 'tagline'), )      # кортеж с кортежами внутри, в каждом внутреннем кортеже 2 записи: None и словарь с ключем и значением ввиде кортежа
        }),
        (None, {
            'fields': (('description', 'poster', 'get_poster'),)
        }),
        (None, {
            'fields': (('year', "world_premiere", 'country'),)
        }),
        ('Актёры, режиссеры и тд', {
            'classes': ('collapse',),
            'fields': (('actors', 'directors', 'genres', 'category'),)
        }),
        (None, {
            'fields': (('budget', 'fees_in_usa', 'fess_in_world'),)
        }),
        (None, {
            'fields': (('url', 'draft'),)
        }),

    )

    def get_poster(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="100" height="110">')

    get_poster.short_description = "Миниатюра постера"

    def unpublish(self, request, queryset):
        row_update = queryset.update(draft=True)
        if row_update == '1':
            message_bit = '1 запись была обновлена'
        else:
            message_bit = f'{row_update} записей были обновлены'
        self.message_user(request, f'{message_bit}')

    def publish(self, request, queryset):
        row_update = queryset.update(draft=False)
        if row_update == '1':
            message_bit = '1 запись была обновлена'
        else:
            message_bit = f'{row_update} записей были обновлены'
        self.message_user(request, f'{message_bit}')

    def rename(self, request, queryset):
        row_update = queryset.update(title='Помечено на удаление')
        if row_update == '1':
            message_bit = '1 запись была помечена как ненужная'
        else:
            message_bit = f'{row_update} записей были помечены как ненужные'
        self.message_user(request, f'{message_bit}')

    publish.short_description = 'Опубликовать'
    unpublish.short_description = 'Снять с публикации'
    publish.allowed_permission = ('change', )
    unpublish.allowed_permission = ('change',)
    rename.allowed_permission = ('change', )
    rename.short_description = 'Переименовать в "Ненужная запись"'


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'parent', 'movie', 'id')
    readonly_fields = ('name', 'email') # эти поля нельзя редактировать из админки



@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin, ImageGet):
    list_display = ('title', 'description', 'get_image', 'movie',)

@admin.register(RatingStar)
class RatingStarAdmin(admin.ModelAdmin):
    list_display = ('value',)


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('movie', 'ip', 'star')



# Register your models here.
