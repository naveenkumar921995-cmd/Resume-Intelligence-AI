
st.sidebar.image(
    "https://img.icons8.com/color/96/artificial-intelligence.png",
    width=90
)

st.sidebar.title(APP_NAME)

st.sidebar.caption(APP_VERSION)

menu = st.sidebar.radio(

    "Navigation",

    SIDEBAR_MENU

)

st.sidebar.divider()

st.sidebar.success("Enterprise Edition")

st.sidebar.caption(FOOTER)
