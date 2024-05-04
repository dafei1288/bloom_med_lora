# import torch
# from transformers import Conv1D, AutoModelForCausalLM
#
#
# def get_specific_layer_names(model):
#     # Create a list to store the layer names
#     layer_names = []
#
#     # Recursively visit all modules and submodules
#     for name, module in model.named_modules():
#         # Check if the module is an instance of the specified layers
#         if isinstance(module, (torch.nn.Linear, torch.nn.Embedding, torch.nn.Conv2d, Conv1D)):
#             # model name parsing
#
#             layer_names.append('.'.join(name.split('.')[4:]).split('.')[0])
#
#     return layer_names
#
# model = AutoModelForCausalLM.from_pretrained("model/bloom-800m-zh",
#                                              low_cpu_mem_usage=True,
#                                              torch_dtype=torch.half,
#                                              device_map="cuda")
# print(list(set(get_specific_layer_names(model))))



from modelscope import Model
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
model = Model.from_pretrained('bloomoutput/bloom-800m-zh-merged-med')
text_generation_zh = pipeline(Tasks.text_generation, model=model)
result_zh = text_generation_zh("关节部位红肿疼痛，排尿困难,怎么办？")
print(result_zh)