from django.http import HttpResponse


class HttpResponseMixin(object):  # In python every class is a child class of object class. 
    def render_to_response(self, json_data):  # We need to pass json_data, While creating the object
        return HttpResponse(json_data, content_type='application/json')
    
