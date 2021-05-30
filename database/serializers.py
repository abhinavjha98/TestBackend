  
import json
from .models import aa419

from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .documents import *

class aa419DocumentSerializer(DocumentSerializer):

    class Meta(object):
        """Meta options."""
        model = aa419
        document = aa419Document
        fields = (
            'url',
            'label',
        )
        def get_location(self, obj):
            """Represent location value."""
            try:
                return obj.location.to_dict()
            except:
                return {}