# Smart Trip Maker

Smart Trip Maker is a travel planning and booking system designed to help users organize trips, compare destinations, plan budgets, and complete bookings with a smooth user experience.

## Overview

The system is divided into three main components:

- Frontend: HTML, CSS, and JavaScript for the user interface and client-side logic.
- Backend: Python Flask for handling business logic, API endpoints, user requests, and booking processing.
- Database: MySQL for storing users, destinations, hotels, trips, and booking records.

## Project Flow

1. User enters trip details in the frontend.
2. Frontend validates and submits trip data to the backend.
3. Backend processes the request and performs business logic.
4. Database stores trip-related information.
5. Booking confirmation and trip details are returned to the user.

## Current Status

The current repository includes the initial project structure and planning files. The frontend prototype is represented in the project archive, while the backend and MySQL integration are planned for the next development phase.

## Planned Architecture

```text
Frontend (HTML + CSS + JS)
    -> sends travel requests
        -> Flask API (Backend)
            -> processes trip data
                -> MySQL Database
                    -> stores users, destinations, hotels, bookings
```

## Future Development Phases

- Phase 1: Frontend interface and local browser-based interaction
- Phase 2: Flask backend development and REST API
- Phase 3: MySQL schema and data persistence
- Phase 4: Booking workflow and trip confirmation
- Phase 5: Deployment and production-ready improvements

## Starter Backend Structure

The repository now includes a starter Flask backend and MySQL schema template to support the next development phase.

## Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

## Database Setup

Import the schema file into MySQL:

```sql
SOURCE database/schema.sql;
```

## Main Features Planned

- User registration and login
- Trip planning and destination selection
- Hotel search and booking
- Budget estimation
- Booking confirmation
- Admin or system management support

## Notes

This repository is designed as a starting point for the Smart Trip Maker project and can be expanded as the application grows.
