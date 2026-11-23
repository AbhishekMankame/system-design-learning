## HTTP responses status codes

HTTP response status codes indicate whether a specific HTTP request has been successfully completed. Responses are grouped in five classes

1. Informational responses(100 - 199)
2. Successful responses(200 - 299)
3. Redirection messages(300 - 399)
4. Client error responses(400 - 499)
5. Server error responses(500 - 599)

Note: If you receive a response that is not listed here, it is a non-standart response, possibly custom to the server's software.

### Inforational responses
- 100 - Continue --> The interim response indicates that the client should continue the request or ignore the response if the request is already finished.
- 101 - Switching Protocols --> This code is sent in response to an `Upgrade` request header from the client and indicates the protocol the server is switching to.
- 102 - Processing --> This code was used in `Web Distributed Authoring (WebDAV) constexts to indicate that a request had been received by the server, but no status was available at the time of response. The response code has been depreceated and it is no longer used.
- 103 - Early Hints --> This status code is primarily intended to be used with the `Link` header, letting the user agent start `overloading` resources while the server prepares a response or `preconnect` to an origin from which the page will need resources.

### Successful responses
- 200 - OK --> The request succedded. The result and meaning of "success" depends on the HTTP method:
    - GET: The resource has been fetched and transmitted in the message body.
    - HEAD: Representation headers are included in the response without any message body.
    - PUT or POST: The resource describing the result of the action is transmitted in the message body.
    - TRACE: The message body contains the request as received by the server.

- 201 - Created --> The request succeeded, and a new resource was created as a result. This is typically the response sent after `POST` requests, or some `PUT` requests.

- 202 - Accepted --> The request has been received but not yet acted upon. It is noncommittal, since there is no way in HTTP to later send an asynchronous response indicating the outcome of the request. It is intended for cases where another process or server handles the request, or for batch processing.

- 203 - Non-Authoritative Information --> This response code means the returned metadata is not exactly the same as is available from the origin server, but it is collected from a local or third-party copy. This is mostly used for mirrors or backups of another resource. Except for that specific case, the `200 OK` response preferred to this status.

- 204 - No Content --> There is no content to send for this request, but the headers are useful. The user agent may update its cached headers for this resource with the new ones.

- 205 - Reset Content --> Tells the user agent to reset the document which sent this request.

- 206 - Partial Content --> This response code is used in response to a range request when the client has requested a part or parts of a resource.

### Client error response
- 400 - Bad request --> The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing).

- 401 - Unauthorized --> Although the HTTP standard specifies "unauthorized", semantically this response means "unauthenticated". That is, the client must authenticate itself to get the requested response.

- 402 - Payment Required --> The initial purpose of this code was for digital payment systems, however this status code is rarely used and no standard convention exists.

- 403 - Forbidden --> The client does not have access rights to the content; that is, it is unauthorized, so the server is refusing to give the requested resource. Unlike, `401 Unauthorized`, the client's identity is konwn to the server.

- 404 - Not Found --> The server cannot find the requested resource. In the browser, this means the URL is not recognized. In an API, this can also mean that the endpoint is valid but the resource itself does not exist. Servers may also send this response instead of `403 Forbidden` to hide the existence of a resource from an unauthorized client. This response code is probably the most well known due to its frequent occurrence on the web.

- 405 - Method Not Allowed --> The request method is known by the server but is not supported by the target resource. For example, an API may not allow `DELETE`on a resource, or the `TRACE` method entirely.

- 406 - Not Acceptable --> This response is sent when the web server, after performing server-driven content negotiation, doesn't find any content that conforms to the criteria given by the user agent.

- 408 - Request Timeout --> This response is sent on an idel connection by some servers, even without any previous request by the client. It means that the server would like to shut down this unused connection. This response is used much more since some browsers use HTTP pre-connection mechanism to speed up browsing. Some servers may shut down a connection without sending this message.

- 429 - Too Many Requests --> The user has sent too many requests in a given amount of time (rate limiting).

### Server error response
- 500 - Internal Server Error --> The server has encountered a situation it does not know how to handle. This error is generic, indicating that the server cannot find a more appropriate `5XX` response code to respond with.

- 501 - Not Implemented --> The request method is not supported by the server and cannot be handled. The only methods that servers are required to support (and therefore must not return this code) are `GET` and `POST`.

- 502 - Bad Gateway --> This error response means that the server, while working as a gateway to get a response needed to handle the request, got an invalid response.

- 503 - Service Unavailable --> The server is not ready to handle the request. Common causes are a server that is down for maintenance or this is overloaded. Note that together with this response, a user-friendly page explaining the problem should be sent. This response should be used for temporary conditions and the `Retry-After` HTTP header should, if possible, contain the estimated time before the recovery of the service. The webmaster must also take care about the caching-related headers that are sent along with this response, as these temporary condition responses should usually not cached.

- 504 - Gateway Timeout --> This error response is given when the server is acting as a gateway and cannot get a response in time.

- 505 - HTTP Version Not Supported --> The HTTP version used in the request is not supported by the server.