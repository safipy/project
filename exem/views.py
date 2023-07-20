from rest_framework.response import Response
from rest_framework import pagination, status
from .models import Exem
from .serializers import ExemSerializer, ExemValidateSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class Page(pagination.PageNumberPagination):
    page_size = 10


class ExemListCreateAPIView(ListCreateAPIView):
    queryset = Exem.objects.all()
    serializer_class = ExemSerializer
    page_class = Page

    def post(self, request, *args, **kwargs):
        serializer = ExemValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
        title = serializer.validated_data["title"]
        description = serializer.validated_data["description"]
        completed = serializer.validated_data["completed"]
        exem = Exem.objects.create(
            title=title, description=description, completed=completed
        )
        return Response(data=ExemSerializer(exem).data, status=status.HTTP_201_CREATED)


class ExemDeteilAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Exem.objects.all()
    serializer_class = ExemSerializer
    lookup_field = "id_exem"

    def put(self, request, *args, **kwargs):
        try:
            item = Exem.objects.get(id_exem=kwargs["id_exem"])
        except Exem.DoesNotExist:
            return Response(
                data={"error": "Is not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = ExemValidateSerializer(instance=item, data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
        # id_exem = serializer.validated_data['id_exem']
        title = serializer.validated_data["title"]
        description = serializer.validated_data["description"]
        completed = serializer.validated_data["completed"]
        item.title = title
        item.description = description
        item.completed = completed
        item.save()
        return Response(data=ExemSerializer(item).data, status=status.HTTP_200_OK)
