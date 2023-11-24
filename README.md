# socratic-model-with-langchain-streamlit

초기 실행 시
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

langchain 사용을 위해 openai key 발급(Command page와 socratic model execute page)
```
openai_api_key = "your_openai_key"
```

메인 페이지 실행 명령어
```
streamlit run '.\Command page.py'
```