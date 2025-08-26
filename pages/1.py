import streamlit as st

st.title('답을 고르시오.')

# 문제 입력
question = st.image("https://lwdw.ebsi.co.kr/UpDown/item_xip/resource/paper/24517780/21104804_000_20241115132717.png", caption="2025학년도 11월 대학수학능력시험 수학 공통 11번")
answer = st.selectbox('답:',[
  '① 120', '② 125', '③ 130', '④ 135', '⑤ 140'
])

# 답안지
answer_data = {
  '① 120': {
    '설명':'정답입니다.'
  },
  '② 125': {
    '설명':'11%가 선택한 오답입니다.'
          '다시 선택해 주십시오.'
  },
  '③ 130': {
    '설명':'14.3%가 선택한 오답입니다.'
          '다시 선택해 주십시오.'
  },
  '④ 135': {
    '설명':'10.2%가 선택한 오답입니다.'
          '다시 선택해 주십시오.'
  },
  '⑤ 140': {
    '설명':'5.2%가 선택한 오답입니다.'
          '다시 선택해 주십시오.'
  },
}

if st.button('정답 확인하기'):
  if answer in answer_data:
    설명 = answer_data[answer]['설명']
    st.write(f"설명: {설명}")
