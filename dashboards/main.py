from flask import Blueprint
from flask import jsonify
from flask import request

main_bp = Blueprint('main', __name__)


# =========================================================
# Flight Status:
# =========================================================

@main_bp.route('/flightStatus', methods=['GET'])
def flightStatus():
    fromDatetime = request.args.get('fromDatetime')
    toDatetime = request.args.get('toDatetime')
    return jsonify({
        "data": [{
            "Completed": 10,
            "Scheduled": 5,
            "Ongoing": 3,
            "Cancelled": 2
        }]
    })


# =========================================================
# 
# =========================================================

