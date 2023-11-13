import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('DataFrame')
#表
df = pd.DataFrame({
  '1列目': [1, 2, 3, 4],
  '2列目': [10, 20, 30, 40]
})

st.dataframe(df.style.highlight_max(axis=0), width=300, height=300)
#マークダウン
"""
```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""
#グラフ
df1 = pd.DataFrame(np.random.rand(20, 3), columns=['a', 'b', 'c'])
st.line_chart(df1)

#マップ

df2 = pd.DataFrame(
  np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
  columns=['lat', 'lon']
)
st.map(df2)

#画像
st.write('Display Image')

if st.checkbox('Show Image'):
  img = Image.open('background-image.jpg')
  st.image(img, caption='back', use_column_width=True)

#セレクトボックス
option = st.selectbox(
  'あなたの好きな数字を教えてください',
  list(range(1, 11))
)
'あなたの好きな数字は、', option, 'です。'

#テキスト入力
st.write('Interactive widgets')

text = st.sidebar.text_input('あなたの趣味を教えて')
condition = st.sidebar.slider('あなたの調子は？', 0, 100, 50)

'あなたの趣味', text
'コンディション:', condition

#カラム
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
  right_column.write('ここは右カラム')

#expander
expander = st.expander('問い合わせ')
expander.write('解答')

#プログレスバー
st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'Done!!!!!'