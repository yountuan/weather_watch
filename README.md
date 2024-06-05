# WeatherWatch
# Task: RESTful API for Sensor Goods Monitoring

**Customer:** WeatherWatch

## Task Description

WeatherWatch is developing a platform to monitor and manage weather data from various sensors and devices. The company needs a system to manage data related to weather conditions to help meteorologists and researchers analyze weather patterns and trends.

## Requirements

- **API Documentation:** Swagger
- **HTTP Methods:** GET, POST, PUT, DELETE
- **Authentication:** Oauth2
- **Error Handling:** Appropriate HTTP statuses and messages
- **Data Format:** JSON
- **Data Consistency:** Transaction mechanisms

## Restrictions

- Must use Django REST Framework and PostgreSQL for Backend Track.

## Q&A

- **Security:** Oauth2bfor authentication and role-based access.
- **Performance:** Data caching, query optimization, and horizontal scaling.
- **Testing:** Unit and integration testing using unittest.
- **Data Format:** JSON for data exchange.
- **Data Consistency:** Database transactions for integrity.

## Screenshots

1. **API Endpoints Overview:**
   ![API Endpoints Overview](/screenshots/Screenshot2024-06-05at0.08.25.png)
   ![API Endpoints Overview](/screenshots/Screenshot2024-06-05at10.09.29.png)
   ![API Endpoints Overview](/screenshots/Screenshot2024-06-05at10.08.06.png)
   ![API Endpoints Overview](/screenshots/Screenshot2024-06-05at10.07.57.png)
   ![API Endpoints Overview](/screenshots/Screenshot2024-06-05at10.08.11.pngg)



2. **Tests:**
   ![Tests](/screenshots/Screenshot2024-06-05at10.05.07.png)


3. **Project configs:**
   Docker-compose
   ![Docker-compose](/screenshots/Screenshot2024-06-01at18.10.31.png)
   ![Docker-compose](/screenshots/Screenshot2024-06-01at18.10.47.png)
   ![Docker-compose](/screenshots/Screenshot2024-06-01at18.10.54.png)


4. **Swagger Documentation:**
   ![Swagger Documentation](/screenshots/Screenshot2024-06-05at11.19.27.png)
   ![Swagger Documentation](/screenshots/Screenshot2024-06-05at11.19.31.png)


## Video Presentation

For a detailed demonstration of the project, please refer to the video linked below. This video walks through the setup, key features, and functionalities of the API:
https://drive.google.com/drive/folders/1BR_qLzhz5P1JVFfpLAKOqZHvO-NuY4hR?usp=sharing

## Deploy on Free Cloud Server (Render):
(Since it's a free server, it could work very slow. Sorry for that T_T)
https://ecotrack-izrf.onrender.com
Credentials to log in to admin panel are
'admin' for username and
'1' for password.