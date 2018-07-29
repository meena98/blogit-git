from blogit.apps.core.renderers import BlogitJSONRenderer


class ProfileJSONRenderer(BlogitJSONRenderer):
    object_label = 'profile'
    pagination_object_label = 'profiles'
    pagination_count_label = 'profilesCount'