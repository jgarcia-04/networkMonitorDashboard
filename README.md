# Network Monitor Dashboard

A full-stack network monitoring system that collects real-time WiFi performance metrics and visualizes them in a live dashboard.

## Features

- Real-time latency monitoring
- Bandwidth tracking (bytes sent/received)
- SQLite data storage
- FastAPI backend
- React + Chart.js frontend
- Auto-refreshing dashboard

## Tech Stack

Backend:
- Python
- FastAPI
- SQLite

Frontend:
- React
- Chart.js

## How It Works

1. Python collector gathers network metrics every few seconds.
2. Data is stored in SQLite.
3. FastAPI serves metrics via REST API.
4. React frontend fetches and visualizes data in real-time.

## Future Improvements

- Deployment to cloud (AWS/GCP)
- Alerts and threshold notifications
