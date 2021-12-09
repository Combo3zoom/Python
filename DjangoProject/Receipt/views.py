from .models import Receipt
from rest_framework import generics, status, filters
from .serializers import ReceiptSerializer
from .custom_pagination import CustomOffsetPagination

from rest_framework.views import APIView
from rest_framework.response import Response
from .docs import Documentations
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator


@method_decorator(
    name="post",
    decorator=swagger_auto_schema(**Documentations.POST)
)
class ReceiptListCreate(generics.ListCreateAPIView):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer

    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ["id","recipientName", "recipientIban", "bank", "paymentType", "amount",
                    "paymentDatetime"]

    pagination_class = CustomOffsetPagination


class ReceiptDetail(APIView):

    def _get_object(self, pk):
        try:
            receipt = Receipt.objects.get(pk=pk)
        except Receipt.DoesNotExist:
            return Response({'message': 'The Receipt does not exist'},
                            status=status.HTTP_404_NOT_FOUND)
        else:
            return receipt

    @swagger_auto_schema(**Documentations.GET)
    def get(self, request, pk):
        receipt = self._get_object(pk)
        if isinstance(receipt, Response):
            return receipt

        receipt_serializer = ReceiptSerializer(receipt)
        return Response(receipt_serializer.data)

    @swagger_auto_schema(**Documentations.PUT)
    def put(self, request, pk):
        receipt = self._get_object(pk)
        if isinstance(receipt, Response):
            return receipt

        receipt_data = request.data
        receipt_serializer = ReceiptSerializer(receipt, data=receipt_data)
        if receipt_serializer.is_valid():
            receipt_serializer.save()
            return Response({"message": receipt_serializer.data},
                            status=status.HTTP_200_OK)
        return Response(receipt_serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(**Documentations.DELETE)
    def delete(self, request, pk):
        receipt = self._get_object(pk)
        if isinstance(receipt, Response):
            return receipt

        receipt.delete()
        return Response({'message': 'Receipt was deleted successfully!'},
                        status=status.HTTP_200_OK)