import streamlit as st
import pandas as pd
from PIL import Image

from questions import data_facil, data_medio

df_facil = pd.DataFrame(data_facil)
df_medio = pd.DataFrame(data_medio)
df = pd.concat([df_facil, df_medio])

def load_image(image_path):
    with open(image_path, 'rb') as f:
        image = f.read()
    return image

def load_and_resize_image(image_path, size=(300, 300)):
    image = Image.open(image_path)
    image = image.resize(size)
    return image

def main():

    st.set_page_config(page_title="Jogo de Lógica", 
                       page_icon=":brain:", 
                       layout="wide")

    st.sidebar.markdown("# 🧠 Escape Room")

    if st.sidebar.button("Reiniciar Jogo"):
        reset_game()

    if st.sidebar.button("Documentação"):
        show_documentation()

    if 'init' not in st.session_state:
        reset_game()

    if st.session_state.init:
        show_welcome_screen()
    else:
        run_game_logic()

def show_documentation():
    st.title("Documentação")
    with open("docs.md", "r", encoding="utf-8") as file:
        docs_content = file.read()
    st.markdown(docs_content)

def reset_game():
    st.session_state.init = True
    st.session_state.score = 0
    st.session_state.current_phase = 1
    st.session_state.subfase = 0
    st.session_state.feedback = None
    st.session_state.advance_phase = False
    st.session_state.difficulty = "Fácil"

def show_welcome_screen():
    st.image("images/image.webp", width=200)

    st.title("Bem-vindo ao Jogo de Lógica!")
    st.write("""
        Instruções do jogo:
        - O jogo consiste em duas fases, cada uma com 5 perguntas.
        - Cada pergunta tem 4 opções, e apenas uma é correta.
        - Você deve acertar pelo menos 4 de 5 perguntas para avançar para a próxima fase.
        - Selecione o nível de dificuldade para começar.
    """)
    difficulty = st.selectbox("Escolha o nível de dificuldade:", ["Fácil", "Médio"])
    if st.button("Iniciar Jogo"):
        st.session_state.init = False
        st.session_state.difficulty = difficulty
        st.rerun()

def run_game_logic():
    questions = df[(df['Fase'] == str(st.session_state.current_phase)) & (df['Dificuldade'] == st.session_state.difficulty)]
    if st.session_state.subfase < len(questions):
        question = questions.iloc[st.session_state.subfase]
        display_question(question, len(questions))
    else:
        handle_phase_completion()

def display_question(question, total_questions):
    st.title(f"Fase {st.session_state.current_phase} - {st.session_state.difficulty}")
    
    # Layout em colunas para posicionar a imagem e a pergunta lado a lado
    col1, col2 = st.columns([1, 3])
    
    with col1:
        update_image()

    with col2:
        #st.markdown(f"**Pergunta:** {question['Pergunta']}")
        st.markdown(f"<h3 style='font-size:18px;'>{question['Pergunta']}</h3>", unsafe_allow_html=True)

        #st.markdown(f"<div class='big-font'>{question['Pergunta']}</div>", unsafe_allow_html=True)

        options = question['Respostas']
        answer = st.radio("Selecione a resposta correta:", options, key=f'question{st.session_state.subfase}')

        if st.button("Responder"):
            check_answer(question, answer)
            update_questions()

        if st.session_state.feedback:
            if st.session_state.feedback.startswith("Correto"):
                st.markdown(f'<p style="color:green;">{st.session_state.feedback}</p>', unsafe_allow_html=True)
            elif st.session_state.feedback.startswith("Incorreto"):
                st.markdown(f'<p style="color:red;">{st.session_state.feedback}</p>', unsafe_allow_html=True)

            st.session_state.feedback = None

    update_progress_bar(total_questions)

def update_image():
    image_path = f"images/img{st.session_state.current_phase}_{st.session_state.subfase + 1}.png"
    image = load_and_resize_image(image_path)
    st.image(image)

def update_questions():
    st.session_state.subfase += 1
    st.rerun()

def update_progress_bar(total_questions):
    progress = st.session_state.subfase / total_questions
    st.progress(progress)

    if st.session_state.subfase >= total_questions:
        st.write("### :trophy: Parabéns! Você completou a fase.")
        st.button("Próxima Fase", on_click=reset_game)

def check_answer(question, answer):
    correct_answer_index = question["Correta"]
    correct_answer = question["Respostas"][correct_answer_index]
    if answer == correct_answer:
        st.session_state.score += 1
        st.session_state.feedback = "Correto!"
    else:
        st.session_state.feedback = f"Incorreto! A resposta correta era: {correct_answer}"

def reset_phase():
    st.session_state.score = 0
    st.session_state.subfase = 0
    st.session_state.feedback = None
    st.rerun()

def advance_phase():
    st.session_state.current_phase += 1
    st.session_state.subfase = 0
    st.session_state.score = 0
    st.session_state.advance_phase = False
    st.session_state.feedback = None
    st.rerun()

def handle_phase_completion():
    if st.session_state.score >= 4:
        if st.session_state.current_phase == 2:
            st.balloons()
            st.success("Parabéns! Você completou o jogo!")
            if st.button("Voltar ao início"):
                reset_game()
                st.rerun()
        else:
            st.session_state.advance_phase = True
            st.write(f"### :trophy: Parabéns! Você completou a Fase {st.session_state.current_phase}")
            st.write(f"Você Acertou {st.session_state.score} de 5 perguntas corretas.")
            st.info("Clique em 'Avançar' para a próxima fase.")
            if st.button("Avançar para a Próxima Fase"):
                advance_phase()
    else:
        st.error("Você não conseguiu avançar para a próxima fase. Tente novamente!")
        if st.button("Tentar novamente"):
            reset_phase()

if __name__ == "__main__":
    main()
