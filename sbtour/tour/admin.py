from django.contrib import admin

from tour.models import TourStop


class TourAdmin(admin.ModelAdmin):
	date_hierarchy = "created"
	fields = ('published', 'title', 'subtitle', 'slug', 'url', 'content',
		      'description' )
	list_display = ['published', 'title', 'updated']
	list_display_links = ['title']
	list_editable  = ['published']
	list_filter = ['published', 'updated']
	prepopulated_fields = {'slug': ('title',)}
	search_fields = ['title', 'content', 'description']
	

admin.site.register(TourStop, TourAdmin)


