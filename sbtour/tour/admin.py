from django.contrib import admin

from tour.models import Stop


class StopAdmin(admin.ModelAdmin):
	date_hierarchy = "created"
	fieldsets = [('Stop Info', 
					{'fields': [('title', 'published',), 'subtitle','content', 'description']}),
				('QR Code',
					{'fields': ['slug', 'url']})]
	readonly_fields = ['url']
	list_display = ['published', 'title', 'updated']
	list_display_links = ['title']
	list_editable  = ['published']
	list_filter = ['published', 'updated']
	prepopulated_fields = {'slug': ('title',)}
	search_fields = ['title', 'subtitle', 'content', 'description']

	def url(self, obj):
		return obj.url()
	

admin.site.register(Stop, StopAdmin)


