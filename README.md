# Caddy CORS

Use a `caddy` docker container to proxify an API and configure CORS.

# Example
The example consists of two services, an API and a client.
The API responses the **path** and the **query string** of the URL used in the incoming **GET** requests.
The client makes a **GET** request to the API and renders the response in the web browser.

# Usage

To run the services it is only needed to execute
```sh
docker-compose up
```

To test the API just try in your browser [http://api-proxy.container.address/sample/path?q=uery&s=tring]().

To test the client, open [http://client-proxy.container.address]().

If you use [docker-hoster](https://github.com/dvddarias/docker-hoster), you can access the API through
[http://api.caddy-cors.com]() and the client through [http://client.caddy-cors.com]().


## Note

I defend personally the idea of solving this problem only once, on the web server.
The use of CORS extensions in web frameworks is only a temporary solution for development.
So, why not always use docker, even in development?
