<h1>Lambda Layers</h1>

Prerequesite: Docker-Desktop

This package explains how to create a lambda layer dynamically.
This package is not a standalone stack. If you want to create a NestedStack you need to change the creation of the class to a NestedStack.
Also you have to delete the `stack` parameter.

<hr>

***How to use:***
1. Set the name/id of the layer in 
```py
class Layers:
    TEST_LAYER_1 = 'TEST_LAYER_1'
    TEST_LAYER_2 = 'TEST_LAYER_2'
``` 
2. Call the ```define_layer``` function for every layer you want to create. Set the parameter `path` to the local directory of the layer. Inside should be a `requirements.txt` with all the needed packages + versions.
You can also add self programmed file to the directory (see Layer1). The parameter `dest_folder` is optional. If you don't set it you can import the libraries directly in the lambda (e.g. `import test_layer`).
If you set the parameter to e.g. `layer1` you need to import the files from these folder: `from layer1 import test_layer`.
```py
class LambdaLayers:
    def __init__(self, stack, stack_params: dict):
        self._test_layer_1 = self.define_layer(stack, Layers.TEST_LAYER_1, 'LambdaLayer/Layer1', 'hertha_commons')
        self._test_layer_2 = self.define_layer(stack, Layers.TEST_LAYER_2, 'LambdaLayer/Layer2')
```
3. With the `propertys` decorater you can access the layers in other functions and attach them to any lambda.
```py
@property
def layer_1(self):
    return self._test_layer_1

@property
def layer_2(self):
    return self._test_layer_2
```