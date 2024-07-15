def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print("Error: template should be a string")
        return

    if not isinstance(attendees, list):
        print("Error: attendees should be a list of dictionaries")
        return

    if not template:
        print("Error: Template is empty, no output files generated.")
        return

    if not attendees:
        print("Error: No data provided, no output files generated.")
        return

    for i, attendee in enumerate(attendees, start=1):
        output = template
        for key, value in attendee.items():
            output = output.replace("{" + key + "}", str(value) if value else "N/A")
        with open(f"output_{i}.txt", "w") as file:
            file.write(output)
