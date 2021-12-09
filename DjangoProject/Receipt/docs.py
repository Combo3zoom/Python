from drf_yasg import openapi


class Examples:
    Receipt_example = {
        "recipientName": "string",
        "recipientIBAN": "string",
        "bank": "enum",
        "paymentType": "enum",
        "amount": "float",
        "paymentDatetime": "datetime"
    }

    Receipt_absent = {
        "status": 404,
        "message": "The Receipt does not exist"
    }

    Receipt_wrong = {
        "status": 400,
        "errors": {
            "field_1": "error_1",
            "field_2": "error_2"
        }
    }

    Receipt_add = {
        "status": 200,
        "receipt": Receipt_example
    }

    Receipt_update = {
        "status": 200,
        "message": Receipt_example
    }

    Receipt_delete = {
        "status": 200,
        "message": "Receipt was deleted successfully!"
    }

    Receipt_INPUT_PARAMETER = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            "recipientName": openapi.Schema(type=openapi.TYPE_STRING,
                                       max_length=30),
            "recipientIBAN": openapi.Schema(type=openapi.TYPE_STRING,
                                                     description='UA195000010000032003364901026',
                                                     max_length=29),
            "bank": openapi.Schema(type=openapi.TYPE_STRING,
                                            description='Enum',
                                            max_length=20),
            "paymentType": openapi.Schema(type=openapi.TYPE_STRING,
                                         description='enum'),
            "amount": openapi.Schema(type=openapi.TYPE_NUMBER),
            "paymentDatetime": openapi.Schema(type=openapi.TYPE_STRING,
                                      format="datetime"),
        })


class Documentations:
    POST = {
        "operation_description": "Insert new Receipt into a database",
        "responses": {
            "200": openapi.Response(
                description="Valid receipt sent -> write to database",
                examples={
                    "application/json": Examples.Receipt_add
                }
            ),
            "400": openapi.Response(
                description="Invalid receipt sent -> discard",
                examples={
                    "application/json": Examples.Receipt_wrong
                }
            ),
        }
    }

    GET = {
        "responses": {
            "200": openapi.Response(
                description="Valid id -> obtain receipt from database",
                examples={
                    "application/json": Examples.Receipt_example
                }
            ),
            "404": openapi.Response(
                description="Invalid id -> response HTTP 404",
                examples={
                    "application/json": Examples.Receipt_absent
                }
            ),
        }
    }

    PUT = {
        "request_body": Examples.Receipt_INPUT_PARAMETER,
        "operation_description": "Edit Receipt record by ID in database",
        "responses": {
            "200": openapi.Response(
                description="Valid id -> obtain receipt from database",
                examples={
                    "application/json": Examples.Receipt_update
                }
            ),
            "400": openapi.Response(
                description="Invalid receipt sent -> discard",
                examples={
                    "application/json": Examples.Receipt_wrong
                }
            ),
            "404": openapi.Response(
                description="Invalid id -> response HTTP 404",
                examples={
                    "application/json": Examples.Receipt_absent
                }
            ),
        }
    }

    DELETE = {
        "operation_description": "Delete Receipt by id from database",
        "responses": {
            "200": openapi.Response(
                description="Valid id -> obtain receipt from database",
                examples={
                    "application/json": Examples.Receipt_delete
                }
            ),
            "404": openapi.Response(
                description="Invalid id -> response HTTP 404",
                examples={
                    "application/json": Examples.Receipt_absent
                }
            ),
        }
    }