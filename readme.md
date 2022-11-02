<div align="center" id="top"> 
  <alt="Text Tagging - Hateful Comments Detection" />

  &#xa0;

  <!-- <a href="https://audioapp.netlify.app">Demo</a> -->
</div>

<h1 align="center">Text Tagging - Hateful Comments Detection</h1>

<p align="center">
  <img alt="Github top language" src="https://img.shields.io/github/languages/top/human-ai2025/Text-Tagging?color=56BEB8">

  <img alt="Github language count" src="https://img.shields.io/github/languages/count/human-ai2025/Text-Tagging?color=56BEB8">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/human-ai2025/Text-Tagging?color=56BEB8">

  <img alt="License" src="https://img.shields.io/github/license/human-ai2025/Text-Tagging?color=56BEB8">


</p>

<!-- Status -->

<!-- <h4 align="center"> 
	🚧  Speech Recognition System 🚀 Under construction...  🚧
</h4> 

<hr> -->

<p align="center">
  <a href="#dart-about">About</a> &#xa0; | &#xa0; 
  <a href="#rocket-technologies">Technologies</a> &#xa0; | &#xa0;
  <a href="#white_check_mark-requirements">Requirements</a> &#xa0; | &#xa0;
  <a href="#checkered_flag-starting">Starting</a> &#xa0; | &#xa0;
  <a href="#memo-license">License</a> &#xa0; | &#xa0;
  <a href="https://github.com/human-ai2025" target="_blank">Author</a>
</p>

<br>

## :dart: About ##
Deployed a model mimicing cloud production server using Docker, Pytorch, HuggingFace, Git and FastAPI. Reduced the model size by quantization and inference time by singleton design pattern approach. 

## :rocket: Technologies ##

The following tools were used in this project:

- [Docker](https://www.docker.com/)
- [Python](https://www.python.org/)
- [Git](https://git-scm.com)
- [FastAPI]()
- [Torch]()
- [Hugging Face]()


## :white_check_mark: Requirements ##

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com), [Docker](https://www.docker.com/) and [Python](https://www.python.org/) installed. 

## :checkered_flag: Starting ##

```bash
# Clone this project
$ git clone https://github.com/human-ai2025/Text-Tagging

# Access
$ cd Text-Tagging


# After doing this, it will give you the model weights [make sure to use the same versions of tensorflow in docker and while buiding the model]

# For docker 
$ docker compose build -- up

# This will fire up the web serice for making predictions.
# The server will initialize in the "http://localhost:8000/predict"
```

## :memo: License ##

This project is under license from MIT. For more details, see the [LICENSE](LICENSE) file.


Made with :heart: by <a href="https://github.com/human-ai2025" target="_blank">Tarini Tanaya Mohapatra</a>


&#xa0;

<a href="#top">Back to top</a>
