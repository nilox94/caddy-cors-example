# Caddy CORS

Use a `caddy` docker container to proxify an API and configure CORS.

# Example
The example consists of two services, an API and a client.
The API responses the **path** and the **query string** of the URL used in the incoming **GET** requests.
The client makes a **GET** request to the API and renders the response in the web browser.

# Usage

To run the services you only need to execute
```
docker-compose up
```
To test the API just open [this](http://api-proxy.container.address/sample/path?q=uery&s=tring) in your browser, and [this](http://client-proxy.container.address) to test the client.

If you use [docker-hoster](https://github.com/nilox94/traefik-hoster), you can access the [API](http://api.caddy-cors.com) and the [client](http://client.caddy-cors.com) through their aliases in the Docker network.

## Note

I defend the idea of solving this problem only once, from the beginning on the webserver.
The use of CORS extensions in web frameworks is only a temporary solution for development.
So why not always use docker, even in development?
