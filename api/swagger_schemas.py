from drf_yasg import openapi

get_average_price_schema = {
    "method": "GET",
    "manual_parameters": [
        openapi.Parameter(
            "product_id",
            openapi.IN_QUERY,
            description="Product ID",
            type=openapi.TYPE_INTEGER,
        ),
        openapi.Parameter(
            "start_date",
            openapi.IN_QUERY,
            description="Start date (YYYY-MM-DD)",
            type=openapi.TYPE_STRING,
        ),
        openapi.Parameter(
            "end_date",
            openapi.IN_QUERY,
            description="End date (YYYY-MM-DD)",
            type=openapi.TYPE_STRING,
        ),
    ],
    "responses": {
        200: openapi.Response(
            "OK",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={"average_price": openapi.Schema(type=openapi.TYPE_NUMBER)},
            ),
        ),
        400: "Bad Request",
        404: "Not Found",
    },
}
