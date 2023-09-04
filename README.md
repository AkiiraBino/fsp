# Running the Application

This section provides instructions for running the FastAPI application in different modes.

## Development Mode

To run the application in development mode, you have two options:

### Option 1: Using Docker Compose

You can use Docker Compose to set up and run the application along with its dependencies.

docker-compose -f docker-compose.dev.yaml up --build


### Option 2: Using Makefile

Alternatively, you can use the Makefile for a simplified command:

make dev


# Example

## Request

GET http://127.0.0.1:8080/api/v1/cities/?started_city=Factoria&target_city=Redmond

## Response

{
  "city": "Factoria",
  "result": {
    "target_city": "Redmond",
    "distance": 8
  }
}


# FastAPI API Documentation

This documentation provides information about the FastAPI API.

## Table of Contents

- [Introduction](#introduction)
- [API Base URL](#api-base-url)
- [Endpoints](#endpoints)
  - [Get Distance between Cities](#get-distance-between-cities)
  - [Get All Cities](#get-all-cities)
  - [Get All Roads](#get-all-roads)
- [Data Models](#data-models)
  - [CitySchema](#cityschema)
  - [DistanceResultSchema](#distanceresultschema)
  - [FSPResponseSchema](#fsponlyschema)
  - [HTTPValidationError](#httpvalidationerror)
  - [RoadSchema](#roadschema)
  - [ValidationError](#validationerror)

## Introduction

This API provides functionality related to cities, distances, and roads. It allows you to query information about cities, calculate distances between cities, and retrieve road data.

## API Base URL

The base URL for all API endpoints is `/api/v1`.

## Endpoints

### Get Distance between Cities

- **URL**: `/cities/`
- **HTTP Method**: GET
- **Summary**: Get Distance
- **Operation ID**: `get_distance_cities__get`
- **Parameters**:
  - `started_city` (query, required): The name of the starting city.
  - `target_city` (query, required): The name of the target city.
- **Responses**:
  - `200`: Successful Response
    - Content Type: `application/json`
    - Schema: [FSPResponseSchema](#fsponlyschema)
  -  `404`: Not found
    -  Content Type: `application/json`
    -  Schema: [HTTPException]
  - `422`: Validation Error
    - Content Type: `application/json`
    - Schema: [HTTPValidationError](#httpvalidationerror)

### Get All Cities

- **URL**: `/cities/city`
- **HTTP Method**: GET
- **Summary**: Get All City
- **Operation ID**: `get_all_city_cities_city_get`
- **Responses**:
  - `200`: Successful Response
    - Content Type: `application/json`
    - Schema: Array of [CitySchema](#cityschema)

### Get All Roads

- **URL**: `/cities/road`
- **HTTP Method**: GET
- **Summary**: Get All Road
- **Operation ID**: `get_all_road_cities_road_get`
- **Responses**:
  - `200`: Successful Response
    - Content Type: `application/json`
    - Schema: Array of [RoadSchema](#roadschema)

## Data Models

### CitySchema

- **Type**: Object
- **Properties**:
  - `id` (integer, required): The ID of the city.
  - `name` (string, maxLength: 200, required): The name of the city.

### DistanceResultSchema

- **Type**: Object
- **Properties**:
  - `target_city` (string, required): The name of the target city.
  - `distance` (integer, required): The calculated distance.

### FSPResponseSchema

- **Type**: Object
- **Properties**:
  - `city` (string, required): The name of the city.
  - `result` (object, required): Distance calculation result as per [DistanceResultSchema](#distanceresultschema).

### HTTPValidationError

- **Type**: Object
- **Properties**:
  - `detail` (array, required): Array of validation error details as per [ValidationError](#validationerror).

### RoadSchema

- **Type**: Object
- **Properties**:
  - `id` (integer, required): The ID of the road.
  - `previous_city` (integer, required): The ID of the previous city in the road.
  - `next_city` (integer, required): The ID of the next city in the road.
  - `distance` (integer, required): The distance between the cities.

### ValidationError

- **Type**: Object
- **Properties**:
  - `loc` (array, required): Location of the validation error.
  - `msg` (string, required): Error message.
  - `type` (string, required): Error type.
