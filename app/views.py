from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from app.models import Event
from app.serializers import EventSerializer, FilterSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('id')
    serializer_class = EventSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_queryset(self):
        queryset = super().get_queryset()

        filters_serializer = FilterSerializer(data=self.request.query_params)
        filters_serializer.is_valid(raise_exception=True)

        event_type = self.request.query_params.get('type')
        user_id = self.kwargs.get('user_id')
        repo_id = self.kwargs.get('repo_id')

        if event_type:
            queryset = queryset.filter(type=event_type)

        if user_id:
            queryset = queryset.filter(actor_id=user_id)

        if repo_id:
            queryset = queryset.filter(repo_id=repo_id)

        return queryset.order_by('id')

    @action(detail=False, methods=['get'])
    def get_events_by_user_id(self, request, user_id=None):
        events = Event.objects.filter(actor_id=user_id).order_by('id')
        serializer = EventSerializer(events, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def get_events_by_repo_id(self, request, repo_id=None):
        events = Event.objects.filter(repo_id=repo_id).order_by('id')
        serializer = EventSerializer(events, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
