import aws_cdk.aws_lambda as lfunction
from aws_cdk import core as cdk


class Layers:
    TEST_LAYER_1 = 'TEST_LAYER_1'
    TEST_LAYER_2 = 'TEST_LAYER_2'


class LambdaLayers:
    def __init__(self, stack, stack_params: dict):
        self._test_layer_1 = self.define_layer(stack, Layers.TEST_LAYER_1, 'LambdaLayer/Layer1', 'hertha_commons')
        self._test_layer_2 = self.define_layer(stack, Layers.TEST_LAYER_2, 'LambdaLayer/Layer2')

    def define_layer(self, stack, layer_id: str, path: str, dest_folder: str = None):
        command_without_dest_folder = 'pip install -r requirements.txt -t /asset-output/python && cp -au * /asset-output/python'
        command_with_dest_folder = 'pip install -r requirements.txt -t /asset-output/python && mkdir /asset-output/python/{dest_folder} && cp -au * /asset-output/python/{dest_folder}'.format(
            dest_folder=dest_folder)
        command = command_without_dest_folder if dest_folder == None else command_with_dest_folder

        return lfunction.LayerVersion(
            stack,
            id=layer_id,
            compatible_runtimes=[lfunction.Runtime.PYTHON_3_9],
            code=lfunction.Code.from_asset(
                path=path,
                bundling=cdk.BundlingOptions(
                    image=lfunction.Runtime.PYTHON_3_9.bundling_image,
                    command=[
                        'bash', '-c',
                        command
                    ]
                )))

    @property
    def layer_1(self):
        return self._test_layer_1

    @property
    def layer_2(self):
        return self._test_layer_2
