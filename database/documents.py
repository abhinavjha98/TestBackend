from django_elasticsearch_dsl import (Document,fields,Index)
from .models import aa419

PUBLISHER_INDEX = Index('aa419_data')

PUBLISHER_INDEX.settings(
    number_of_shards=1,
    number_of_replicas=1
)

@PUBLISHER_INDEX.doc_type
class aa419Document(Document):
    
    id = fields.IntegerField(attr='id')
    fielddata=True
    url = fields.TextField(
        fields={
            'raw':{
                'type': 'keyword',
            }
            
        }
    )
    label = fields.TextField(
        fields={
            'raw': {
                'type': 'keyword',
                
            }
        },
    )
   

    class Django(object):
        model = aa419
