**Refer YouTube Video**: https://www.youtube.com/watch?v=H6nUoszwcrM

**BytesCommerce/tools/ProductInventoryTool/ProductInventoryManager.py**<br>
This cloud function returns product quantity.

**BytesCommerce/tools/ProductInventoryTool/OpenAPISchema.json**<br>
OpenAPI Schema that defines (the interfaces of) the above function (ProductInventoryManager.py).<br>
**_Important_**: In this schema - you must modify the function name URL, PATHS and operationId as per your implementation.

**BytesAgent**

Goal:<br>
Answer questions related to Products.

Instructions:<br>
_-_ Greet the user, ask them how you can help them.<br>
_-_ Ask the user for additional details when necessary.<br>
_-_ Use ${TOOL: ProductCatalogTool} to find information about Products like Product Id, Product Name, Description<br>
_-_ Use ${TOOL: ProductInventoryTool} to get quantity of a Product Id.

**ProductCatalogTool:**<br>
Description: This tool can provide product information like Product Id, Product Name and Product Description.

**ProductInventoryTool**<br>
Description: This tool can return quantity for a Product.

**How to get OAuth Client ID**

In Google Cloud Console > APIs & Services<br>

  _Create Credentials_ > OAuth Client ID<br>
    Application Type: Web Application<br>
    Name: Provide Some Name<br>
    JavaScript Origins: https://YourWebsite (That Hosts DialogflowMessenger Page)<br>
    Hit Save, and copy Client ID<br>

  _OAuth Consent Screen_ > <br>
    Provie App Name (this will be displayed to user), Support Email, Developer Contact Email, Domain Info (optional)  <br>
    Save & Continue <br>
    Publish App. 

  _Library_ > <br>
    Enable DialogFlow API (if not enabled DialogFlow Messenger may not work and return a 403 error)

  Replace the oauth-client-id="INSERT_OAUTH_CLIENT_ID" in the html fragment of dialogflow messenger integration (for Authenticated API) with the Client ID copied earlier (while creating Credentials).
