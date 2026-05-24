# front_app.py
import streamlit as st#ブラウザ画面を作るためのツールを読み込み
from fix_the_error import perform_analysis # 自作したファイルを読み込む

st.set_page_config(page_title="エラー解析AI", layout="wide")
st.title("💻 ローカルエラー解析ツール")

#画面の設定
source_code_screen, error_code_screen = st.columns(2)
with source_code_screen:
    language = st.selectbox("使用する言語を選択してください", ["Python", "JavaScript", "C++", "Java", "Go", "HTML/CSS"])
    source_code = st.text_area("ソースコード", height=300)
with error_code_screen:
    error_message = st.text_area("エラーメッセージ", height=300)

if st.button("解析実行"):
    if source_code and error_message:
        with st.spinner("AIが解析中..."):
            try:
                # 外部ファイルの中にある関数を実行
                result = perform_analysis(source_code, error_message,language)

                # 結果を画面に表示
                st.subheader("解析結果")
                st.markdown(result)
            except Exception as e:
                st.error(f"解析中にエラーが発生しました: {e}")