from api.pagination import LimitPageNumberPagination
from django.contrib.auth import get_user_model
from djoser.views import UserViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Follow
from .serializers import FollowSerializer

User = get_user_model()


class MyUserViewSet(UserViewSet):
    pagination_class = LimitPageNumberPagination

    @action(detail=True, permission_classes=[IsAuthenticated])
    def subscribe(self, request, id=None):
        user = request.user
        author = get_object_or_404(User, id=id)

        if Follow.objects.filter(user=user, author=author).exists():
            return Response({
                'error': 'Вы уже подписаны на данного пользователя'
            }, status=status.HTTP_400_BAD_REQUEST)
        if user == author:
            return Response({
                'error': 'Нельзя подписаться на самого себя!'
            }, status=status.HTTP_400_BAD_REQUEST)

        follow = Follow.objects.create(user=user, author=author)
        serializer = FollowSerializer(
            follow, context={'request': request}
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @subscribe.mapping.delete
    def unsubscribe(self, request, id=None):
        user = request.user
        author = get_object_or_404(User, id=id)
        follow = Follow.objects.filter(user=user, author=author)

        if user == author:
            return Response({
                'error': 'Нельзя отписаться от самого себя!'
            }, status=status.HTTP_400_BAD_REQUEST)

        if follow.exists():
            follow.delete()
            return Response({
                'accept': f'Вы успешно отписались от пользователя {author}!'
            }, status=status.HTTP_204_NO_CONTENT)
        return Response({
            'error': 'Вы уже отписались!'
        }, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, permission_classes=[IsAuthenticated])
    def subscriptions(self, request):
        user = request.user
        queryset = Follow.objects.filter(user=user)
        pages = self.paginate_queryset(queryset)
        serializer = FollowSerializer(
            pages,
            many=True,
            context={'request': request}
        )
        return self.get_paginated_response(serializer.data)
