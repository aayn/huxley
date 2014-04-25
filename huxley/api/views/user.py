# Copyright (c) 2011-2014 Berkeley Model United Nations. All rights reserved.
# Use of this source code is governed by a BSD License (see LICENSE).

from django.contrib.auth import login, logout
from django.http import Http404

from rest_framework import generics, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from huxley.accounts.models import HuxleyUser
from huxley.api.permissions import IsPostOrSuperuserOnly, IsUserOrSuperuser
from huxley.api.serializers import UserSerializer


class UserList(generics.ListCreateAPIView):
    authentication_classes = (SessionAuthentication,)
    queryset = HuxleyUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsPostOrSuperuserOnly,)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (SessionAuthentication,)
    queryset = HuxleyUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUserOrSuperuser,)


class CurrentUser(generics.GenericAPIView):
    authentication_classes = (SessionAuthentication,)

    def get(self, request, *args, **kwargs):
        '''Get the current user if they're authenticated.'''
        if not request.user.is_authenticated():
            raise Http404
        return Response(UserSerializer(request.user).data)

    def post(self, request, *args, **kwargs):
        '''Log in a new user.'''
        if request.user.is_authenticated():
            raise APIException('Another user is currently logged in.')

        data = request.DATA
        user, error = HuxleyUser.authenticate(data['username'],
                                              data['password'])
        if error:
            raise APIException(error)

        login(request, user)
        return Response(UserSerializer(user).data,
                        status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        '''Log out the currently logged-in user.'''
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)