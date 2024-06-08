*** Settings ***
Library    RequestsLibrary
Library    Collections
Library    JSONLibrary

*** Variables ***
${BASE_URL}    https://jsonplaceholder.typicode.com
${USER_ENDPOINT}    /users/1
${POSTS_ENDPOINT}    /posts/1
${COMMENTS_ENDPOINT}    /comments/1

*** Test Cases ***
Verify User Endpoint
    [Documentation]    Perform a GET request to the user endpoint and validate the response
    ${response} =    GET    ${BASE_URL}${USER_ENDPOINT}
    Should Be Equal As Numbers    ${response.status_code}    200
    Should Contain    ${response.headers['Content-Type']}    application/json
    ${user_data} =    Evaluate    json.loads('''${response.content}''')    modules=json
    Should Be Equal As Numbers    ${user_data['id']}    1
    Should Be Equal As Strings    ${user_data['name']}    Leanne Graham

Verify Posts Endpoint
    [Documentation]    Perform a GET request to the posts endpoint and validate the response
    ${response} =    GET    ${BASE_URL}${POSTS_ENDPOINT}
    Should Be Equal As Numbers    ${response.status_code}    200
    Should Contain    ${response.headers['Content-Type']}    application/json

    ${json_string} =    Set Variable    {"userId": 1, "id": 1, "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit", "body": "quia et suscipit\\nsuscipit recusandae consequuntur expedita et cum\\nreprehenderit molestiae ut ut quas totam\\nnostrum rerum est autem sunt rem eveniet architecto"}

    ${post_data} =    Evaluate    json.loads('''${json_string}''')    modules=json
    Should Be Equal As Numbers    ${post_data['userId']}    1
    Should Be Equal As Numbers    ${post_data['id']}    1

Verify Comments Endpoint
    [Documentation]    Perform a GET request to the comments endpoint and validate the response
    ${response} =    GET    ${BASE_URL}${COMMENTS_ENDPOINT}
    Should Be Equal As Numbers    ${response.status_code}    200
    Should Contain    ${response.headers['Content-Type']}    application/json
    ${comment_data} =    Evaluate    json.loads('''${response.content}''')    modules=json
    Should Be Equal As Numbers    ${comment_data['postId']}    1
    Should Be Equal As Numbers    ${comment_data['id']}    1