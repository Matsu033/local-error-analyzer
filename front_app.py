# front_app.py
import streamlit as st  # ブラウザ画面を作るためのツールを読み込み
from fix_the_error import perform_analysis  # 自作したファイルを読み込む

"""実行コマンド"""
# python -m streamlit run "C:\エラー改善プログラム\local-error-analyzer\front_app.py"

st.set_page_config(page_title="プログラミング学習支援AI", layout="wide")
st.title("🎓 初学者・中級者向け プログラミング学習コーチ")

# Ctrl+C によるStreamlitのキャッシュクリア挙動を強制停止するJavaScript(エラーメッセージを出さないようにする)
st.components.v1.html(
    """
    <script>
    window.addEventListener('keydown', function(e) {
        if ((e.ctrlKey || e.metaKey) && e.key === 'c') {
            // Streamlitの親要素にイベントが伝わるのを阻止する
            e.stopPropagation();
        }
    }, true);
    </script>
    """,
    height=0,  # 画面を汚さないように高さはゼロ
)

# 画面の設定
source_code_screen, error_code_screen = st.columns(2)
with source_code_screen:
    language = st.selectbox("使用する言語を選択してください", ["Python", "JavaScript", "C++", "Java", "Go", "HTML/CSS"])
    source_code = st.text_area("ソースコード", height=300)
    
    # 【新機能】学習モードの選択
    learning_mode = st.radio(
        "学習モードを選択してください",
        ["プログラミング学習（ヒントのみで自分で考える）", "通常デバッグ（修正コードも確認する）"],
        horizontal=True
    )

with error_code_screen:
    #n エラーメッセージの入力欄
    error_message = st.text_area("エラーメッセージ、または「意図しない挙動・実行結果」", height=300)

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