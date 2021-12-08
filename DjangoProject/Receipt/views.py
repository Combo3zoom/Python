from .models import Receipt
from rest_framework import generics, status, filters
from .serializers import ReceiptSerializer


from rest_framework.views import APIView
from rest_framework.response import Response


class ReceiptListCreate(generics.ListCreateAPIView):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer

    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ["id","recipientName", "recipientIban", "bank", "paymentType", "amount",
                    "paymentDatetime"]


class ReceiptDetail(APIView):

    def _get_object(self, pk):
        try:
            receipt = Receipt.objects.get(pk=pk)
        except Receipt.DoesNotExist:
            return Response({'message': 'The Receipt does not exist'},
                            status=status.HTTP_404_NOT_FOUND)
        else:
            return receipt

    def get(self, request, pk):
        receipt = self._get_object(pk)
        if isinstance(receipt, Response):
            return receipt

        receipt_serializer = ReceiptSerializer(receipt)
        return Response(receipt_serializer.data)

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

    def delete(self, request, pk):
        receipt = self._get_object(pk)
        if isinstance(receipt, Response):
            return receipt

        receipt.delete()
        return Response({'message': 'Receipt was deleted successfully!'},
                        status=status.HTTP_200_OK)