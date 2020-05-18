from django.shortcuts import render

# Create your views here.

@api_view(['POST'])
@permission_classes((permissions.IsAuthenticated, ))
def get_controls_state(request):
    # Need security here
    duration = request.data['device']

    logger.info('Get the controls state for device id %s' % (control_id, duration))
    for 
        # maybe should be in interaction?
        [{state, pin_id, duration, pin_type}]
    return Response({'status': 'OK'})

