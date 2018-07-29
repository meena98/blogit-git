from blogit.apps.core.renderers import BlogitJSONRenderer


class UserJSONRenderer(BlogitJSONRenderer):
    object_label = 'user'
    pagination_object_label = 'users'
    pagination_count_label = 'usersCount'

    def render(self, data, media_type=None, renderer_context=None):
        token = data.get('token', None)

        if token is not None and isinstance(token, bytes):

            data['token'] = token.decode('utf-8')

        return super(UserJSONRenderer, self).render(data)