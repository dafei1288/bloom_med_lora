---
license: Apache License 2.0

tasks:
- text-generation

model-type:
- gpt

frameworks:
- pytorch

backbone:
- transformer

language:
- zh

tags:
- bloom
- Huatuo

---


# Jimmy_Med
基模型进行了指令微调，提高了基模型在医疗领域的问答效果。

#On modelscope.cn
`dafei1288/Jimmy_Med`

# 底模
基于 `Langboat/bloom-800m-zh` 基础模型进行微调

# 数据集

基于 `本草[原名：华驼(HuaTuo)]` 的训练数据集

# A quick start 

`pip install -r requirements.txt`


## 代码示例
```python
from transformers import pipeline,AutoTokenizer,AutoModelForCausalLM
from transformers import pipeline
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
text_generation_zh = pipeline(Tasks.text_generation, model='dafei1288/Jimmy_Med')
result_zh = text_generation_zh("关节部位红肿疼痛，排尿困难,怎么办？")
print(result_zh['text'])

```


## 项目参与者

本项目由 [Jack 'dafei1288' Lee](https://github.com/dafei1288)

  

## 致谢

  

本项目参考了以下开源项目，在此对相关项目和研究开发人员表示感谢。

- 本草: https://github.com/SCIR-HI/Huatuo-Llama-Med-Chinese
- Bloom: https://huggingface.co/Langboat/bloom-800m-zh

  

## 免责声明

本项目相关资源仅供学术研究之用，严禁用于商业用途。使用涉及第三方代码的部分时，请严格遵循相应的开源协议。模型生成的内容受模型计算、随机性和量化精度损失等因素影响，本项目无法对其准确性作出保证。本项目数据集绝大部分由模型生成，即使符合某些医学事实，也不能被用作实际医学诊断的依据。对于模型输出的任何内容，本项目不承担任何法律责任，亦不对因使用相关资源和输出结果而可能产生的任何损失承担责任。


## Citation

如果您使用了本项目的数据或者代码，或是我们的工作对您有所帮助，请声明引用


首版技术报告: [Huatuo: Tuning llama model with chinese medical knowledge](https://arxiv.org/pdf/2304.06975)

```
@misc{wang2023huatuo,
    title={HuaTuo: Tuning LLaMA Model with Chinese Medical Knowledge},
    author={Haochun Wang and Chi Liu and Nuwa Xi and Zewen Qiang and Sendong Zhao and Bing Qin and Ting Liu},
    year={2023},
    eprint={2304.06975},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```

知识微调：[Knowledge-tuning Large Language Models with Structured Medical Knowledge Bases for Reliable Response Generation in Chinese
](https://arxiv.org/pdf/2309.04175.pdf)

```
@misc{wang2023knowledgetuning,
      title={Knowledge-tuning Large Language Models with Structured Medical Knowledge Bases for Reliable Response Generation in Chinese}, 
      author={Haochun Wang and Sendong Zhao and Zewen Qiang and Zijian Li and Nuwa Xi and Yanrui Du and MuZhen Cai and Haoqiang Guo and Yuhan Chen and Haoming Xu and Bing Qin and Ting Liu},
      year={2023},
      eprint={2309.04175},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

医学文献知识获取：[The CALLA Dataset: Probing LLMs’ Interactive Knowledge Acquisition from Chinese Medical Literature](https://arxiv.org/pdf/2309.04198.pdf)

```
@misc{du2023calla,
      title={The CALLA Dataset: Probing LLMs' Interactive Knowledge Acquisition from Chinese Medical Literature}, 
      author={Yanrui Du and Sendong Zhao and Muzhen Cai and Jianyu Chen and Haochun Wang and Yuhan Chen and Haoqiang Guo and Bing Qin},
      year={2023},
      eprint={2309.04198},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```

