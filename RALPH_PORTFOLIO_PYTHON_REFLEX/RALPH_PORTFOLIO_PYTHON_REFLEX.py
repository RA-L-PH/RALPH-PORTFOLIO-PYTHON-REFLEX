"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.container(
            rx.flex(
                rx.container(
                    rx.text(
                        "Ralph Carvalho",
                        align="left",
                        size="8",
                        ),
                    height="100%",
                    width="50%",
                    ),
                rx.container(
                    rx.flex(
                        rx.link(
                            rx.button(
                                rx.icon(tag="github"),
                                color_scheme="mint",
                            ),
                            href="https://github.com/RA-L-PH",
                        ),
                        rx.link(
                            rx.button(
                                rx.icon(tag="linkedin"),
                                color_scheme="mint",
                            ),
                            href="https://www.linkedin.com/in/ralph-carvalho-614b78257/",
                        ),
                        rx.link(
                            rx.button(
                                rx.icon(tag="mail"),
                                color_scheme="mint",
                            ),
                            href="mailto:ralphaacarvalho@gmail.com",
                        ),
                        spacing="3",
                        justify="end"
                    ),
                    align="right",                 
                ),
                
                align="center",
                spacing="4"
            ),
            height="10%",
            width="100%",
        ),
        rx.divider(),
        rx.container(
            rx.flex(
                rx.box(
                    rx.text("""Hi, I’m Ralph Carvalho, a coder and Arduino enthusiast. I love traveling and exploring new cultures. I’m known for my innovative problem-solving, teamwork, and leadership. Whether I’m coding, leading, or traveling, I’m always ready for a new adventure.""", size="5",),
                    background_color="white",
                    radius="20px",
                    width="50%",
                    padding="25px",
                ),
                rx.box(
                    rx.center(
                        rx.image(
                            src="https://issb.sfit.ac.in/ppl/Copy%20of%20Ralph_Carvalho__Webmaster.jpg",
                            width="100%",
                            height="100%",
                            margin="10px",
                            border_radius="50%",
                            border="5px solid black",
                        ),
                    ),
                    background_color="white",
                    radius="20px",
                    width="50%",
                    padding="25px",
                ),
                justify="between",
                spacing="2",
                align="center",
            ),
        ),
        rx.divider(),
        rx.center(
            rx.container(
                rx.text("My Expertise",size="7",align="center"),
                width="100%",
                border_radius="5px",
                border="1px solid black",
                margin="15px",
            ),
        ),
        rx.container(
            rx.center(
                rx.flex(
                    rx.container(
                        rx.image(
                            src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/HTML5_logo_and_wordmark.svg/512px-HTML5_logo_and_wordmark.svg.png",
                            width="300px",
                            height="300px",
                            margin="10px",
                            border_radius="50%",
                            border="5px solid black",
                        ),
                        rx.text("HTML 5", align="center", size="4"),
                        height="300px",
                        width="300px",
                        margin="5%",
                    ),
                    rx.container(
                        rx.image(
                            src="https://upload.wikimedia.org/wikipedia/commons/6/62/CSS3_logo.svg",
                            width="300px",
                            height="300px",
                            margin="10px",
                            border_radius="50%",
                            border="5px solid black",
                        ),
                        rx.text("CSS 3", align="center", size="4"),
                        height="300px",
                        width="300px",
                        margin="5%",
                    ),
                    rx.container(
                        rx.image(
                            src="https://upload.wikimedia.org/wikipedia/commons/6/6a/JavaScript-logo.png",
                            width="300px",
                            height="300px",
                            margin="10px",
                            border_radius="50%",
                            border="5px solid black",
                        ),
                        rx.text("Java Script", align="center", size="4"),
                        height="300px",
                        width="300px",
                        margin="5%",
                    ),
                    rx.container(
                        rx.image(
                            src="https://avatars.githubusercontent.com/u/104714959?v=4",
                            width="300px",
                            height="300px",
                            margin="10px",
                            border_radius="50%",
                            border="5px solid black",
                        ),
                        rx.text("Reflex", align="center", size="4"),
                        height="300px",
                        width="300px",
                        margin="5%",
                    ),
                    rx.container(
                        rx.image(
                            src="https://5.imimg.com/data5/HT/HX/YO/GLADMIN-13634783/selection-208-500x500.png",
                            width="300px",
                            height="300px",
                            margin="10px",
                            border_radius="50%",
                            border="5px solid black",
                        ),
                        rx.text("Flask", align="center", size="4"),
                        height="300px",
                        width="300px",
                        margin="5%",
                    ),
                    rx.container(
                        rx.image(
                            src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png",
                            width="300px",
                            height="300px",
                            margin="10px",
                            border_radius="50%",
                            border="5px solid black",
                        ),
                        rx.text("Python", align="center", size="4"),
                        height="300px",
                        width="300px",
                        margin="5%",
                    ),
                    wrap="wrap",
                    justify="between",
                    align="center",
                    direction="row",
                )
            ),
            height="auto",
            width="100%",
            margin="10px",
        ),
        rx.divider(),
        rx.center(
            rx.container(
                rx.text("My Projects",size="7",align="center"),
                width="100%",
                border_radius="5px",
                border="1px solid black",
                margin="15px",
            ),
        ),
        rx.container(            
            rx.card(
                rx.card(
                    rx.video(
                        url="https://drive.google.com/file/d/14sdiZSuTIaHdRh2cinzlSoYBOrqCsfO1/view?usp=sharing",
                        width="100%",
                        height="auto",
                    ),
                    width="100%",
                    padding="5px",
                ),
                rx.heading("Euphoria Sportz"),
                rx.link("View Website",
                        href="https://euphoriasportz.github.io/euphoriasportz/",    
                ),
                width="100%",
                height="auto",
                margin="10px",                                    
            ),
            rx.card(
                rx.card(
                    rx.video(
                        url="https://drive.google.com/file/d/14vgc1H6VrwF-xwp-FtUxPK0GJ74tYKKz/view?usp=sharing",
                        width="100%",
                        height="auto",
                    ),
                    width="100%",
                    padding="5px",
                ),
                rx.heading("IEEE WIE SFIT"),
                rx.link("View Website",
                        href="https://issb.sfit.ac.in/wie/index.html",    
                ),
                width="100%",
                height="auto",
                margin="10px",                                    
                
            ),
            width="100%",
            height="auto",
        ),
        rx.divider(),
        rx.center(
            rx.container(
                rx.text("Other Social Links",size="7",align="center"),
                width="100%",
                border_radius="5px",
                border="1px solid black",
                margin="15px",
            ),
        ),
        rx.center(
            rx.container(
                rx.flex(
                    rx.link(
                        rx.button(
                            rx.icon(tag="instagram"),
                            color_scheme="pink",
                        ),
                        href="https://www.instagram.com/ralph.carvalho.09/",
                    ),
                    wrap="wrap",
                    justify="center",
                    align="center",
                    direction="row",
                ),       
                width="100%",
                border_radius="5px",
                border="1px solid black",
                margin="15px",        
            ),
        ),
        rx.text("This Portfolio was solely made using Python Reflex",size="5",align="center"),
    )

app = rx.App()
app.add_page(index)