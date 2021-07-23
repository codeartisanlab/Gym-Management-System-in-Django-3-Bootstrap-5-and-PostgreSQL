from django.contrib import admin
from . import models

class BannerAdmin(admin.ModelAdmin):
	list_display=('alt_text','image_tag')
admin.site.register(models.Banners,BannerAdmin)

class ServiceAdmin(admin.ModelAdmin):
	list_display=('title','image_tag')
admin.site.register(models.Service,ServiceAdmin)

class PageAdmin(admin.ModelAdmin):
	list_display=('title',)
admin.site.register(models.Page,PageAdmin)

class FaqAdmin(admin.ModelAdmin):
	list_display=('quest',)
admin.site.register(models.Faq,FaqAdmin)

class EnquiryAdmin(admin.ModelAdmin):
	list_display=('full_name','email','detail','send_time')
admin.site.register(models.Enquiry,EnquiryAdmin)

class GalleryAdmin(admin.ModelAdmin):
	list_display=('title','image_tag')
admin.site.register(models.Gallery,GalleryAdmin)

class GalleryImageAdmin(admin.ModelAdmin):
	list_display=('alt_text','image_tag')
admin.site.register(models.GalleryImage,GalleryImageAdmin)

class SubPlanAdmin(admin.ModelAdmin):
	list_editable=('highlight_status',)
	list_display=('title','price','highlight_status')
admin.site.register(models.SubPlan,SubPlanAdmin)

class SubPlanFeatureAdmin(admin.ModelAdmin):
	list_display=('title','subplan')
admin.site.register(models.SubPlanFeature,SubPlanFeatureAdmin)
