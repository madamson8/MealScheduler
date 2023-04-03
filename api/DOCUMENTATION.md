#API CALLS AND CODES

endpoints are listed as follows

link/ -REQUIRED METHOD TYPE ? field 1, -optional-field 2 | response 1, response 2

USER ENDPOINTS:
1. register/ -POST ? username, password, v_password | 201 CREATED, 400 BAD REQUEST, 405 METHOD NOT ALLOWED, 500 SERVER ERROR
2. login/ -POST ? username, password
3. logout/ 

FOOD ENDPOINTS:
1. create-food/ -POST ? name, -calories, -protein, -fat, rel_user ? 201 CREATED, 405 METHOD NOT ALLOWED, 400 BAD REQUEST