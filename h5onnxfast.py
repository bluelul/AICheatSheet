#########################################
#             H5 ONNX FAST              #
# Convert H5 model to ONNX model        #
# with nchw/nhwc & batch1/batchN option #
#         Author: bluelul.com           #
#           Date: 14/04/2023            #
#########################################

import tensorflow as tf
from tensorflow import keras

import tf2onnx
import onnx
from onnxruntime.tools.onnx_model_utils import make_dim_param_fixed, fix_output_shapes

import argparse

####################### CONFIG
parser = argparse.ArgumentParser(description='Convert model h5 to onnx')
parser.add_argument('model_file', help='path of h5 model file', type=str)
parser.add_argument("--nhwc", help="export NHWC input format (instead of default NCHW)", action="store_true")
parser.add_argument("--nchw", help="export NCHW input format (default)", action="store_true")
parser.add_argument("--batchN", help="dynamic batch size (instead of default fixed batch size = 1)", action="store_true")
parser.add_argument("--batch1", help="convert batch size to 1 (default)", action="store_true")
parser.add_argument('--opset', default=13, help='opset of onnx file', type=int)
args = parser.parse_args()

if (args.nhwc == args.nchw):
	args.nchw = True
	args.nhwc = False
if (args.batch1 == args.batchN):
	args.batch1 = True
	args.batchN = False

model_file = args.model_file
is_NCHW = args.nchw
is_batch1 = args.batch1
opset = args.opset

####################### LOAD MODEL
model = keras.models.load_model(model_file)
model_name = model_file[:-3]

####################### PREPARE METADATA
config = model.get_config()
input_config = config["layers"][0]["config"]

spec = (tf.TensorSpec(input_config['batch_input_shape'], tf.float32, name=input_config['name']),)
output_path = model.name + "_batchN.onnx"

inputs_as_nchw = None
if (is_NCHW): inputs_as_nchw=[input_config['name']+':0']

####################### CONVERT TO ONNX
model_proto, _ = tf2onnx.convert.from_keras(model, input_signature=spec, 
						opset=opset, output_path=output_path, inputs_as_nchw=inputs_as_nchw)

####################### MODIFY BATCH SIZE
if (is_batch1):
	onnx_batch_name = model_proto.graph.input[0].type.tensor_type.shape.dim[0].dim_param

	model_onnx = onnx.load(output_path)

	make_dim_param_fixed(model_onnx.graph, onnx_batch_name, 1)

	fix_output_shapes(model_onnx) # update the output shapes to make them fixed if possible.

	onnx.save(model_onnx, model.name + '_batch1.onnx')

