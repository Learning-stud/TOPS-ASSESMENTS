# blog_api/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Comment
from .serializers import CommentSerializer

@api_view(['GET', 'POST', 'DELETE'])
def comment_api(request, comment_id=None):
    if request.method == 'GET':
        if comment_id:
            comment = Comment.objects.get(id=comment_id)
            serializer = CommentSerializer(comment)
        else:
            comments = Comment.objects.all()
            serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        comment = Comment.objects.get(id=comment_id)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
