## Object Detection Using Transformers:

- I've used meta's detr-resnet-101 model to perform object detection.
- The model is availble for use at:
- https://huggingface.co/facebook/detr-resnet-101
_ I've buiid a simple Flask web app to deploy it.
- Once deployed the app can be accessed using a POST request.
- API testing has been done by me on Postman.


#### Usage:
- The app can be accessed through POST requests with a form-data body.
- It outputs intra image object location, match confidence percentage and
a object label in the form of a JSON.


#### Input
[!image](https://drive.google.com/uc?export=view&id=1tFn_cYNQvQDSNR0GETloTtna5XBCzCFw)



#### Output
[!image](https://drive.google.com/uc?export=view&id=1fAB3GqVGo7ySkN_VLOWpsuy89GIq4G-y)

[!image](https://drive.google.com/uc?export=view&id=1nhMpS_BMvrApNpizXiLvszwJbAUjgKjW)

[!image](https://drive.google.com/uc?export=view&id=1LErNfCelHJXHBYKK9OIeS3N7nBnKHlRV)