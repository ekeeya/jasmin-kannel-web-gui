
#
#  Copyright (c) 2024
#  File created on 2024/7/17
#  By: Emmanuel Keeya
#  Email: ekeeya@thothcode.tech
#
#  This project is licensed under the GNU General Public License v3.0. You may
#  redistribute it and/or modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This project is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
#  without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#  See the GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License along with this project.
#  If not, see <http://www.gnu.org/licenses/>.
#

import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from web.renderers.renderers import PlainTextRenderer, CustomPlainTextRenderer

logger = logging.getLogger('main')


class SMSCallback(APIView):
    renderer_classes = [PlainTextRenderer, CustomPlainTextRenderer]

    def post(self, request, *args, **kwargs):
        try:
            # Handle form-encoded data
            if request.content_type == 'application/x-www-form-urlencoded':
                data = request.POST
            else:  # Default to JSON data
                data = request.data
            logger.info(f"Received DLR: {data}")

            return Response('ACK/Jasmin', status=status.HTTP_200_OK, content_type='text/plain')
        except Exception as e:
            logger.error(f"Error processing DLR: {e}")
        return Response('Error', status=status.HTTP_500_INTERNAL_SERVER_ERROR, content_type='text/plain')
