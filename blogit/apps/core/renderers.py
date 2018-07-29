import json

from rest_framework.renderers import JSONRenderer
#from rest_framework.utils.serializer_helpers import ReturnList


class BlogitJSONRenderer(JSONRenderer):
    charset = 'utf-8'
    object_label = 'object'
    #object_label_plural='objects'
    pagination_object_label = 'objects'
    pagination_count_label = 'count'

    # def render(self, data, media_type=None, renderer_context=None):
    #     if isinstance(data,ReturnList):
    #         _data=json.loads(super(BlogitJSONRenderer,self).render(data).decode('utf-8'))
    #         return json.dumps({
    #             self.object_label_plural:_data
    #         })
    #     else:
    #         errors = data.get('errors', None)
    #
    #         if errors is not None:
    #             return super(BlogitJSONRenderer, self).render(data)
    #
    #         return json.dumps({
    #             self.object_label: data
    #         })

    def render(self, data, accepted_media_type=None, renderer_context=None):
        if data.get('results',None) is not None:
            return json.dumps({
                self.pagination_object_label: data['results'],
                self.pagination_count_label: data['count']
            })
        elif data.get('errors', None) is not None:
            return super(BlogitJSONRenderer, self).render(data)

        else:
            return json.dumps({self.object_label: data})
