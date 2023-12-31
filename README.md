# socratic-model-with-langchain-streamlit

기존 **socratic model에 langchain과 streamlit**을 적용

사용자가 **한국어로 입력**을 하게 되면 **langchain을 통해 번역**이 되고 **agent의 tool끼리 서로 상호작용** 후 socratic model을 실행

**사용자의 편리함**을 위해 streamlit을 사용


## 초기 실행 시

``` python
pip install ftfy regex tqdm fvcore imageio==2.4.1 imageio-ffmpeg==0.4.5
pip install git+https://github.com/openai/CLIP.git
pip install -U --no-cache-dir gdown --pre
pip install pybullet moviepy
pip install flax
pip install openai
pip install easydict
pip install torch==1.13.0+cu117 torchvision==0.14.0+cu117 torchaudio==0.13.0 --extra-index-url https://download.pytorch.org/whl/cu117
pip install tensorflow
pip install IPython
pip install matplotlib
pip install gsutil
pip install typing-extensions --upgrade
```

## langchain 사용을 위해 openai key 발급(Command page와 socratic model execute page)
```
openai_api_key = "your_openai_key"
```

## 메인 페이지 실행 명령어
```
streamlit run '.\Command page.py'
```

## 결과물

<p align="center">

  
  #### 명령어 페이지
  <img src="./images/Command page.PNG">
  
  -------------------------------------

  #### 실행 페이지
  <img src="./images/execute page.PNG">
  
  -------------------------------------

  #### 첫 번째 단계
  <img src="./images/1 step execute.PNG">
  
  -------------------------------------

  #### 두 번째 단계
  <img src="./images/2 step execute.PNG">
  
  -------------------------------------

  #### 에러 단계(고의로 발생시킴)
  <img src="./images/error step execute.PNG">
  
  -------------------------------------

  #### 네 번째 단계
  <img src="./images/4 step execute.PNG">
  
  -------------------------------------
  
  #### 다섯 번째 단계
  <img src="./images/5 step execute.PNG">
  
  -------------------------------------

  #### 여섯 번째 단계
  <img src="./images/6 step execute.PNG">
  
  -------------------------------------
  
</p>
