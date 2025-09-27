
from django.contrib import admin
from .models import SocialLink, TechCategory, Technology, WorkHistory, Project, Profile
from django.utils.html import format_html
from django.utils.safestring import mark_safe


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_full_name_tag', 'profile_image_tag', 'bio_tag', 'working_as', 'email', 'contact_number',
                    'resume_tag']
    list_filter = ['working_as']  
    search_fields = ['user__first_name', 'user__last_name', 'working_as', 'email'] 
    list_display_links = ['get_full_name_tag']
    def get_full_name_tag(self, obj):
        if obj.user:
            return f'{obj.user.first_name} {obj.user.last_name}'
        return "-"

    get_full_name_tag.short_description = 'Full Name'

    def profile_image_tag(self, obj):
        if obj.profile_image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit:cover; border-radius:50%;" />',
                               obj.profile_image.url)
        return "-"

    def bio_tag(self, obj):
        if obj.bio:
            return mark_safe(obj.bio)
        return "-"

    def resume_tag(self, obj):
        if obj.resume:
            return format_html('<a href="{}" target="_blank" >View</a>', obj.resume.url)
        return "-"


class SocialLinksAdmin(admin.ModelAdmin):
    list_display = ['id', 'profile', 'platform']
    list_display_links = ['profile']

    def platform(self, obj):
        if obj.link and obj.platform_name:
            return format_html('<a href="{}" target="_blank" >{}</a>', obj.link, obj.platform_name)
        return "-"


class TechCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'profile']
    list_display_links = ['name']


class TechnologyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'profile']
    list_display_links = ['name']


class WorkHistoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'company_name', 'designation', 'description_tag', 'start_date', 'end_date', 'present',
                    'profile']
    list_display_links = ['company_name']
    
    def description_tag(self, obj):
        if obj.description:
            return mark_safe(obj.description)
        return "-"

    description_tag.short_description = 'Description'


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'github_link_tag', 'description_tag', 'sortorder','profile']
    list_display_links = ['name']
    filter_horizontal = ('techs',)
    list_editable = ['sortorder']
    ordering = ['sortorder']

    def github_link_tag(self, obj):
        if obj.github_link:
            return format_html('<a href="{}" target="_blank">GitHub</a>', obj.github_link)
        return "-"

    github_link_tag.short_description = 'GitHub Link'

    def description_tag(self, obj):
        if obj.description:
            return mark_safe(obj.description)
        return "-"

    description_tag.short_description = 'Description'




    
admin.site.register(Profile, ProfileAdmin)
admin.site.register(SocialLink, SocialLinksAdmin)
admin.site.register(TechCategory, TechCategoryAdmin)
admin.site.register(Technology, TechnologyAdmin)
admin.site.register(WorkHistory, WorkHistoryAdmin)
admin.site.register(Project, ProjectAdmin)