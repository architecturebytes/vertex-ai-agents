from flask import Flask, request, make_response
import json

app = Flask(__name__)

@app.route('/ProductInventoryManager', methods=['GET'])
def getProductQuantity(request):
    product_id = request.args.get('productId')
    if not product_id:
        return make_response(json.dumps({"error": "Missing productId parameter"}), 400)

    # Simulating a database lookup
    inventory = {
        "productId": product_id,
        "quantity": 10  # Example quantity, should be retrieved from database
    }

    return make_response(json.dumps(inventory), 200, {'Content-Type': 'application/json'})
