## Market Price Monitor Documentation

## Introduction

The scope of this app is to calculate the average price for a certain product for a certain period. The average price is calculated: the sum of the price on each day/number of days. This documentation provides instructions on how to clone the project, run it using Docker Compose, run tests inside Docker, and use Swagger for API documentation.

## Clone the Project

To clone the project repository, follow these steps:

1. Navigate to the desired directory:

```bash
   cd /path/to/destination
```

2. Clone the repository:

```bash
   git clone https://github.com/AlexPrunici/ProductPriceMonitor.git
```

## Running the Application with Docker Compose

To run the Market Price Monitor application using Docker Compose, follow these steps:

1. Navigate to the project directory:

```bash
   cd /path/to/market_price_monitor
```

2. Build and start Docker containers:

```bash
   docker-compose up -d --build
```

3. Access the application at `http://localhost:8000`.

## Running Tests Inside Docker

To run tests for the Market Price Monitor application inside Docker containers, follow these steps:

1. Ensure Docker containers are running:

```bash
   docker-compose up -d --build
```

2. Open a new terminal window and access the running Docker container:

```bash
   docker-compose exec web bash
```

3. Run tests inside the Docker container:

```bash
   python manage.py test
```

## Using Swagger for API Documentation

Market Price Monitor provides API documentation using Swagger. Follow these steps to access the Swagger documentation:

1. Ensure Docker containers are running:

```bash
   docker-compose up -d --build
```

2. Access the Swagger documentation at `http://localhost:8000/swagger`.

## Endpoints Documentation

## Swagger Documentation:

- Endpoint: /swagger/
- Method: GET
- Description: Provides Swagger documentation for the API.
- Usage: Access the Swagger documentation at `http://localhost:8000/swagger/`.

## Admin Interface:

- Endpoint: /admin/
- Method: GET
- Description: Provides access to the Django admin interface.
- Usage: Access the admin interface at `http://localhost:8000/admin/`.

## API Endpoints:

1. Product List:
   - Endpoint: /api/products/
   - Method: GET
   - Description: Retrieves a list of all products.
2. Retrieve Product by ID:
   - Endpoint: /api/products/<int:pk>/
   - Method: GET
   - Description: Retrieves details of a specific product by its ID.
3. Create Product:

   - Endpoint: /api/products/create/
   - Method: POST
   - Description: Creates a new product.
   - Request Body:
     ```
     {
         "name": ""
     }
     ```

4. Price List:
   - Endpoint: /api/prices/
   - Method: GET
   - Description: Retrieves a list of all prices.
5. Retrieve Price by ID:
   - Endpoint: /api/prices/<int:pk>/
   - Method: GET
   - Description: Retrieves details of a specific price by its ID.
6. Create Price:

   - Endpoint: /api/prices/create/
   - Method: POST
   - Description: Creates a new price.
   - Request Body:
     ```
     {
         "product": "",
         "price": "",
         "date": ""
     }
     ```

7. Calculate Average Price:
   - Endpoint: /api/prices/average/
   - Method: GET
   - Description: Calculates the average price of all products for a certain period.
   - Query Parameters:
     - product_id: ID of the product (required)
     - start_date: Start date of the period (required, format: YYYY-MM-DD)
     - end_date: End date of the period (required, format: YYYY-MM-DD)
