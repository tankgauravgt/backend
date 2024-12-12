# Main Dashboard

## Story
- Aggregated status of the flights in the given time range using `Flight Status` donut chart.

- Information about control aspects of the notifications. I.e., How many notifications are sent, how many are failed, and how many are successful, etc...

## Panels:

### `Flight Status` {Donut Chart}

It shows the status of the flights in the given time range. It shows the count of the completed, scheduled, ongoing and cancelled flights.

#### Endpoint: 
```
/dashboard/main/flightStatus?fromISOTime=<isoTime>&toISOTime=<isoTime>
```
See APPENDIX.md for more details on isoTime format.

#### Response:
```json
{
  "data": [
    {
        "completed": 10,
        "scheduled": 5,
        "ongoing": 3,
        "cancelled": 2
    }
  ]
}
```

### Flight List View
### Particular Flight View
