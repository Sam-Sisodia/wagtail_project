from wagtail_modeladmin.options import ModelAdmin, modeladmin_register
from wagtail_modeladmin.mixins import ThumbnailMixin

from .models import NewsPage ,NewsDetailPage


class NewsDetailPageModelAdmin(ThumbnailMixin, ModelAdmin):
    model = NewsDetailPage
    menu_label = 'Add news'
    # menu_icon = 'news'
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    # list_display = ('title', 'beds', 'baths', 'sq_ft', 'admin_thumb', 'site', 'live',)
    # search_fields = ('title',)
    # list_filter = ('beds', 'baths', 'live',)
    # thumb_image_field_name = 'hero_image'
    # list_export = (
    #     'id', 'short_description', 'description', 'hero_image', 
    #     'download_plan_link', 'customize_plan_link', 
    #     'price_starting_at', 'beds', 'baths', 'sq_ft', 
    #     'garages',  # Add all the other fields you want to include
    # )

modeladmin_register(NewsDetailPageModelAdmin)