@client.event
async def on_message(message):
    # Your code for on_message events

    await client.process_commands(message)

@client.command()
async def my_command(ctx):
    # Your code for the command
