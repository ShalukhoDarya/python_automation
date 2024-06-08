*** Settings ***
Library    RequestsLibrary

*** Variables ***
${BASE_URL}    https://jsonplaceholder.typicode.com

*** Test Cases ***
Create a Post
    ${headers}=    Create Dictionary    Content-Type=application/json
    ${payload}=    Create Dictionary    title=foo    body=bar    userId=1
    ${response}=    POST    ${BASE_URL}/posts    data=${payload}    headers=${headers}
    Should Be Equal As Numbers    ${response.status_code}    201
    ${json}=    Set Variable    ${response.json()}
    Should Contain    ${json}    title    foo

Update a Post
    ${headers}=    Create Dictionary    Content-Type=application/json
    ${payload}=    Create Dictionary    title=foo_updated
    ${response}=    PUT   ${BASE_URL}/posts/1    data=${payload}    headers=${headers}
    Should Be Equal As Numbers    ${response.status_code}    200
    ${json}=    Set Variable    ${response.json()}
    Should Contain    ${json}    title    foo_updated

Partial Update a Post
    ${headers}=    Create Dictionary    Content-Type=application/json
    ${payload}=    Create Dictionary    title=foo_partial_updated
    ${response}=        PATCH     ${BASE_URL}/posts/1    data=${payload}    headers=${headers}
    Should Be Equal As Numbers    ${response.status_code}    200
    ${json}=    Set Variable    ${response.json()}
    Should Contain    ${json}    title    foo_partial_updated

Delete a Post
    ${headers}=    Create Dictionary    Content-Type=application/json
    ${response}=        DELETE    ${BASE_URL}/posts/1    headers=${headers}
    Should Be Equal As Numbers    ${response.status_code}    200
