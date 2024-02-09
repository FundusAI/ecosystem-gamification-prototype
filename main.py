import flet as ft

# Function to validate numeric input
def is_numeric(string):
    return all(char.isdigit() for char in string)

# Main application function
def main(page: ft.Page):
    # Set up progress bar and initial value
    progress_bar = ft.ProgressBar(value=0)
    completed_steps = 0

    # Initial page setup
    current_index = 0

    # Define navigation arrows
    left_arrow = ft.IconButton(icon="chevron_left", on_click=lambda: navigate(-1))
    right_arrow = ft.IconButton(icon="chevron_right", on_click=lambda: navigate(1))

    # Navigation function
    def navigate(direction):
        global completed_steps
        new_index = max(0, min(2, current_index + direction))
        if new_index != current_index:
            page.controls.clear()
            page.controls.append(question_boxes[new_index])
            current_index = new_index
            progress_bar.value = completed_steps
            update_arrows()


    # Function to update arrow visibility
    def update_arrows():
        left_arrow.visible = current_index > 0
        right_arrow.visible = current_index < 2


    # Define input fields and labels
    questions = [
        # TODO: Input Filtering
        ("Number of Steps Taken Today:", ft.TextField()),
        ("Blood Sugar:", ft.TextField()),
        ("Number of Medications Taken:", ft.TextField()),
    ]

    # Function to handle form submission
    def submit_form():
        global completed_steps
        points = completed_steps
        page.controls.clear()
        page.controls.append(
            ft.Column(
                [
                    ft.Text(
                        f"CONGRATULATIONS, You Have Received {points} Points!",
                        size=30,
                        weight="bold",
                    ),
                    ft.Text(
                        "Click here to go back to the dashboard.",
                        underline=True,
                        href="#",  # Replace with actual navigation link
                    ),
                ]
            )
        )

    # Create question boxes with validation and progress update
    question_boxes = []
    for i, (question, field) in enumerate(questions):
        box = ft.Column(
            [
                ft.Text(question, size=20),
                field,
                ft.FilledButton(
                    text="Submit",
                    # on_click=lambda: (
                    #     completed_steps += 1 if is_numeric(field.value) else 0,
                    #     progress_bar.value = completed_steps,
                    #     submit_form() if completed_steps == 3 else None,
                    # ),
                ),
            ]
        )
        question_boxes.append(box)

    # Navigation bar based on "navbar_sample.png" and your specifications
    navigation_bar = ft.AppBar(
        leading=ft.Image(src="logo.png"),
        title="FundusAI Reward System",
        actions=[
            # TODO: href
            ft.TextButton("Input Data"),
            ft.TextButton("Redeem"),
        ],
        bgcolor="#0447B8",  # Company primary color
        color="#FF9839",  # Company secondary color
    )
    
    # Dashboard section design based on "dashboard_body_sample.png"
    dashboard_section = ft.Column(
        [
            ft.Card(
                content=ft.Column(
                    [
                        ft.Text("Total Points", size=24, weight="bold"),
                        ft.Text("1234", size=36, weight="bold"),
                    ]
                ),
                color="#FF9839",
                elevation=4,
            ),
            ft.Card(
                content=ft.Column(
                    [
                        ft.Text("Physical Activity Tracking", size=20, weight="bold"),
                        # Placeholder charts based on "dashboard_body_sample.png"
                        ft.Row(
                            [
                                ft.Container(
                                    [
                                        ft.Text("Steps Chart"),
                                    ],
                                    width=200,
                                    height=200,
                                ),
                                ft.Container(
                                    [
                                        ft.Text("Distance Chart"),
                                    ],
                                    width=200,
                                    height=200,
                                ),
                            ]
                        ),
                        ft.Row(
                            [
                                ft.Container(
                                    [
                                        ft.Text("Other Activity Chart"),
                                    ],
                                    width=200,
                                    height=200,
                                ),
                            ]
                        ),
                    ]
                ),
            ),
            ft.Card(
                content=ft.Column(
                    [
                        ft.Text("Appointments and Diagnosis", size=20, weight="bold"),
                        # Appointments section
                        ft.Text("Upcoming Appointments:", size=16),
                        # Placeholder list of appointments
                        # ft.List(
                        #     [
                        #         ft.ListItem(
                        #             leading=ft.Text("Doctor Appointment"),
                        #             trailing=ft.Text("2024-02-15"),
                        #         ),
                        #         ft.ListItem(
                        #             leading=ft.Text("Dentist Appointment"),
                        #             trailing=ft.Text("2024-03-01"),
                        #         ),
                        #     ]
                        # ),
                        # # Diagnosis section
                        # ft.Text("Recent Diagnosis:", size=16),
                        # # Placeholder list of diagnoses
                        # ft.List(
                        #     [
                        #         ft.ListItem(
                        #             leading=ft.Text("Common Cold"),
                        #             trailing=ft.Text("2024-01-20"),
                        #         ),
                        #     ]
                        # ),
                    ]
                )
            ),
        ]
    )

    # Page layout with navigation and sections
    page.controls.append(
        ft.Column(
            [navigation_bar, dashboard_section]
        )
    )

    page.title = "FundusAI Reward System"
    page.update()

ft.app(target=main)
