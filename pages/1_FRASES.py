import streamlit as st
import funcoes as fn
from datetime import datetime

st.title("Exercicio 1")
st.write("Esse programa gera frases aleatóris e conta quanas vogais e consoanes ela possui")

quanidade=st.number_input("Quantas frases deseja gerar?", min_value=1, step=1)
substantivo=st.text_input("Digite um subantivo para buscar")

if st.button("Gerar Frases"):
    frases= fn.array_frases(quanidade)

    