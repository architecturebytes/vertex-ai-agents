**Refer YouTube Video**: https://www.youtube.com/watch?v=H6nUoszwcrM

**BytesCommerce/tools/ProductInventoryTool/ProductInventoryManager.py**<br>
This cloud function returns product quantity.

**BytesCommerce/tools/ProductInventoryTool/OpenAPISchema.json**<br>
OpenAPI Schema that defines (the interfaces of) the above function (ProductInventoryManager.py).<br>
**_Important_**: In this schema - you must modify the function name URL, PATHS and operationId as per your implementation.

**BytesAgent**

Goal:<br>
Answer questions related to Products.

Instructions:
- Greet the user, ask them how you can help them.
- Ask the user for additional details when necessary.
- Use ${TOOL: ProductCatalogTool} to find information about Products like Product Id, Product Name, Description
- Use ${TOOL: ProductInventoryTool} to get quantity of a Product Id.

**ProductCatalogTool:**<br>
Description: This tool can provide product information like Product Id, Product Name and Product Description.

**ProductInventoryTool**<br>
Description: This tool can return quantity for a Product.

