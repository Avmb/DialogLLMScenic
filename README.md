# DialogLLMScenic

Code for the paper [Dialogue-based generation of self-driving simulation scenarios using Large Language Models](https://arxiv.org/abs/2310.17372)

# Instructions

* Install Scenic from the repository
* Install numpy openai backoff tiktoken langchain from pip 
* Run scenario_generation/notebook_generate_multistep_with_sim_eval.ipynb

# License

BSD 3-Clause (see LICENSE).
Note: this repository contains data created from processing the examples in the [Scenic repository](https://github.com/BerkeleyLearnVerify/Scenic), the Scenic authors retain all the rights to this data.
The data augmentations in scenario_generation/curated_50_50_split_augmented/ have been created with the OpenAI GPT-3 model (text-davinci-003) and they are therefore subject to the [OpenAI Terms and policies](https://openai.com/policies). These augmentations are not necessary to run the experiments.

# Cite as

```
@misc{micelibarone2023dialoguebased,
      title={Dialogue-based generation of self-driving simulation scenarios using Large Language Models}, 
      author={Antonio Valerio Miceli-Barone and Alex Lascarides and Craig Innes},
      year={2023},
      eprint={2310.17372},
      archivePrefix={arXiv},
      primaryClass={cs.AI}
}
```
