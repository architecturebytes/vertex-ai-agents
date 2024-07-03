**Refer YouTube Video**: https://www.youtube.com/watch?v=H6nUoszwcrM

**BytesCommerce/tools/ProductInventoryTool/ProductInventoryManager.py**<br>
This cloud function returns product quantity.

NOTE: The above function uses flask library. <br>
If the (flask) dependency is not being automatically handled in GCP, add a line with text 'flask' in requirements.txt file that exists alongside cloud function python file.

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

**If you want Unauthenticated Agent:** (This step is not shown in the demo)<br>
Go to Dialoglfow CX screen using the menu on the left and hit the Publish button - you will get HTML fragment that you can embed in your webpage. You can add domain restriction before publishing.

**If you want Authenticated Agent:**<br>
You will need OAuth Client ID. 

**How to get OAuth Client ID**

In Google Cloud Console > APIs & Services<br>

  _Create Credentials_ > OAuth Client ID<br>
    Application Type: Web Application<br>
    Name: Provide Some Name<br>
    JavaScript Origins: https://YourWebsite (That hosts DialogflowMessenger page)<br>
    Hit Save, and copy Client ID<br>

  _OAuth Consent Screen_ > <br>
    Provie App Name (this will be displayed to user), Support Email, Developer Contact Email, Domain Info (optional)  <br>
    Save & Continue <br>
    Publish App. 

  _Library_ > <br>
    Enable DialogFlow API (if not enabled DialogFlow Messenger may not work and return a 403 error)

  Replace the oauth-client-id="INSERT_OAUTH_CLIENT_ID" in the html fragment of dialogflow messenger integration (for Authenticated API) with the Client ID copied earlier (while creating Credentials).

  **Invoke Agent via API call**

In Google Cloud Console > Service Accounts > Create New Service Account<br>
For Role choose 'Dialogflow API Client'<br>
Create Key (JSON) & Save It.

Now use this program to generate Access token **Utils\GetAccessToken.py**<br>
Invoke agent: **Utils\InvokeAgent.py**

Ref:<br>
https://cloud.google.com/dialogflow/vertex/docs/quick/api<br>
https://cloud.google.com/dialogflow/es/docs/how/region#regions<br>
Note that there have been some changes to dialogflow endpoints over a period of time.
