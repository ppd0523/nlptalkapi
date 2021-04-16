from rest_framework.decorators import api_view
from django.http import HttpResponse
import json
from .user_func.analysis import analysis_pc
from django.conf import settings

@api_view(['POST'])
def analysis(request):
    if request.method == 'POST':
        file = request.POST['file']

        text, picture = analysis_pc(settings.BASE_DIR/"../talk"/file)
        res = json.dumps({'text': text, 'picture': picture})

    return HttpResponse(res, content_type='text/json')