from flask import Blueprint
from flask import jsonify
from flask import request

flightlist_bp = Blueprint('flightlist', __name__)


# =========================================================
# Flight Status:
# =========================================================

@flightlist_bp.route('/allFlights', methods=['GET'])
def flightStatus():
    fromDatetime = request.args.get('fromDatetime')
    toDatetime = request.args.get('toDatetime')
    return jsonify({
        "data": [
            {
                "flightNumber": "AI202",
                "origin": "DEL",
                "destination": "BOM",
                "departureTime": "2020-01-01T12:00:00.000Z",
                "arrivalTime": "2020-12-01T14:00:00.000Z",
                "status": "Completed"
            },
            {
                "flightNumber": "AI202",
                "origin": "DEL",
                "destination": "BOM",
                "departureTime": "2020-01-02T12:00:00.000Z",
                "arrivalTime": "2020-01-02T14:00:00.000Z",
                "status": "Completed"
            },
            {
                "flightNumber": "AI493",
                "origin": "COK",
                "destination": "AMD",
                "departureTime": "2020-01-03T12:00:00.000Z",
                "arrivalTime": "2020-01-03T14:00:00",
                "status": "Scheduled"
            },
            {
                "flightNumber": "AI101",
                "origin": "DEL",
                "destination": "BOM",
                "departureTime": "2020-01-04T12:00:00.000Z",
                "arrivalTime": "2020-01-04T14:00:00.000Z",
                "status": "Ongoing"
            },
            {
                "flightNumber": "AI303",
                "origin": "DEL",
                "destination": "BOM",
                "departureTime": "2020-01-05T12:00:00.000Z",
                "arrivalTime": "2020-01-05T14:00:00.000Z",
                "status": "Cancelled"
            },
            {
                "flightNumber": "AI202",
                "origin": "DEL",
                "destination": "BOM",
                "departureTime": "2020-01-01T12:00:00.000Z",
                "arrivalTime": "2020-12-01T14:00:00.000Z",
                "status": "Completed"
            },
            {
                "flightNumber": "AI202",
                "origin": "DEL",
                "destination": "BOM",
                "departureTime": "2020-01-02T12:00:00.000Z",
                "arrivalTime": "2020-01-02T14:00:00.000Z",
                "status": "Completed"
            },
            {
                "flightNumber": "AI493",
                "origin": "COK",
                "destination": "AMD",
                "departureTime": "2020-01-03T12:00:00.000Z",
                "arrivalTime": "2020-01-03T14:00:00",
                "status": "Scheduled"
            },
            {
                "flightNumber": "AI101",
                "origin": "DEL",
                "destination": "BOM",
                "departureTime": "2020-01-04T12:00:00.000Z",
                "arrivalTime": "2020-01-04T14:00:00.000Z",
                "status": "Ongoing"
            },
            {
                "flightNumber": "AI303",
                "origin": "DEL",
                "destination": "BOM",
                "departureTime": "2020-01-05T12:00:00.000Z",
                "arrivalTime": "2020-01-05T14:00:00.000Z",
                "status": "Cancelled"
            }
        ]
    })


# =========================================================
# Channelwise Notification Distribution:
# =========================================================

@flightlist_bp.route('/channelwiseNotificationDistribution', methods=['GET'])
def channelwiseNotificationDistribution():
    fromDatetime = request.args.get('fromDatetime')
    toDatetime = request.args.get('toDatetime')
    return jsonify({
        "data": [
            {
                "axis": "",
                "toBeSent": 2,
                "sent": 5,
                "missed": 6,
                "failed": 20,
                "duplicated": 5,
                "delayed": 12
            }
        ]
    })
